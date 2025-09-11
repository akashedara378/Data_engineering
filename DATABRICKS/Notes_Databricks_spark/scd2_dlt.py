import dlt
from pyspark.sql.functions import col, lit, current_timestamp

# 1. Bronze Layer: Ingest raw customer data (streaming or batch)
@dlt.table(
    name="bronze_customers",
    comment="Raw customer data from source."
)
def bronze_customers():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load("/FileStore/tables/customer_streaming/")
    )

# 2. Silver Layer: Clean and prepare data
@dlt.table(
    name="silver_customers",
    comment="Cleaned customer data."
)
def silver_customers():
    df = dlt.read("bronze_customers")
    return (
        df
        .withColumn("effective_date", current_timestamp())
        .withColumn("is_current", lit(True))
    )

# 3. Gold Layer: SCD2 implementation
@dlt.table(
    name="gold_customers_scd2",
    comment="SCD2 table tracking historical changes for customers."
)
def gold_customers_scd2():
    new_df = dlt.read("silver_customers")
    existing_df = dlt.read_stream("gold_customers_scd2")  # Use read_stream for incremental updates

    # Join on business key (e.g., customer_id)
    join_cond = [new_df.customer_id == existing_df.customer_id, existing_df.is_current == True]

    # Find changed records
    changed = (
        new_df.join(existing_df, join_cond, "left_outer")
        .filter(
            (existing_df.customer_id.isNull()) |  # New customer
            (new_df.name != existing_df.name) |   # Changed attributes
            (new_df.email != existing_df.email) |
            (new_df.country != existing_df.country)
        )
    )

    # Mark old records as not current
    expired = (
        existing_df.join(changed, "customer_id", "inner")
        .withColumn("is_current", lit(False))
        .withColumn("expired_date", current_timestamp())
    )

    # Prepare new records
    new_records = changed.withColumn("is_current", lit(True)).withColumn("effective_date", current_timestamp())

    # Union new and expired records with unchanged current records
    unchanged = existing_df.filter(existing_df.is_current == True).join(changed, "customer_id", "left_anti")
    result = unchanged.unionByName(expired).unionByName(new_records)

    return result
