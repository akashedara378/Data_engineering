# Load new data
df_source = spark.read.format("parquet").load("/mnt/source/silver_customers")

# Load Delta table
delta_table_path = "/mnt/delta/gold_customers_scd1"
delta_table = DeltaTable.forPath(spark, delta_table_path)

# Merge: overwrite matching records, insert new ones
delta_table.alias("target").merge(
    source=df_source.alias("source"),
    condition="target.customer_id = source.customer_id"
).whenMatchedUpdateAll() \
 .whenNotMatchedInsertAll() \
 .execute()


from pyspark.sql.functions import col
from delta.tables import DeltaTable

# Load new data
df_source = spark.read.format("parquet").load("/mnt/source/silver_customers")

# Load existing Delta table as DataFrame
delta_table_path = "/mnt/delta/gold_customers_scd1"
delta_table = DeltaTable.forPath(spark, delta_table_path)
df_target = delta_table.toDF()

# Remove old versions of matching records
df_non_matching = df_target.join(df_source, "customer_id", "left_anti")

# Combine new and non-matching records
df_final = df_non_matching.unionByName(df_source)

# Overwrite the Delta table
df_final.write.format("delta").mode("overwrite").save(delta_table_path)
