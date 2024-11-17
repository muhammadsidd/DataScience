import os
from google.cloud import storage,bigquery
from google.api_core.exceptions import Conflict,NotFound
from faker import Faker
import random
import csv

# Initialize Faker instance
fake = Faker()
#for service account use below code 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/airflow/gcs/dags/scripts/skilful-alpha-441902-r7-4b7913ba93c5.json'
#for main account use gloud auth application-default login on the shell

# Function to generate a dummy employee
def generate_employee():
    return {
        "employee_id": fake.uuid4(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job_title": fake.job().replace(',','-'),
        "department": random.choice(['HR', 'Finance', 'Engineering', 'Marketing', 'Sales', 'IT']),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.state(),
        "date_of_birth": fake.date_of_birth(minimum_age=22, maximum_age=65).strftime('%Y-%m-%d'),
        "hire_date": fake.date_this_decade().strftime('%Y-%m-%d'),
        "salary": random.randint(50000, 150000),  # Example salary range
        "is_active": random.choice([True, False]),
        "password": fake.password()
    }

# Function to generate a list of employees
def generate_employees(num_employees):
    employees = []
    for _ in range(num_employees):
        employees.append(generate_employee())
    return employees

# Save the generated data to a local CSV file
def save_to_csv(employees, filename="employees.csv"):
    keys = employees[0].keys()
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(employees)

# Function to upload the CSV file to a GCS bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # Instantiate a GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a new blob (file object) in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example: Generate 10 dummy employees and save to CSV

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
    bigquery_client = bigquery.Client(project=project_id)

    # Set the URI for the file in GCS (gs://bucket_name/gcs_file_path)
    gcs_uri = f"gs://{bucket_name}/{gcs_file_path}"

    # Define the destination table reference
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)

    # Define the configuration for loading the data into BigQuery
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,  # Assuming CSV format, adjust if needed
        skip_leading_rows=1,  # Skip the header row
        autodetect=True,  # Automatically detect schema (optional)
    )

    # Start the load job
    load_job = bigquery_client.load_table_from_uri(
        gcs_uri, table_ref, job_config=job_config
    )

    print(f"Starting job {load_job.job_id}...")

    # Wait for the job to complete
    load_job.result()

    print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")

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
    num_employees = 100
    employees = generate_employees(num_employees)

    # Save to a local CSV file
    local_filename = "dummy_employees.csv"
    save_to_csv(employees, local_filename)

    # Define your GCS bucket name and the desired destination file path
    bucket_name = "demo_bucket786543"
    gcs_destination_path = "folder/dummy_employees.csv"  # e.g., "uploads/dummy_employees.csv"

    # Upload the file to GCS
    upload_to_gcs(bucket_name, local_filename, gcs_destination_path)

    # Optionally, you can remove the local file after upload
    # os.remove(local_filename)
    print(f"Local file {local_filename} deleted after upload.")
    # Replace with your details
    bucket_name = "your-gcs-bucket-name"
    gcs_file_path = "path/to/your/file.csv"  # GCS file path (e.g., "uploads/dummy_employees.csv")
    # dataset_id = "your_bigquery_dataset"  # BigQuery dataset name
    # table_id = "your_bigquery_table"      # BigQuery table name
    # project_id = "your-gcp-project-id"    # GCP Project ID
    # upload_gcs_to_bigquery(bucket_name, gcs_file_path, dataset_id, table_id, project_id)