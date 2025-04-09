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
