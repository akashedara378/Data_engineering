-- Internal

CREATE OR REPLACE TABLE employee_task_internal (
  emp_id INT,
  emp_name STRING,
  department STRING
);


INSERT INTO employee_task_internal VALUES
  (1, 'Alice', 'HR'),
  (2, 'Bob', 'IT');

CREATE OR REPLACE STREAM employee_task_stream
ON TABLE employee_task_internal
APPEND_ONLY = TRUE;


CREATE OR REPLACE TABLE employee_task_target (
  emp_id INT,
  emp_name STRING,
  department STRING
);


CREATE OR REPLACE TASK load_employee_history_task
  WAREHOUSE = WAR1
  SCHEDULE = '1 MINUTE'
AS
INSERT INTO employee_task_target
SELECT a.emp_id, a.emp_name, a.department FROM employee_task_stream a;


ALTER TASK load_employee_history_task RESUME;


-- TESTING
INSERT INTO employee_task_internal VALUES
  (3, 'Charlie', 'Finance'),
  (4, 'Diana', 'HR');


EXECUTE TASK load_employee_history_task;


SELECT * FROM employee_task_target;

SELECT * from employee_task_internal;

SELECT * FROM employee_task_stream;



SELECT *
FROM TABLE(SNOWFLAKE.INFORMATION_SCHEMA.TASK_HISTORY())
WHERE TASK_NAME = 'LOAD_EMPLOYEE_HISTORY_TASK'
ORDER BY COMPLETED_TIME DESC;

SHOW TASKS;

SELECT * FROM TABLE (INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME =>  'load_employee_history_task'));

-- EXTERNAL

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



