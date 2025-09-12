emp=spark.read.parquet(“/Volumes/dataengg/datalake/mydata/EMP.parquet”)
emp.write.saveAsTable("employees")

spark.read.table("employees").show()

delta_df = spark.read.format("delta").table("employees")
delta_df.show()

%sql
Select * from employees;

%sql
update default.employees set salary = 4000 where empno=7934

describe history employees;
select * from employees version as of 0;

milleroldsalary=spark.read.format("delta").option("versionAsOf","0").table('employees')
milleroldsalary.show()

# schema evoultion
# emps will have old file and new file(new schema)
Emp=spark.read.option(“header”,”true”).option(“inferschema”,”true”).csv(“/Volumes/dataengg/datalake/mydata/emps/”)
Emp.show(Emp.count())

Emp=spark.read.option("header","true").option("inferschema","true").csv("/Volumes/dataengg/datalake/emps/EMP.csv")
Emp.write.saveAsTable("dataengg.payroll.empinfo")

newEmp=spark.read.option("header","true").option("inferschema","true")
                  .csv("/Volumes/dataengg/datalake/emps/EMP_denormalized.csv")

newEmp.write.mode("append").saveAsTable("dataengg.payroll.empinfo") #will throw error

newEmp.write.mode("append").option("mergeSchema","true").saveAsTable("dataengg.payroll..empinfo")
