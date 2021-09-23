# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------



# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/test3.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x: x.split(" ")).filter(lambda x: len(x) != 0)

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.map(lambda x: (x,1))
rddt = rdd3.groupByKey().mapValues(list).collect()
rddt

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd4 =  rdd3.reduceByKey(lambda x,y: x+y).collect()

# COMMAND ----------

rdd4

# COMMAND ----------

rdd.count()

# COMMAND ----------

rdd.countByValue()

# COMMAND ----------

rdd2.countByValue()

# COMMAND ----------


