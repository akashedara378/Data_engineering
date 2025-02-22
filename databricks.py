# Define parameters in Databricks
dbutils.widgets.text("input_file", "")
dbutils.widgets.text("output_path", "")
dbutils.widgets.text("run_date", "")

# Read parameters
input_file = dbutils.widgets.get("input_file")
output_path = dbutils.widgets.get("output_path")
run_date = dbutils.widgets.get("run_date")

print(f"Processing file: {input_file}, Output path: {output_path}, Run date: {run_date}")
