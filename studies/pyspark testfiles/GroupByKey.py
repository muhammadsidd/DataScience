# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/test3.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x: x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.filter(lambda x: not (x[0]=='a' or x[0]=='c'))

# COMMAND ----------

rdd4=rdd3.map(lambda x: (x,len(x)))

# COMMAND ----------

rdd4.groupByKey().mapValues(tuple).collect() #List not working so using tuple instead

# COMMAND ----------


