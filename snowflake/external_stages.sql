show tables;

-- it helps to access the s3
CREATE OR REPLACE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::your_account_id:role/your_snowflake_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://your-bucket-name/your-folder/');

-- descrieb Integration
DESC INTEGRATION s3_int;

CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = 'CSV'
  SKIP_HEADER = 1
  FIELD_DELIMITER = ','
  RECORD_DELIMITER = '\n';
  
CREATE OR REPLACE STAGE my_s3_stage
  URL = 's3://your-bucket-name/your-folder/'
  STORAGE_INTEGRATION = s3_int
  FILE_FORMAT = csv_format;

COPY INTO employee
FROM @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'csv_format');


-- for continous data loading.

CREATE OR REPLACE PIPE employee_pipe
  AUTO_INGEST = TRUE
  AS
  COPY INTO employee
  FROM @my_s3_stage
  FILE_FORMAT = (FORMAT_NAME = 'csv_format');

-- To trigger the pipe when a new file is uploaded:

-- Go to your S3 bucket > Properties > Event notifications

-- Create an event:

-- Event type: PUT

-- Prefix: folder path where files land

-- Destination: SNS topic(which snow pipe listen to)

-- Snowflake will provide the SNS topic and subscription when you run show pipes:


show pipes;
