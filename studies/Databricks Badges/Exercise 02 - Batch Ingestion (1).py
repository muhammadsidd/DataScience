# Databricks notebook source
# %md-sandbox
#
# <div style="text-align: center; line-height: 0; padding-top: 9px;">
#   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# </div>

# COMMAND ----------

# %md
# # Exercise #2 - Batch Ingestion
#
# In this exercise you will be ingesting three batches of orders, one for 2017, 2018 and 2019.
#
# As each batch is ingested, we are going to append it to a new Delta table, unifying all the datasets into one single dataset.
#
# Each year, different individuals and different standards were used resulting in datasets that vary slightly:
# * In 2017 the backup was written as fixed-width text files
# * In 2018 the backup was written a tab-separated text files
# * In 2019 the backup was written as a "standard" comma-separted text files but the format of the column names was changed
#
# Our only goal here is to unify all the datasets while tracking the source of each record (ingested file name and ingested timestamp) should additional problems arise.
#
# Because we are only concerned with ingestion at this stage, the majority of the columns will be ingested as simple strings and in future exercises we will address this issue (and others) with various transformations.
#
# As you progress, several "reality checks" will be provided to you help ensure that you are on track - simply run the corresponding command after implementing the corresponding solution.
#
# This exercise is broken up into 3 steps:
# * Exercise 2.A - Ingest Fixed-Width File
# * Exercise 2.B - Ingest Tab-Separated File
# * Exercise 2.C - Ingest Comma-Separated File

# COMMAND ----------

# %md <h2><img src="https://files.training.databricks.com/images/105/logo_spark_tiny.png"> Setup Exercise #2</h2>
#
# To get started, we first need to configure your Registration ID and then run the setup notebook.

# COMMAND ----------

# %md ### Setup - Registration ID
#
# In the next commmand, please update the variable **`registration_id`** with the Registration ID you received when you signed up for this project.
#
# For more information, see [Registration ID]($./Registration ID)

# COMMAND ----------

# TODO
registration_id = "3419578"

# COMMAND ----------

# %md ### Setup - Run the exercise setup
#
# Run the following cell to setup this exercise, declaring exercise-specific variables and functions.

# COMMAND ----------

# %run ./_includes/Setup-Exercise-02

# COMMAND ----------

# %md Run the following cell to preview a list of the files you will be processing in this exercise.

# COMMAND ----------

# files = dbutils.fs.ls(f"{working_dir}/raw/orders/batch") # List all the files
# display(files)                                           # Display the list of files

# COMMAND ----------

# %md <h2><img src="https://files.training.databricks.com/images/105/logo_spark_tiny.png"> Exercise #2.A - Ingest Fixed-Width File</h2>
#
# **In this step you will need to:**
# 1. Use the variable **`batch_2017_path`**, and **`dbutils.fs.head`** to investigate the 2017 batch file, if needed.
# 2. Configure a **`DataFrameReader`** to ingest the text file identified by **`batch_2017_path`** - this should provide one record per line, with a single column named **`value`**
# 3. Using the information in **`fixed_width_column_defs`** (or the dictionary itself) use the **`value`** column to extract each new column of the appropriate length.<br/>
#   * The dictionary's key is the column name
#   * The first element in the dictionary's value is the starting position of that column's data
#   * The second element in the dictionary's value is the length of that column's data
# 4. Once you are done with the **`value`** column, remove it.
# 5. For each new column created in step #3, remove any leading whitespace
#   * The introduction of \[leading\] white space should be expected when extracting fixed-width values out of the **`value`** column.
# 6. For each new column created in step #3, replace all empty strings with **`null`**.
#   * After trimming white space, any column for which a value was not specified in the original dataset should result in an empty string.
# 7. Add a new column, **`ingest_file_name`**, which is the name of the file from which the data was read from.
#   * This should not be hard coded.
#   * For the proper function, see the <a href="https://spark.apache.org/docs/latest/api/python/index.html" target="_blank">pyspark.sql.functions</a> module
# 8. Add a new column, **`ingested_at`**, which is a timestamp of when the data was ingested as a DataFrame.
#   * This should not be hard coded.
#   * For the proper function, see the <a href="https://spark.apache.org/docs/latest/api/python/index.html" target="_blank">pyspark.sql.functions</a> module
# 9. Write the corresponding **`DataFrame`** in the "delta" format to the location specified by **`batch_target_path`**
#
# **Special Notes:**
# * It is possible to use the dictionary **`fixed_width_column_defs`** and programatically extract <br/>
#   each column but, it is also perfectly OK to hard code this step and extract one column at a time.
# * The **`SparkSession`** is already provided to you as an instance of **`spark`**.
# * The classes/methods that you will need for this exercise include:
#   * **`pyspark.sql.DataFrameReader`** to ingest data
#   * **`pyspark.sql.DataFrameWriter`** to ingest data
#   * **`pyspark.sql.Column`** to transform data
#   * Various functions from the **`pyspark.sql.functions`** module
#   * Various transformations and actions from **`pyspark.sql.DataFrame`**
# * The following methods can be used to investigate and manipulate the Databricks File System (DBFS)
#   * **`dbutils.fs.ls(..)`** for listing files
#   * **`dbutils.fs.rm(..)`** for removing files
#   * **`dbutils.fs.head(..)`** to view the first N bytes of a file
#
# **Additional Requirements:**
# * The unified batch dataset must be written to disk in the "delta" format
# * The schema for the unified batch dataset must be:
#   * **`submitted_at`**:**`string`**
#   * **`order_id`**:**`string`**
#   * **`customer_id`**:**`string`**
#   * **`sales_rep_id`**:**`string`**
#   * **`sales_rep_ssn`**:**`string`**
#   * **`sales_rep_first_name`**:**`string`**
#   * **`sales_rep_last_name`**:**`string`**
#   * **`sales_rep_address`**:**`string`**
#   * **`sales_rep_city`**:**`string`**
#   * **`sales_rep_state`**:**`string`**
#   * **`sales_rep_zip`**:**`string`**
#   * **`shipping_address_attention`**:**`string`**
#   * **`shipping_address_address`**:**`string`**
#   * **`shipping_address_city`**:**`string`**
#   * **`shipping_address_state`**:**`string`**
#   * **`shipping_address_zip`**:**`string`**
#   * **`product_id`**:**`string`**
#   * **`product_quantity`**:**`string`**
#   * **`product_sold_price`**:**`string`**
#   * **`ingest_file_name`**:**`string`**
#   * **`ingested_at`**:**`timestamp`**

# COMMAND ----------

# %md ### Fixed-Width Meta Data
#
# The following dictionary is provided for reference and/or implementation<br/>
# (depending on which strategy you choose to employ).
#
# Run the following cell to instantiate it.

# COMMAND ----------

fixed_width_column_defs = {
  "submitted_at": (1, 15),
  "order_id": (16, 40),
  "customer_id": (56, 40),
  "sales_rep_id": (96, 40),
  "sales_rep_ssn": (136, 15),
  "sales_rep_first_name": (151, 15),
  "sales_rep_last_name": (166, 15),
  "sales_rep_address": (181, 40),
  "sales_rep_city": (221, 20),
  "sales_rep_state": (241, 2),
  "sales_rep_zip": (243, 5),
  "shipping_address_attention": (248, 30),
  "shipping_address_address": (278, 40),
  "shipping_address_city": (318, 20),
  "shipping_address_state": (338, 2),
  "shipping_address_zip": (340, 5),
  "product_id": (345, 40),
  "product_quantity": (385, 5),
  "product_sold_price": (390, 20)
}

# COMMAND ----------

# %md ### Implement Exercise #2.A
#
# Implement your solution in the following cell:

# COMMAND ----------

# TODO
# Use this cell to complete your solution
from pyspark.sql.functions import col, lit, sum, avg, max, mean, count, udf, substring
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType
from pyspark import SparkConf, SparkContext
from pyspark.sql import functions as F
from pyspark.sql.functions import col,when
from  pyspark.sql.functions import input_file_name



conf = SparkConf().setAppName("Read File")
spark = SparkContext.getOrCreate(conf=conf)
DataFrameReader = spark.read.option("header",True).text(batch_2017_path)
DataFrameReader.show()
DataFrameReader = DataFrameReader.select("value",*[F.substring("value",*v).alias(k) for k,v in fixed_width_column_defs.items()])

DataFrameReader.show()

DataFrameReader= DataFrameReader.drop("value")
DataFrameReader.show()

for colname in DataFrameReader.columns:
    DataFrameReader = DataFrameReader.withColumn(colname,F.ltrim(colname))
DataFrameReader.show()


DataFrameReader=DataFrameReader.select([when(col(c)=="",None).otherwise(col(c)).alias(c) for c in DataFrameReader.columns])
DataFrameReader.show()

DataFrameReader= DataFrameReader.withColumn("ingest_file_name", input_file_name())
DataFrameReader.show()
df = DataFrameReader.withColumn("ingested_at", input_file_name())

df = DataFrameReader.withColumn("ingested_at", F.current_timestamp())
df.show()

df.write.format("delta").mode("overwrite").save(batch_target_path)

# COMMAND ----------

# %md ### Reality Check #2.A
# Run the following command to ensure that you are on track:

# COMMAND ----------

reality_check_02_a()

# COMMAND ----------

# %md <h2><img src="https://files.training.databricks.com/images/105/logo_spark_tiny.png"> Exercise #2.B - Ingest Tab-Separted File</h2>
#
# **In this step you will need to:**
# 1. Use the variable **`batch_2018_path`**, and **`dbutils.fs.head`** to investigate the 2018 batch file, if needed.
# 2. Configure a **`DataFrameReader`** to ingest the tab-separated file identified by **`batch_2018_path`**
# 3. Add a new column, **`ingest_file_name`**, which is the name of the file from which the data was read from - note this should not be hard coded.
# 4. Add a new column, **`ingested_at`**, which is a timestamp of when the data was ingested as a DataFrame - note this should not be hard coded.
# 5. **Append** the corresponding **`DataFrame`** to the previously created datasets specified by **`batch_target_path`**
#
# **Additional Requirements**
# * Any **"null"** strings in the CSV file should be replaced with the SQL value **null**

# COMMAND ----------

# %md ### Implement Exercise #2.b
#
# Implement your solution in the following cell:

# COMMAND ----------

# TODO
# Use this cell to complete your solution
df = spark.read.option("header",True).option("delimiter","\t").csv(batch_2018_path)
df = df.withColumn("ingest_file_name",input_file_name())
df.show()
df =  df.withColumn("ingested_at", F.current_timestamp())
df.show()
df=df.select([when(col(c)=="null",None).otherwise(col(c)).alias(c) for c in df.columns])
df.write.format("delta").mode("append").save(batch_target_path)
    

# %md <h2><img src="https://files.training.databricks.com/images/105/logo_spark_tiny.png"> Exercise #2.C - Ingest Comma-Separted File</h2>
#
# **In this step you will need to:**
# 1. Use the variable **`batch_2019_path`**, and **`dbutils.fs.head`** to investigate the 2019 batch file, if needed.
# 2. Configure a **`DataFrameReader`** to ingest the comma-separated file identified by **`batch_2019_path`**
# 3. Add a new column, **`ingest_file_name`**, which is the name of the file from which the data was read from - note this should not be hard coded.
# 4. Add a new column, **`ingested_at`**, which is a timestamp of when the data was ingested as a DataFrame - note this should not be hard coded.
# 5. **Append** the corresponding **`DataFrame`** to the previously created dataset specified by **`batch_target_path`**<br/>
#    Note: The column names in this dataset must be updated to conform to the schema defined for Exercise #2.A - there are several strategies for this:
#    * Provide a schema that alters the names upon ingestion
#    * Manually rename one column at a time
#    * Use **`fixed_width_column_defs`** programaticly rename one column at a time
#    * Use transformations found in the **`DataFrame`** class to rename all columns in one operation
#
# **Additional Requirements**
# * Any **"null"** strings in the CSV file should be replaced with the SQL value **null**<br/>

# COMMAND ----------

# %md ### Implement Exercise #2.C
#
# Implement your solution in the following cell:

# COMMAND ----------

# TODO
# Use this cell to complete your solution
df = spark.read.option("header",True).csv('batch_2019_path')

l1 = list(fixed_width_column_defs)
l1[1]

for c in range(len(df.columns)):
    df = df.withColumnRenamed(df.columns[c],l1[c])
df.printSchema()

df = df.withColumn("ingest_file_name",input_file_name())
df.show()
df =  df.withColumn("ingested_at", F.current_timestamp())
df.show()
df=df.select([when(col(c)=="null",None).otherwise(col(c)).alias(c) for c in df.columns])
df.write.format("delta").mode("append").save('batch_target_path')