from google.cloud import bigquery
from google.cloud import storage
from google.api_core.exceptions import Conflict,NotFound
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/talha/OneDrive/Desktop/GCP/skilful-alpha-441902-r7-4b7913ba93c5.json'

def upload_gcs_to_bigquery(bucket_name, gcs_file_path, dataset_id, table_id, project_id):
    """
    Uploads a file from Google Cloud Storage to BigQuery.

    Args:
    - bucket_name: GCS bucket name
    - gcs_file_path: Path to the file in the GCS bucket (e.g., 'folder/data.csv')
    - dataset_id: BigQuery dataset name
    - table_id: BigQuery table name
    - project_id: Google Cloud project ID
    """

    # Initialize BigQuery client
    bigquery_client = bigquery.Client()

    # Set the URI for the file in GCS (gs://bucket_name/gcs_file_path)
    gcs_uri = f"gs://{bucket_name}/{gcs_file_path}"

    dataset_ref = bigquery_client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)

    # Optionally, you can set properties on the dataset (e.g., location, description)
    dataset.description = "This is a sample dataset created using Python."
    dataset.location = "US"  # You can change to another region if needed

    try:
        # Create the dataset
        dataset = bigquery_client.create_dataset(dataset)  # API request
        print(f"Dataset {dataset_id} created successfully in project {project_id}.")
    except Conflict:
        # If the dataset already exists, print a message
        print(f"Dataset {dataset_id} already exists in project {project_id}.")
    
    table_ref = dataset_ref.table(table_id)

    # Define the destination table reference

    # Define the configuration for loading the data into BigQuery
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,  # Assuming CSV format, adjust if needed
        skip_leading_rows=1,  # Skip the header row
        autodetect=True,  # Automatically detect schema (optional)
    )

    try:
        load_job = bigquery_client.load_table_from_uri(
            gcs_uri, table_ref, job_config=job_config
        )
        print(f"Starting job {load_job.job_id}...")

        # Wait for the job to complete
        load_job.result()

        # Print the result
        print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
    except NotFound:
        print(f"Dataset {dataset_id} or table {table_id} does not exist.")
    except Exception as e:
        print(f"Error during the load job: {e}")
# Example Usage

if __name__ == "__main__":
    # Replace with your details
    bucket_name = "demo_bucket786543"
    gcs_destination_path = "folder/dummy_employees.csv" 
    dataset_id = "dataset_1"  # BigQuery dataset name
    table_id = "table_1"      # BigQuery table name
    project_id = "your-gcp-project-id"    # GCP Project ID

    # Upload data from GCS to BigQuery
    upload_gcs_to_bigquery(bucket_name, gcs_destination_path, dataset_id, table_id, project_id)