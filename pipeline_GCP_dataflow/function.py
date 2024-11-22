from googleapiclient.discovery import build
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'skilful-alpha-441902-r7-4b7913ba93c5.json'
def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "skilful-alpha-441902-r7"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://tal-cricket-ranking-data/udf.js",
        "JSONPath": "gs://tal-cricket-ranking-data/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "skilful-alpha-441902-r7.testdb1.testtable1",
        "inputFilePattern": "gs://tal-cricket-ranking-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://tal-cricket-ranking-data/temp",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)