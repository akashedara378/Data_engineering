
# -- It automates the creation and management of Delta Tables through declarative ETL logic.
# -- we declare what we want and DLT take cares of how it will be done.

# -- data quality checks will be done using Execptions(rules). if it fails it will be sent to quarantine..
# -- supports streaming and incremental loading.


import dlt
from pyspark.sql.functions import col, lower, trim

# BRONZE: Raw data ingestion (streaming)
@dlt.table(
    name="bronze_customers",
    comment="Bronze layer: Raw streaming customer data."
)
def bronze_customers():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load("/FileStore/tables/customer_streaming/")
    )

# SILVER: Data cleaning and enrichment
@dlt.table(
    name="silver_customers",
    comment="Silver layer: Cleaned and standardized customer data."
)
def silver_customers():
    df = dlt.read("bronze_customers")
    return (
        df
        .withColumn("email", lower(trim(col("email"))))
        .withColumn("country", trim(col("country")))
        .filter(col("email").isNotNull())
    )

# GOLD: Aggregation and business logic
@dlt.table(
    name="gold_customer_summary",
    comment="Gold layer: Aggregated customer counts by country and type."
)
def gold_customer_summary():
    df = dlt.read("silver_customers")
    return (
        df.groupBy("country", "customer_type")
          .count()
          .withColumnRenamed("count", "customer_count")
    )

# Optional: Reporting view for active customers
@dlt.view(
    name="active_customers_view"
)
def active_customers_view():
    return spark.sql("""
        SELECT * FROM LIVE.gold_customer_summary WHERE customer_count > 10
    """)



import dlt
from pyspark.sql.functions import col, lower, trim

# 1. Streaming ingestion (Bronze Layer)
@dlt.table(
    name="customer_streaming_table",
    comment="Bronze layer: Raw streaming customer data."
)
def customer_streaming_table():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .load("/FileStore/tables/customer_streaming/")
    )

# 2. Batch ingestion (Bronze Layer)
@dlt.table(
    name="customer_batch_table",
    comment="Bronze layer: Raw batch customer data."
)
def customer_batch_table():
    return (
        spark.read
        .format("csv")
        .option("header", "true")
        .load("/FileStore/tables/customer_batch/")
    )

# 3. Silver Layer: Combine and clean data from both sources, with expectations
@dlt.table(
    name="silver_customers",
    comment="Silver layer: Combined and cleaned customer data from streaming and batch sources."
)
@dlt.expect("valid_email", "email IS NOT NULL AND email LIKE '%@%'")
@dlt.expect_or_drop("valid_age", "age IS NOT NULL AND age > 0")
def silver_customers():
    streaming_df = dlt.read("customer_streaming_table")
    batch_df = dlt.read("customer_batch_table")
    combined_df = streaming_df.unionByName(batch_df)
    return (
        combined_df
        .withColumn("email", lower(trim(col("email"))))
        .withColumn("country", trim(col("country")))
        .withColumn("age", col("age").cast("int"))
    )

# 4. Gold Layer: Aggregation and business logic
@dlt.table(
    name="gold_customer_summary",
    comment="Gold layer: Aggregated customer counts by country and type."
)
def gold_customer_summary():
    df = dlt.read("silver_customers")
    return (
        df.groupBy("country", "customer_type")
          .count()
          .withColumnRenamed("count", "customer_count")
    )

# 5. Reporting view (optional)
@dlt.view(
    name="active_customers_view"
)
def active_customers_view():
    return spark.sql("""
        SELECT * FROM LIVE.gold_customer_summary WHERE customer_count > 10
    """)
