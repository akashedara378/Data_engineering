# Databricks notebook source
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PySpark Basics") \
    .config("spark.some.config.option", "value") \
    .getOrCreate()

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# Create DataFrame
data = [(1, "Alice", 25), (2, "Bob", 30)]
df = spark.createDataFrame(data, schema)
df.show()

# RDD
df2.rdd.getNumPartitions()
df3 =  df2.repartition(3)
df3.rdd.getNumPartitions()

# Reading Diff files.
df2 = spark.read.csv('/FileStore/tables/employee3.csv', header=True, inferSchema=True)

df1 = spark.read.format('csv').options(inferSchema=True, header=True).load('FileStore/tables/employee3.csv')

df1 = spark.read.format('json').option('inferSchema', True).option('header', True).option('multiline', False).load('/FileStore/drivers.json/')

my_ddl_schema = '''
                    Item_Identifier STRING,
                    Item_Weight STRING,
                    Item_Fat_Content STRING, 
                    Item_Visibility DOUBLE, '''

my_strct_schema = StructType([
                               StructField('Item_Identifier',StringType(),True),
                               StructField('Item_Weight',StringType(),True), 
                               StructField('Item_Fat_Content',StringType(),True), 
                                StructField('Item_Visibility',StringType(),True),])
                
df = spark.read.format('csv')\
                .schema(my_strct_schema)\
                .option('header', True)\
                .load('/FileStore/BigMart_Sales.csv')


df = spark.read.csv('/FileStore/tables/employee3.csv', header=True, inferSchema=True)

# writing diff files
df.write.csv("hdfs://namenode:9000/user/output/no_partition", header=True)
df.write.parquet("hdfs://namenode:9000/user/output/parquet")
df.write.partitionBy("age").csv("hdfs://namenode:9000/user/output/partitioned", header=True)
df.coalesce(1).write.csv("hdfs://namenode:9000/user/output/coalesce", header=True) #try to less shuffle data and give single file
df.repartition(1).write.csv("hdfs://namenode:9000/user/output", header=True) # more shuffle



# bucketing for skewness.
df.write.format("parquet").bucketBy(4, "id").saveAsTable("bucketed_table")
bucketed_df = spark.read.table("bucketed_table")
bucketed_df.show()

df1 = spark.read.table("bucketed_table")
df2 = spark.read.table("another_bucketed_table")  # Assume this is also bucketed on 'id'

# salting
from pyspark.sql.functions import col, concat_ws, lit, rand

# Add a random salt value (1-5) to store_id
df_salted = df.withColumn("salt", (rand() * 5).cast("int"))
df_salted = df_salted.withColumn("store_salt", concat_ws("_", col("store_id"), col("salt")))

# Now group by the new salted key instead of store_id
df_salted.groupBy("store_salt").sum("sales").show()

# Perform Optimized Join
joined_df = df1.join(df2, "id")

# The same store_id = 1 is now split across multiple partitions (1_0, 1_1, 1_2...).


# explode in json.
from pyspark.sql.functions import explode

json_df = spark.read.json("hdfs://namenode:9000/user/data/sample.json")
json_df_exploded = json_df.withColumn("exploded_col", explode(json_df["array_column"]))
json_df_exploded.show()

+---+-------------+-------------+
|id |array_column |exploded_col |
+---+-------------+-------------+
|1  |[A, B, C]    |A            |
|1  |[A, B, C]    |B            |
|1  |[A, B, C]    |C            |
|2  |[X, Y]       |X            |
|2  |[X, Y]       |Y            |
+---+-------------+-------------+


# transformations
df.select("name", "user").show()
df.select(df.name, df.user).display()
df.select(df.columns[1:3]).display()
df.select(col('Item_Identifier'),col('Item_Weight'),col('Item_Fat_Content')).display()

from pyspark.sql.functions import col
from pyspark.sql.functions import lit

df_with_new_col = df.withColumn("new_age", col("age") + 10)
df.withColumn('country',lit('usa')).show()
df_with_new_col.show()

# typecasting
df = df.withColumn('Item_Weight', col('Item_Weight').cast(StringType()))
df.printSchema()

df.drop(col('Item_Visibility')).display()
df.drop('Item_Visibility', 'col2').display()

df_no_duplicates = df.dropDuplicates() #removes duplicates rows
df.dropDuplicates(['name']).show()

df.distinct().show()

#difference
df1.subtract(df2).show()
df1.intersect(df2).show()

df_renamed = df.withColumnRenamed("name", "full_name")
df_renamed.show()

df.filter(col('Item_Fat_Content') == 'Regular').display()
df.filter((col('Item_Type') == 'Soft Drinks') & (col('Item_Weight')<10)).display()  
df.filter((col('Outlet_Size').isNull()) & (col('Outlet_Location_Type').isin('Tier 1','Tier 2'))).display()
df.filter((df.salary > 100) & (df.name == 'rahu')).show()
df.filter(df.name.startswith('r')).show()
df.filter(df.name.endswith('h')).show()
df.filter(df.name.like('%rn%')).show()

from pyspark.sql.functions import F

df_sorted = df.orderBy("age", ascending=False)
df.sort(df.salary).show()
df.sort(df.salary.desc()).show()
df.sort('salary', 'name').show()

df_grouped = df.groupBy("age").count()

# Average salary by location
df.groupBy('location').agg({"salary": "avg"}).show() 
df.groupBy('location').agg(F.avg('salary').alias('average_salary')).show()

df.groupBy('location').sum('salary').show()
df.groupBy('location').agg(F.sum('salary').alias('new_column_name')).show()

from pyspark.sql.functions import col,sum,count
df.groupBy('email').agg(count('email').alias('email_count')).filter(col('email_count')>1).select('email').show()
df.groupBy('email').count().show()

from pyspark.sql.functions import when

df_case = df.withColumn("age_group", when(df.age < 30, "Young").otherwise("Old"))
df_case.show()


# window Functions
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

window_spec = Window.partitionBy("age").orderBy("name")
df_window = df.withColumn("row_number", row_number().over(window_spec))
df_window.show()

win_spec = Window.partitionBy('Department').orderBy(df.Salary.desc())
df_row = df.withColumn('row_num', row_number().over(win_spec))
df_row.show()

from pyspark.sql.functions import rank
win_spec = Window.partitionBy('Department').orderBy(df.Salary.desc())

df_row = df.withColumn('row_num', rank().over(win_spec))

df_row.show()

from pyspark.sql.functions import dense_rank
win_spec = Window.partitionBy('Department').orderBy(df.Salary.desc())

df_row = df.withColumn('row_num', dense_rank().over(win_spec))
df_row.show()

# joins
df1 = spark.createDataFrame([(1, "Alice"), (2, "Bob")], ["id", "name"])
df2 = spark.createDataFrame([(1, "HR"), (2, "Engineering")], ["id", "dept"])

# Regular Join
df_join = df1.join(df2, "id")
df_join.show()

# Broadcast Join
from pyspark.sql.functions import broadcast
df_broadcast_join = df1.join(broadcast(df2), "id")
df_broadcast_join.show()

df_1.join(df_2, 'inner').show()
df_1.join(df_2, df_1.id == df_2.user_id, 'inner').show()

d1.union(d2).show() #no duplicates
d1.unionAll(d2).show()
d1.unionByName(d2).show() #based on column name.


# spark sql
df.createOrReplaceTempView("people")
result = spark.sql("SELECT * FROM people WHERE age > 25")
result.show()

data = [(1, "abc@gmail.com"), (2, "bcd@gmail.com"), (3, "abc@gmail.com")]
schema = "ID int,email string"
df = spark.createDataFrame(data, schema)

df.createOrReplaceTempView('email')
spark.sql(""" select email from (
                                    select email,count(*) as count
                                    from email
                                    group by email
                                    having count>1
                                )""").show()

# null values
df.na.fill(value)  # Fill all columns with 'value'
df.na.fill(value, subset=['col1', 'col2'])  # Fill specific columns

df.fillna(value)  # Fill all columns with 'value'
df.fillna(value, subset=['col1', 'col2'])  # Fill specific columns

d1.na.fill("", ['name']).na.fill("10",['id']).show()

# Drop rows with any null value
df.dropna()

# Drop rows where all values are null
df.dropna(how='all')

# Drop rows based on null values in specific columns
df.dropna(subset=["id"])

# Drop rows with fewer than 2 non-null values
df.dropna(thresh=2)

# Drop rows where either 'id' or 'value' is null
df.dropna(subset=["id", "value"], how="any")


# collect action
data = [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
columns = ['id', 'name']
df = spark.createDataFrame(data, columns)

# Using collect() to bring data to the driver
result = df.collect()
print(result)
for row in result:
    print(row)

#brings all data to driver. 


# pivot copvert row to column
# unpivot convert column to row

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("PivotExample").getOrCreate()

# Sample data
data = [(1, "Jan", 200), (1, "Feb", 300), (2, "Jan", 400), (2, "Feb", 500)]
columns = ["ID", "Month", "Sales"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Perform pivot
pivoted_df = df.groupBy("ID").pivot("Month").sum("Sales")

# Show the pivoted DataFrame
pivoted_df.show()

+---+---+---+
| ID|Jan|Feb|
+---+---+---+
|  1|200|300|
|  2|400|500|
+---+---+---+

# COMMAND ----------

from pyspark.sql.functions import expr

# Unpivot columns
unpivoted_df = pivoted_df.selectExpr("ID", "stack(2, 'Jan', Jan, 'Feb', Feb) as (Month, Sales)")

# Show the unpivoted DataFrame
unpivoted_df.show()


# udf
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf,col,upper

spark = SparkSession.builder.appName('udf').getOrCreate()
data = [("Alice", 29), ("Bob", 35), ("Cathy", 28)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()

def upper(a):
    return a.upper()

#reg_udf
udf1 = udf(upper, StringType())

df.select(udf1('Name').alias('Upper_Name'), 'Age').show()



from pyspark.sql.functions import upper
df.withColumn("Name", upper(df.Name)) \
  .show()

df.withColumn("Name2", upper(col('Name'))).show()



# Dates
from pyspark.sql.functions import current_date,current_timestamp
df = spark.createDataFrame([(1,)], ["id"])
df.withColumn("current_date", current_date()).show()
df.withColumn('current_timestamp', current_timestamp()).show()

from pyspark.sql.functions import date_format
df.withColumn("formatted_date", date_format(current_date(), "yyyy-MM-dd")).show()

from pyspark.sql.functions import to_date
df = spark.createDataFrame([("2024-12-30",)], ["date_string"])
df.withColumn("date", to_date("date_string", "yyyy-MM-dd")).show()

from pyspark.sql.functions import datediff, lit
df.withColumn("days_diff", datediff(lit("2025-01-01"), current_date())).show()

from pyspark.sql.functions import add_months
df.withColumn("next_month", add_months(current_date(), 1)).show()

from pyspark.sql.functions import date_add, date_sub
df.withColumn("add_5_days", date_add(current_date(), 5)).show()
df.withColumn("sub_5_days", date_sub(current_date(), 5)).show()


from pyspark.sql.functions import year, month, dayofmonth
df.withColumn("year", year(current_date())).show()
df.withColumn("month", month(current_date())).show()
df.withColumn("day", dayofmonth(current_date())).show()


from pyspark.sql.functions import last_day,next_day
df.withColumn("last_day", last_day(current_date())).show()
df.withColumn("last_day", next_day(current_date(), "Thursday")).show()



# collect set
data = [
    ("john", "tomato", 2),
    ("𝚋𝚒𝚕𝚕", "𝚊𝚙𝚙𝚕𝚎", 2),
    ("john", "𝚋𝚊𝚗𝚊𝚗𝚊", 2),
    ("john", "tomato", 3),
    ("𝚋𝚒𝚕𝚕", "𝚝𝚊𝚌𝚘", 2),
    ("𝚋𝚒𝚕𝚕", "𝚊𝚙𝚙𝚕𝚎", 2),
]
schema = "name string,item string,weight int"
df = spark.createDataFrame(data, schema)
df.display()

df1 = df.groupBy(df.name, df.item).sum("weight").withColumnRenamed("sum(weight)","total_weight")
df1.display()
from pyspark.sql.functions import collect_list, struct
df2 = df1.groupBy(df.name).agg(collect_set(struct("item","total_weight")).alias("total_items")).orderBy("name")
df2.display()

#rdd Map and Flatmap
rdd = sc.parallelize(["hello world", "how are you"])
mapped = rdd.map(lambda x: x.split(" "))
print(mapped.collect()) -> [['hello', 'world'], ['how', 'are', 'you']]

rdd = sc.parallelize(["hello world", "how are you"])
flat_mapped = rdd.flatMap(lambda x: x.split(" "))
print(flat_mapped.collect()) -> ['hello', 'world', 'how', 'are', 'you']

from pyspark import SparkContext
sc = SparkContext("local", "maps")
rd1 = sc.parallelize([1,2,3])
rd1_maped = rd1.map(lambda x:x*2)
rd1_maped.collect()

rd2 = sc.parallelize([1, 2, 3])
rd2_mapped = rd2.flatMap(lambda x: [x * 2, x * 3])
rd2_mapped.collect()

rd3 = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('b', 4)])
rd3_map = rd3.reduceByKey(lambda x,y:x+y)
rd3_map.collect()


#cache and persist
df.cache()
df.persist(StorageLevel.MEMORY_ONLY)
df.persist(StorageLevel.MEMORY_AND_DISK)



#Delta tables

# record bads
df = spark.read.format("json").option("badRecordsPath", "/bad_records/").load("path")
df = spark.read.format("csv").option("mode", "DROPMALFORMED").load("path")
df = spark.read.format("csv").option("mode", "FAILFAST").load("path")

# pytest
import pytest
from pyspark.sql import SparkSession
from my_spark_job import transform_data  # Your function to test

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[*]").appName("test").getOrCreate()

def test_transform_data(spark):
    input_data = [(1, "Alice", 25), (2, "Bob", 30)]
    schema = ["id", "name", "age"]
    input_df = spark.createDataFrame(input_data, schema)

    result_df = transform_data(input_df)  # Apply your transformation

    assert result_df.count() == 2
    assert result_df.filter(result_df.name == "Alice").count() == 1
