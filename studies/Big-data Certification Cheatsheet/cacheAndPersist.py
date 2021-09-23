# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# COMMAND ----------

df =  spark.read.options(inferSchema = 'True', header = 'True').csv('/FileStore/tables/OfficeData.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

def getTotalsalary(salary,bonus):
  return salary + bonus

totalSalaryUDF = udf(lambda x,y: getTotalsalary(x,y), IntegerType())

df.withColumn("totalsalary", totalSalaryUDF(df.salary,df.bonus)).show()
df.cache()

# COMMAND ----------

def state_calc(state,salary,bonus):
  if state == 'NY':
    return (0.1*salary) + (0.05*bonus)
  elif state == 'CA':
    return (0.12*salary) + (0.03*bonus)

statecalc = udf(lambda x,y,z: state_calc(x,y,z), DoubleType())

df.withColumn("new_total", statecalc(df.state,df.salary,df.bonus)).show()
    

# COMMAND ----------


