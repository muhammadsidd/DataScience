import requests
import csv
from google.cloud import storage,bigquery
from google.api_core.exceptions import Conflict,NotFound
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'skilful-alpha-441902-r7-4b7913ba93c5.json'

client = storage.Client()
client_bq = bigquery.Client()

def create_dataset(dataset_name):
    """Create a BigQuery dataset if it doesn't exist."""
    try:
        # Check if the dataset exists
        dataset = client_bq.get_dataset(dataset_name)  # Will raise an exception if not found
        print(f"Dataset '{dataset_name}' already exists.")
        return dataset
    except NotFound:
        # Create the dataset if it doesn't exist
        dataset = bigquery.Dataset(dataset_name)
        dataset.location = "US"  # Set location (optional)
        dataset = client_bq.create_dataset(dataset)  # Create the dataset
        print(f"Dataset '{dataset_name}' created successfully.")
        return dataset

def create_or_append_table(dataset_name, table_name, data_frame):
    """Create a table if it doesn't exist or append data if the table exists."""
    table_id = f"{client_bq.project}.{dataset_name}.{table_name}"
    
    try:
        # Check if the table exists
        table = client_bq.get_table(table_id)
        print(f"Table '{table_name}' already exists. Appending data.")
        
        # If the table exists, append the data
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND",  # This appends the data to the existing table
            autodetect=True,  # Automatically detects schema from DataFrame
        )
        
        # Load the data from DataFrame to BigQuery table
        load_job = client_bq.load_table_from_dataframe(data_frame, table_id, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        print(f"Data appended to table '{table_name}'.")
        
    except NotFound:
        # If the table doesn't exist, create a new table and load the data
        print(f"Table '{table_name}' does not exist. Creating and loading data.")
        
        # Define table schema based on DataFrame (automatically detected)
        job_config = bigquery.LoadJobConfig(
            autodetect=True,
            write_disposition="WRITE_TRUNCATE",  # This creates a new table or replaces an existing one
        )
        # load_job = client_bq.create_table(dataset_name + '.' +table_name) ##create empty table
        # Load the data from DataFrame to BigQuery table
        load_job = client_bq.load_table_from_dataframe(data_frame, table_id, job_config=job_config)
        load_job.result()  # Wait for the job to complete
        print(f"Table '{table_name}' created and data loaded.")

def create_bucket(bucket_name):
    """Creates a new bucket if it does not exist."""
    try:
        # Check if the bucket already exists
        bucket = client.get_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
        return bucket
    except Exception as e:
        if "Not Found" in str(e):
            # Create the bucket if it doesn't exist
            bucket = client.create_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")
            return bucket
        else:
            # If any other error occurs, print it
            print(f"Error while accessing the bucket: {e}")
            return None

def upload_csv_to_bucket(bucket_name, local_file_path, blob_name):
    """Uploads a CSV file to the GCP bucket."""
    try:
        # Create or get the bucket
        bucket = create_bucket(bucket_name)
        
        if bucket is None:
            print(f"Failed to create or find the bucket: {bucket_name}")
            return
        
        # Create a blob object (GCS equivalent of a file)
        blob = bucket.blob(blob_name)
        
        # Upload the local file to the GCS bucket
        blob.upload_from_filename(local_file_path)
        print(f"File '{local_file_path}' uploaded to bucket '{bucket_name}' as '{blob_name}'.")
    except Exception as e:
        print(f"An error occurred during the upload: {e}")

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"odi"}

headers = {
	"x-rapidapi-key": "8d48575b7bmshd9f62d0dd3b4216p1c6b91jsnf28606b10f93",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
# print(response.json())

if response.status_code == 200:
    data = response.json().get('rank',[])
    csv_filename = 'batsmen_ranking.csv'

    if data:
        field_name = ['rank','name','country']

        with open(csv_filename,'w',newline='',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=field_name)
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_name})
        print(f"data fetched and successfully written to '{csv_filename}'")
    # Instantiate a GCS client
        storage_client = storage.Client()
        bucket_name = 'tal-cricket-ranking-data'
        upload_csv_to_bucket (bucket_name,'batsmen_ranking.csv','cricket-stats')
        # create_dataset("skilful-alpha-441902-r7.testdb1")
        # create_or_append_table("testdb1","testtable1")
          
    else:
        print("no data available")

else:
    print("failed to fetch data", response.status_code)
