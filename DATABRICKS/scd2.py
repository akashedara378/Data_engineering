from pyspark.sql.functions import current_timestamp, lit
from delta.tables import DeltaTable

# Load new data
df_source = spark.read.format("parquet").load("/mnt/source/silver_customers") \
    .withColumn("effective_date", current_timestamp()) \
    .withColumn("expired_date", lit(None).cast("timestamp")) \
    .withColumn("is_current", lit(True))

# Load existing Delta table
delta_table_path = "/mnt/delta/gold_customers_scd2"
delta_table = DeltaTable.forPath(spark, delta_table_path)
df_target = delta_table.toDF()

# Join to detect changes
join_cond = df_source["customer_id"] == df_target["customer_id"]
df_joined = df_source.join(df_target.filter("is_current = true"), join_cond, "left_outer")

# Identify changed records
df_changed = df_joined.filter(
    df_target["customer_id"].isNull() |
    (df_source["name"] != df_target["name"]) |
    (df_source["email"] != df_target["email"]) |
    (df_source["country"] != df_target["country"])
).select(df_source.columns)

# Expire old records
df_expired = df_target.join(df_changed, "customer_id", "inner") \
    .withColumn("is_current", lit(False)) \
    .withColumn("expired_date", current_timestamp())

# Get unchanged records
df_unchanged = df_target.filter("is_current = true") \
    .join(df_changed, "customer_id", "left_anti")

# Final union
df_final = df_unchanged.unionByName(df_expired).unionByName(df_changed)

# Overwrite the Delta table
df_final.write.format("delta").mode("overwrite").save(delta_table_path)
