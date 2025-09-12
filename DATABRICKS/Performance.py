🔹 ZORDER BY in Delta Lake
Purpose:
ZORDER BY is used to optimize data skipping during queries by co-locating related data in the same set of files. This is especially useful for columns that are frequently used in filters (e.g., WHERE clauses).
How it works:

Delta Lake uses data skipping to avoid scanning irrelevant files.
ZORDER BY physically reorganizes the data using a multi-dimensional clustering technique (Z-order curve).
It improves query performance by reducing the number of files scanned.
                                                                                          
OPTIMIZE my_table
ZORDER BY (member_id, diagnosis_code)

OPTIMIZE delta.`/mnt/datalake/healthcare/FACT_HCE`
ZORDER BY (member_id, service_date)                                                                                          

Best used when:
you have large datasets.
You frequently filter on specific columns.
You want to reduce query latency.                                                                                          




🔹 VACUUM in Delta Lake
Purpose:
VACUUM is used to clean up old files that are no longer needed due to updates or deletes. Delta Lake uses versioning, so it keeps older versions of data for time travel and rollback.
How it works:

When you update or delete data, Delta Lake creates new files and marks old ones as obsolete.
VACUUM removes these obsolete files to free up storage.

VACUUM my_table RETAIN 168 HOURS


🔹 What is AQE (Adaptive Query Execution)?
AQE is a feature in Spark SQL that dynamically optimizes query plans at runtime based on actual data statistics. 
  It helps improve performance by making smarter decisions after the query starts executing.  

✅ Key Features of AQE
1. tuning shuffle partitions: 200 part but df is having only 15 distinct keys.spark will colease into 15 part.
2. optimizing joins: SMJ(sort merge join to BJ join).
3. optimizing skewing joins: large part into smaller part.

                                                                                          

                                                                                        
