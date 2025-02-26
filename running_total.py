from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import sum

# Initialize Spark Session
spark = SparkSession.builder.appName("RunningTotal").getOrCreate()

# Sample Data (Multiple Rows per ID)
data = [
    (1, "2024-02-01", 100),
    (1, "2024-02-02", 300),
    (1, "2024-02-03", 200),
    (2, "2024-02-01", 400),
    (2, "2024-02-02", 500),
    (3, "2024-02-01", 600)
]

# Create DataFrame
columns = ["id", "date", "sales"]
df = spark.createDataFrame(data, columns)

# Define Window Spec (Partition by ID, Order by Date) - No rowsBetween
window_spec = Window.partitionBy("id").orderBy("date")

# Running Total Without rowsBetween
df_running_total = df.withColumn("running_total", sum("sales").over(window_spec))

window_spec_rows = Window.partitionBy("id").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_running_total.show()



#  If you need custom windowing logic, such as:

# Rolling sums for last N rows (e.g., last 3 days)
# Moving Averages
# Resetting window boundaries dynamically

window_spec_last_3 = Window.partitionBy("id").orderBy("date").rowsBetween(-2, Window.currentRow)
df_last_3_sum = df.withColumn("last_3_day_sum", sum("sales").over(window_spec_last_3))
df_last_3_sum.show()



