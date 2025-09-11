
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
