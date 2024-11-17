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
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py',
    )
    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="us-west1",
    pipeline_name="ETL-pipeline",
    instance_name="datafusion-dev",
    task_id="start_datafusion_pipeline",
    )

    run_script_task >> start_pipeline #dependencies