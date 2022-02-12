from numpy import source
from pyspark import SparkContext, SparkConf

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType


############################### STEP 1 EXTRACT DATA FROM AZURE SQL ###############################

# Configure connection and spark context
# conf = SparkConf().setAppName("FilterData")
# sc = SparkContext.getOrCreate(conf=conf)
jdbcHostname = "host_name"
jdbcPort = 1433
jdbcDatabase = "database_name"
jdbcUsername = "username"
jdbcPassword = "pass"
jdbcDriver = "driver location"
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};databaseNmae={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"
spark = SparkSession.builder.appName("Spark DF actions").getOrCreate()

# Read tables
df_product = spark.read.format("jdbc").option(
    "url", jdbcUrl).option("dbtable", "SalesLT.Products").load()
df_sales = spark.read.format("jdbc").option("url", jdbcUrl).option(
    "dbtable", "SalesLT.DslrdOrderDetail").load()

############################# STEP 2 TRANSFORMING THE DATA AS PER BUSINESS RULES #####################

# Cleaning Dimesnions - replacing null values and dropping duplicates
df_product_neat = df_product.na.fill({"Size": "M", "Weight": 100})
df_sales_neat = df_sales.dropDuplicates()

#Perform Join to merge dataframes 
df_join = df_sales_neat.join(df_product_neat, df_sales_neat.ProductID == df_product_neat.ProductID, "leftouter").select(df_sales_neat.ProductID,
                                                                                                                        df_sales_neat.UnitPrice,
                                                                                                                        df_sales_neat.LineTotal,
                                                                                                                        df_product_neat.Name,
                                                                                                                        df_product_neat.Color,
                                                                                                                        df_product_neat.Size,
                                                                                                                        df_product_neat.Weight
                                                                                                                        )
#Perform Aggregation
df_agg =  df_join.groupBy(["ProductID", "Name","Color","Weoght"]).sum("LineTotal").withColumnRenamed("sum(LineTotal)","sum_total_sales")

############################# STEP 3 LOAD DATA INTO AZURE DATA LAKE STORAGE (FOR DATABEICKS) ##########################

#Create a mountPoint for ADLS integration 
dbutils.fs.mount(source = "azure datalake storage", 
                mount_point = "mount_point_directory",
                extra_configs = "access key and other variables in json format" )

#List the files under the mount point 
dbutils.fs.ls("mount_pointdirectory")

#Write Data in parquet or csv format
df_agg.write.format("parquet").save("mount_point_directory/parquet_file_name/")
df_agg.write.format("csv").option("header","true").save("mount_point_directory/csv_file_name/")