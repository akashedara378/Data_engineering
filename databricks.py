#cluster details
1 Driver node: Standard_E8s_v3 (8 vCPUs, 64 GB RAM)
10 Executor (worker) nodes: Standard_E8s_v3 (each with 8 vCPUs, 64 GB RAM)
Total vCPUs: 80
Default parallelism: ~80
Shuffle partitions: Set to 800 (10x parallelism for better performance)**
You're telling Spark to split shuffled data into 800 partitions.

1,000,000 MB / 128 MB ≈ ~7800 partitions
 6000-8000 ideal and 300-400 mb of file.


# Define parameters in Databricks
dbutils.widgets.text("input_file", "")
dbutils.widgets.text("output_path", "")
dbutils.widgets.text("run_date", "")

# Read parameters
input_file = dbutils.widgets.get("input_file")
output_path = dbutils.widgets.get("output_path")
run_date = dbutils.widgets.get("run_date")

print(f"Processing file: {input_file}, Output path: {output_path}, Run date: {run_date}")



#Delta tables
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


# writing delta tables to sql db:
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("BulkDeltaToSQL") \
    .getOrCreate()

# Delta table locations in ADLS Gen2
delta_tables = {
    "customer": "abfss://<container>@<storage_account>.dfs.core.windows.net/delta/customer",
    "orders": "abfss://<container>@<storage_account>.dfs.core.windows.net/delta/orders",
    "products": "abfss://<container>@<storage_account>.dfs.core.windows.net/delta/products",
    "invoices": "abfss://<container>@<storage_account>.dfs.core.windows.net/delta/invoices",
    "returns": "abfss://<container>@<storage_account>.dfs.core.windows.net/delta/returns"
}

# JDBC connection details
jdbc_url = "jdbc:sqlserver://<onprem-ip>:1433;databaseName=<db_name>"
jdbc_properties = {
    "user": "<username>",
    "password": "<password>",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Loop over each delta table and load to SQL
for table_name, path in delta_tables.items():
    print(f"Processing table: {table_name}")
    df = spark.read.format("delta").load(path)

    # Write to on-prem SQL
    df.write \
        .jdbc(url=jdbc_url,
              table=table_name,
              mode="overwrite",  # or "append"
              properties=jdbc_properties)


#SCD2
# First expire old rows (update is_current and end_date)
delta_table.alias("target").merge(
    source_df.alias("source"),
    "target.emp_id = source.emp_id AND target.is_current = true AND (target.name != source.name OR target.city != source.city)"
).whenMatchedUpdate(set={
    "end_date": "current_date()",
    "is_current": "false"
}).whenNotMatchedInsert(values={
    "emp_id": "source.emp_id",
    "name": "source.name",
    "city": "source.city",
    "start_date": "source.start_date",
    "end_date": "source.end_date",
    "is_current": "source.is_current"
}).execute()


from delta.tables import DeltaTable
from pyspark.sql.functions import col

# Load target (gold) delta table
target_table = DeltaTable.forPath(spark, "<path-to-gold-table>")

# Load incoming data from silver/bronze
incoming_df = spark.read.format("delta").load("<path-to-incoming-data>")

# Optional: Filter incoming data to keep only latest (if required)
# incoming_df = incoming_df.withColumn("ingestion_ts", current_timestamp())

# Merge
target_table.alias("target").merge(
    incoming_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdate(condition="""
    target.col1 != source.col1 OR
    target.col2 != source.col2 OR
    target.col3 != source.col3
""", set={
    "col1": "source.col1",
    "col2": "source.col2",
    "col3": "source.col3"
}).whenNotMatchedInsertAll().execute()
