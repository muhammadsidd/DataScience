from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/airflow/gcs/dags/scripts/skilful-alpha-441902-r7-4b7913ba93c5.json'
#add this to airflow admin connections ^ under path credentials

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['vishal.bulbule@techtrapture.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract_and_push_gcs.py',
    )
    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="us-west1",
    pipeline_name="ETL-pipeline",
    instance_name="datafusion-dev",
    task_id="start_datafusion_pipeline",
    )

    run_script_task >> start_pipeline #dependencies

# from airflow import DAG
# from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
# from airflow.utils.dates import days_ago
# from datetime import timedelta

# # Define your BigQuery project, source, and destination datasets
# PROJECT_ID = 'your-project-id'
# SOURCE_DATASET = 'your-source-dataset'
# TARGET_DATASET = 'your-target-dataset'

# # Define the DAG's default_args
# default_args = {
#     'owner': 'airflow',
#     'start_date': days_ago(1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# # Define the DAG
# with DAG(
#     'bigquery_data_transform_and_load',
#     default_args=default_args,
#     description='Extract, transform (merge columns), and load data in BigQuery',
#     schedule_interval='@daily',  # Set the schedule to your needs
#     catchup=False,
# ) as dag:

#     # SQL query to extract and transform the data (merge two columns)
#     transform_sql = f"""
#     SELECT 
#         column1,
#         column2,
#         CONCAT(column1, ' ', column2) AS merged_column  -- Merging column1 and column2
#     FROM `{PROJECT_ID}.{SOURCE_DATASET}.source_table`
#     """

#     # SQL query to load the transformed data into the target dataset
#     load_sql = f"""
#     CREATE OR REPLACE TABLE `{PROJECT_ID}.{TARGET_DATASET}.target_table` AS
#     {transform_sql}
#     """

#     # Task 1: Extract and transform data (using BigQueryInsertJobOperator)
#     transform_data = BigQueryInsertJobOperator(
#         task_id='transform_data',
#         sql=transform_sql,
#         destination_dataset_table=f"{PROJECT_ID}.{TARGET_DATASET}.target_table",  # Where to load the data
#         project_id=PROJECT_ID,
#         create_disposition='CREATE_IF_NEEDED',  # Create the table if it doesn't exist
#         write_disposition='WRITE_TRUNCATE',  # Overwrite the table if it exists
#         use_legacy_sql=False,
#     )

#     # Task 2: Load transformed data into the target dataset (using BigQueryInsertJobOperator)
#     load_data = BigQueryInsertJobOperator(
#         task_id='load_transformed_data',
#         sql=load_sql,
#         destination_dataset_table=f"{PROJECT_ID}.{TARGET_DATASET}.target_table",  # Target table
#         project_id=PROJECT_ID,
#         create_disposition='CREATE_IF_NEEDED',
#         write_disposition='WRITE_TRUNCATE',
#         use_legacy_sql=False,
#     )

#     # Define the task dependencies
#     transform_data >> load_data  # Ensure data is transformed before loading