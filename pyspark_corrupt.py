corrupt records:
PERMISSIVE	(Default) Tries to parse all rows. If a row is corrupt, it puts it in the _corrupt_record column.
DROPMALFORMED	Skips rows that don’t match the schema.
FAILFAST	Fails immediately when it sees a bad record.
LEGACY	Used in earlier versions (not common anymore).

df = spark.read.format("json").option("badRecordsPath", "/bad_records/").load("path")
df = spark.read.format("csv").option("mode", "DROPMALFORMED").load("path")
df = spark.read.format("csv").option("mode", "FAILFAST").load("path")

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HandleDuplicates").getOrCreate()

# Read CSV with corrupt record handling
df = spark.read \
    .option("header", True) \
    .option("mode", "PERMISSIVE") \
    .option("columnNameOfCorruptRecord", "_corrupt_record") \
    .csv("/path/to/input.csv")

# Filter out only valid rows
valid_df = df.filter(df["_corrupt_record"].isNull()).drop("_corrupt_record")

corrupt_df = df.filter(df["_corrupt_record"].isNotNull())
corrupt_df.write.mode("overwrite").json("/path/to/output/corrupt_data")

# Drop exact duplicate rows
distinct_df = valid_df.dropDuplicates()

# Find duplicate rows (records that appeared more than once)
from pyspark.sql.functions import count, col

duplicate_df = valid_df.groupBy(valid_df.columns).count().filter("count > 1").drop("count")

# ✅ Save clean records
distinct_df.write.mode("overwrite").csv("/path/to/clean_records")

# ✅ Save duplicates (for auditing or further inspection)
duplicate_df.write.mode("overwrite").csv("/path/to/duplicate_records")

# Step 1: Find duplicate ids
duplicate_ids_df = df.groupBy("id").count().filter("count > 1").select("id")

# Step 2: Get rows with duplicate ids
duplicate_rows_df = df.join(duplicate_ids_df, on="id", how="inner")

# Step 3: Get distinct rows (keep only 1 row per id)
distinct_rows_df = df.dropDuplicates(["id"])
