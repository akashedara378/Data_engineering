CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Glucose@1';

CREATE DATABASE SCOPED CREDENTIAL ManagedIdentity
WITH IDENTITY = 'Managed Identity';


CREATE EXTERNAL DATA SOURCE taxilake
WITH (
    LOCATION = 'https://nyctaxidatalake378.dfs.core.windows.net/bronze/'
    CREDENTIAL = ManagedIdentity
);

-- This is auto-generated code
SELECT
    TOP 100 *
FROM
    OPENROWSET(
        BULK 'https://nyctaxidatalake378.dfs.core.windows.net/bronze/revenue_star.csv',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0'
    ) AS rows


CREATE EXTERNAL FILE FORMAT CsvFileFormat
WITH (
    FORMAT_TYPE = DELIMITEDTEXT,
    FORMAT_OPTIONS (
        FIELD_TERMINATOR = ',',
        STRING_DELIMITER = '"',
        USE_TYPE_DEFAULT = TRUE
    )
);

CREATE EXTERNAL FILE FORMAT ParquetFileFormat
WITH
(
    FORMAT_TYPE = PARQUET
);


DROP EXTERNAL TABLE SalesData;

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
    FILE_FORMAT= CsvFileFormat
);

select * from SalesData;


--- CETAS
CREATE EXTERNAL TABLE sales_cetas
WITH
(
    LOCATION='sales_cetas',
    DATA_SOURCE=taxilake,
    FILE_FORMAT=ParquetFileFormat
)
AS
SELECT *
FROM
    OPENROWSET(
        BULK 'sales',
        DATA_SOURCE= 'taxilake',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW=TRUE
    ) AS query1


--- view
CREATE view sales_view
AS
SELECT *
 FROM
    OPENROWSET(
        BULK 'sales',
        DATA_SOURCE= 'taxilake',
        FORMAT = 'CSV',
        PARSER_VERSION = '2.0',
        HEADER_ROW=TRUE
    ) AS query1


select * from sales_view;



