USE YourDatabaseName;
EXEC sys.sp_cdc_enable_db;

EXEC sys.sp_cdc_disable_db;

EXEC sys.sp_cdc_enable_table
@source_schema = N'dbo',  
@source_name   = N'Orders',  
@role_name     = NULL;

EXEC sys.sp_cdc_disable_table
@source_schema = N'dbo',  
@source_name   = N'Orders';


SELECT is_cdc_enabled FROM sys.databases WHERE name = 'YourDatabaseName';


CREATE TABLE dbo.Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME,
    Amount DECIMAL(10,2)
);


-- cdc.dbo_Orders_CT After enabling CDC on this table, SQL Server creates a change table named:

SELECT * FROM cdc.dbo_Orders_CT;

🧠 What Do These Mean?
$operation:

1 = Delete
2 = Insert
3 = Update (Before)
4 = Update (After)

$update_mask: Binary mask showing which columns were updated.



