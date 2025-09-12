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

dbutils.notebook.exit(str(my_var))
result = dbutils.notebook.run("other_notebook", 60)
print(result)  # will print the string output
