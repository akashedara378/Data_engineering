# streaming
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr
from pyspark.sql.types import StructType, StringType, TimestampType

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("AuthorizationStreamProcessor") \
    .config("spark.sql.streaming.schemaInference", "true") \
    .getOrCreate()

# Step 2: Define schema for incoming JSON
schema = StructType() \
    .add("auth_id", StringType()) \
    .add("member_id", StringType()) \
    .add("diagnosis_code", StringType()) \
    .add("request_time", TimestampType()) \
    .add("priority", StringType())

# Step 3: Read from Kafka
raw_stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "auth_requests") \
    .option("startingOffsets", "latest") \
    .load()

# Step 4: Parse JSON from Kafka value
parsed_df = raw_stream_df.selectExpr("CAST(value AS STRING) as json_str") \
    .select(from_json(col("json_str"), schema).alias("data")) \
    .select("data.*")

# Step 5: Filter high-risk diagnosis codes
high_risk_df = parsed_df.filter(col("diagnosis_code").isin("C34.1", "I21.9", "J45.9"))

# Step 6: Write to Delta Lake
query = high_risk_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/delta/checkpoints/auth_stream") \
    .option("path", "/mnt/delta/tables/high_risk_auths") \
    .trigger(processingTime="1 minute") \
    .start()

query.awaitTermination()


# event bases streaming
from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col
from pyspark.sql.types import StructType, StringType, TimestampType

# Spark session
spark = SparkSession.builder.appName("WatermarkExample").getOrCreate()

# Schema
schema = StructType() \
    .add("auth_id", StringType()) \
    .add("member_id", StringType()) \
    .add("diagnosis_code", StringType()) \
    .add("request_time", TimestampType())

# Simulated stream (replace with Kafka in production)
stream_df = spark.readStream \
    .format("json") \
    .schema(schema) \
    .load("/path/to/incoming/json/files")  # or Kafka source

# Apply watermark and windowed aggregation
aggregated_df = stream_df \
    .withWatermark("request_time", "15 minutes") \
    .groupBy(window(col("request_time"), "10 minutes")) \
    .count()

# Write to console or sink
query = aggregated_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()


# late data
from pyspark.sql.functions import expr, current_timestamp

# Define watermark
main_df = parsed_df.withWatermark("request_time", "15 minutes")

# Filter late data
late_data_df = parsed_df.filter(
    col("request_time") < expr("current_timestamp() - interval 15 minutes")
)

# Write late data to a separate Delta table
late_data_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/delta/checkpoints/late_data") \
    .option("path", "/mnt/delta/tables/late_auths") \
    .start()

# we can also use delta lake merge command to upsert..
