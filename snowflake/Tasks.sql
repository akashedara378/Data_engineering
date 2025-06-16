CREATE OR REPLACE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::your_account_id:role/your_snowflake_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://your-bucket-name/your-folder/');



CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = 'CSV'
  SKIP_HEADER = 1
  FIELD_DELIMITER = ',';


CREATE OR REPLACE STAGE ext_stage
  URL = 's3://my-bucket/logs/'
  STORAGE_INTEGRATION = s3_int
  FILE_FORMAT = csv_format;


CREATE OR REPLACE EXTERNAL TABLE ext_events (
  event_id INT AS (VALUE:c1::INT),
  event_type STRING AS (VALUE:c2),
  source STRING AS (VALUE:c3)
)
WITH LOCATION = @ext_stage
AUTO_REFRESH = FALSE;

CREATE OR REPLACE STREAM ext_events_stream 
ON TABLE ext_events 
APPEND_ONLY = TRUE;


CREATE OR REPLACE TABLE clean_events (
  event_id INT,
  event_type STRING,
  source STRING
);


CREATE OR REPLACE TASK load_clean_events_task
  WAREHOUSE = my_wh
  SCHEDULE = '5 MINUTE'
AS
INSERT INTO clean_events
SELECT event_id, event_type, source
FROM ext_events_stream;


ALTER TASK load_clean_events_task RESUME;

-- (for testing)
EXECUTE TASK load_clean_events_task;



