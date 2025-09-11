from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit
from delta.tables import DeltaTable

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SCD2 Implementation") \
    .getOrCreate()

# Load new source data
df_source = spark.read.format("parquet").load("/mnt/source/silver_customers") \
    .withColumn("effective_date", current_timestamp()) \
    .withColumn("expired_date", lit(None).cast("timestamp")) \
    .withColumn("is_current", lit(True))

# Define Delta table path
delta_table_path = "/mnt/delta/gold_customers_scd2"

# Load target Delta table
delta_table = DeltaTable.forPath(spark, delta_table_path)

# Step 1: Expire old records where data has changed
delta_table.alias("target").merge(
    source=df_source.alias("source"),
    condition="""
        target.customer_id = source.customer_id AND target.is_current = true AND (
            target.name != source.name OR
            target.email != source.email OR
            target.country != source.country
        )
    """
).whenMatchedUpdate(set={
    "is_current": "false",
    "expired_date": "current_timestamp()"
}).execute()

# Step 2: Insert new records (new or changed)
delta_table.alias("target").merge(
    source=df_source.alias("source"),
    condition="target.customer_id = source.customer_id AND target.is_current = true"
).whenNotMatchedInsert(values={
    "customer_id": "source.customer_id",
    "name": "source.name",
    "email": "source.email",
    "country": "source.country",
    "effective_date": "source.effective_date",
    "expired_date": "source.expired_date",
    "is_current": "source.is_current"
}).execute()
