# Databricks notebook source
from pyspark.streaming import StreamingContext
from pyspark import SparkConf, SparkContext


conf =  SparkConf().setAppName("Streaming")
sc =  SparkContext.getOrCreate(conf =  conf)

ssc =  StreamingContext(sc,5) #number represent time interval for checking new files in the directory


# COMMAND ----------

#need to refer to ssc instead of sc when using streaming need to specify the directory which keeps on refreshing 
#not a regular rdd its a datastream, cannot go for collect go for pprint
#any transformation can be applied to it after reading it onto rdd
rdd = ssc.textFileStream("/FileStore/tables/")

# COMMAND ----------

rdd = rdd.map(lambda x: (x,1))
rdd = rdd.reduceByKey(lambda x,y: x+y)
#need to run the directory first and then put the file, so it sees the directory updating 

rdd.pprint()

#after hitting these two statements it will start looking into the directory for refresh content
ssc.start()
#put timeout, if the user terminates it or 100 seconds after no change 
ssc.awaitTerminationOrTimeout(100)
#After running these statements if you run it again, it will throw an exception
#this is because after running it for the first time Spark creates a DAG and when u run it again it tries to expand that DAG, which is illegal
#restart the cluster/ clear the state
#if you face the same issue in you IDE then refer to the following command 
# ssc.stop()

# COMMAND ----------


