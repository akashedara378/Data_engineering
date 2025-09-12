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


from pyspark.sql import SparkSession
from delta.tables import DeltaTable

# Initialize Spark session
spark = SparkSession.builder.appName("DeltaExample").getOrCreate()

# Define Delta Table Path in ADLS
delta_path = "/mnt/datalake/delta/employees"

# Sample data
data = [
    (1, "Alice", "Data Engineer", 70000),
    (2, "Bob", "Cloud Engineer", 80000),
    (3, "Charlie", "Python Developer", 75000)
]

# Define schema
columns = ["id", "name", "role", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Write DataFrame as a Delta Table
df.write.format("delta").mode("overwrite").save(delta_path)

# Read Delta Table
df_read = spark.read.format("delta").load(delta_path)
df_read.show()

# Load Delta Table
delta_table = DeltaTable.forPath(spark, delta_path)

# Insert New Records
new_data = [(4, "David", "ML Engineer", 90000), (5, "Emma", "DevOps Engineer", 85000)]
df_new = spark.createDataFrame(new_data, columns)

delta_table.alias("old").merge(
    df_new.alias("new"),
    "old.id = new.id"
).whenNotMatchedInsertAll().execute()

delta_table.alias("old").merge(
    df_new.alias("new"),
    "old.id = new.id"
).whenMatchedUpdate(set={"old.salary": "new.salary"}).whenNotMatchedInsertAll().execute()

# Delete a Record
delta_table.delete("id = 3")  # Deletes Charlie's record

# Read updated data
df_updated = spark.read.format("delta").load(delta_path)
df_updated.show()
