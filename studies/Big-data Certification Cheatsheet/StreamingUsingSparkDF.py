# Databricks notebook source
from pyspark.sql import SparkSession
SparkSession.builder.appName("StreamingDF").getOrCreate()
word = spark.readStream.text("/FileStore/tables")
#read every files that lands in this directory while 
#rdd only considers newly landed files, df considers all the exisiting files


# COMMAND ----------

# word.writeStream.format("console").start() ##use regular df write instead of this shit

# COMMAND ----------

df =  word.groupBy("value").count() #will keep on updating count, will consider all copies of file and words in a file (in our example)
#can do all transformation using dataframe here
display(df)

# COMMAND ----------


