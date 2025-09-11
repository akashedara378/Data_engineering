-- BRONZE: Ingest raw streaming data
CREATE OR REFRESH STREAMING LIVE TABLE bronze_customers
COMMENT "Bronze layer: Raw streaming customer data."
AS SELECT * FROM cloud_files("/FileStore/tables/customer_streaming/", "csv");

-- SILVER: Clean and standardize data
CREATE OR REFRESH LIVE TABLE silver_customers
COMMENT "Silver layer: Cleaned and standardized customer data."
AS
SELECT
  lower(trim(email)) AS email,
  trim(country) AS country,
  customer_type,
  *
FROM LIVE.bronze_customers
WHERE email IS NOT NULL;

-- GOLD: Aggregate for business reporting
CREATE OR REFRESH LIVE TABLE gold_customer_summary
COMMENT "Gold layer: Aggregated customer counts by country and type."
AS
SELECT
  country,
  customer_type,
  COUNT(*) AS customer_count
FROM LIVE.silver_customers
GROUP BY country, customer_type;

-- Reporting view (optional)
CREATE OR REFRESH LIVE VIEW active_customers_view
AS
SELECT * FROM LIVE.gold_customer_summary WHERE customer_count > 10;
