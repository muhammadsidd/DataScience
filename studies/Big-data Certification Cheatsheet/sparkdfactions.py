# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# COMMAND ----------

df = spark.read.options(header = 'True',inferSchema ='True').csv('/FileStore/tables/StudentData.csv')

# COMMAND ----------

df.show()

# COMMAND ----------

df.count() #number of rows

# COMMAND ----------

df.filter(col("course")=="DB").count()

# COMMAND ----------

#unique rows/records count
df.select("name","age").distinct().count() #distinct all the columns for unique record, it runs on rows 

# COMMAND ----------

df.dropDuplicates(["gender","course"]).show() #picks out the unique combination gender and course name 

# COMMAND ----------

### SORTING AND ORDER BY
df = df.sort("marks") #ascending order

# COMMAND ----------

df.show()

# COMMAND ----------

df.sort(df.marks.desc(),df.age.asc()).dropDuplicates(["name"]).show()

# COMMAND ----------

# df.withColumn("index",lit(enumerate df))

# COMMAND ----------

df.show()

# COMMAND ----------

df.count()

# COMMAND ----------

df2 = df.groupBy("gender").sum("marks")
df3 =  df.groupBy("gender").count() #groupBy should always be followed by some aggregation 
df2.show()
df3.show()
df3.count()
df4 = df.groupBy("name","course").sum("marks")
df4.select("name","course").distinct().show()
df4.filter(col("name").endswith("n")).show()

# COMMAND ----------

df69 = df.groupBy("name").max("marks")
df68 = df.groupBy("age").avg("marks")
df68.show()
df69.dropDuplicates(["name"]).show()

# COMMAND ----------


