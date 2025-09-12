🔹 ZORDER BY in Delta Lake
Purpose:
ZORDER BY is used to optimize data skipping during queries by co-locating related data in the same set of files. This is especially useful for columns that are frequently used in filters (e.g., WHERE clauses).
How it works:

Delta Lake uses data skipping to avoid scanning irrelevant files.
ZORDER BY physically reorganizes the data using a multi-dimensional clustering technique (Z-order curve).
It improves query performance by reducing the number of files scanned.

OPTIMIZE my_table
ZORDER BY (member_id, diagnosis_code)

                                                                                          


                                                                                        
