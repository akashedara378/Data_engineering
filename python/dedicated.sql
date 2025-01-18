
CREATE DATABASE SCOPED CREDENTIAL ManagedIdentity
WITH IDENTITY = 'Managed Identity';


CREATE EXTERNAL DATA SOURCE taxilake
WITH (
    LOCATION = 'abfss://bronze@nyctaxidatalake378.dfs.core.windows.net/bronze/'
    CREDENTIAL = ManagedIdentity
);


CREATE EXTERNAL FILE FORMAT ParquetFileFormat
WITH
(
    FORMAT_TYPE = PARQUET
);


COPY INTO SalesData
(Dealer_ID, Model_ID, Branch_ID, Date_ID, Units_Sold, Revenue)
FROM 'https://nyctaxidatalake378.dfs.core.windows.net/bronze/sales_cetas/'
WITH (
    FILE_FORMAT = ParquetFileFormat,
    CREDENTIAL = (IDENTITY = 'ManagedIdentity'),
);


CREATE EXTERNAL TABLE SalesData (
    Dealer_ID VARCHAR(4000),
    Model_ID VARCHAR(4000),
    Branch_ID VARCHAR(4000),
    Date_ID VARCHAR(4000),
    Units_Sold VARCHAR(4000),
    Revenue VARCHAR(4000)
)
WITH
(
    LOCATION = 'sales',
    DATA_SOURCE= taxilake,
    FILE_FORMAT= ParquetFileFormat
);


--- ctas
CREATE TABLE polybase_table
WITH
(
    DISTRIBUTION=ROUND_ROBIN
) AS
select * from SalesData
