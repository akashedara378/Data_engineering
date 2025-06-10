show tables;

-- table stage
list @%employee;

-- user stage
list @~;

-- internal stage
list @internal_stage1;

create or replace stage internal_stage1;


drop stage internal_stage1;

truncate table employee;

select * from employee;

copy into employee
from @internal_stage1
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);


-- create file format
CREATE OR REPLACE FILE FORMAT csv_format
  TYPE = 'CSV'
  SKIP_HEADER = 1
  FIELD_DELIMITER = ','
  RECORD_DELIMITER = '\n';


copy into employee
from @internal_stage1
file_format = (format_name = csv_format);



create or replace stage internal_stage2 
FILE_FORMAT = csv_format;

show file formats;

