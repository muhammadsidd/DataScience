# Databricks notebook source
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("FilterData")
sc= SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile('/FileStore/tables/average_quiz_sample.csv')
rdd.collect()

# COMMAND ----------

rdd =  rdd.map(lambda x : (x.split(',')[0],x.split(',')[2]))
rdd.collect()

# COMMAND ----------

rdd2 = rdd.map(lambda x : (x[0],(float(x[1]),1)))
rdd2.collect()


# COMMAND ----------

rdd3 = rdd2.reduceByKey(lambda x,y: ((x[0]+y[0],x[1]+y[1])))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd4 =  rdd3.map(lambda x : (x[0],(x[1][0]/x[1][1])))

# COMMAND ----------

rdd4.collect()

# COMMAND ----------


