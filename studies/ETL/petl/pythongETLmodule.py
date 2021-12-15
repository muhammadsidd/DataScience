from pyspark.sql import SparkSession, udf
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
spark = SparkSession.builder.appName("Spark DataFrames").config("spark.jars", "/path_to_postgresDriver/postgresql-42.2.5.jar").getOrCreate()

# COMMAND ----------

df = spark.read.options(inferSchema = 'True', header = 'True').csv('developerdata.csv')

def getTotalsalary(salary,bonus):
  return salary + bonus

totalSalaryUDF = udf(lambda x,y: getTotalsalary(x,y), IntegerType())

dfsalary = df.filter(df.ConvertedComp > 75000).select("Respondent","Employment","Country")

print(dfsalary.count())

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/databasename") \
    .option("dbtable", "tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()
