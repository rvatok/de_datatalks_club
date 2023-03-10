import io
import os
import requests
# import pyarrow
from google.cloud import storage
from pathlib import Path

"""
Pre-reqs: 
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""
os.environ["GCLOUD_PROJECT"] = "aerobic-canto-376317"

# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
BUCKET = "dtc_data_lake_aerobic-canto-376317"


def write_local(url: str, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    path = Path(f"{dataset_file}")
    with open(dataset_file, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
    return path


def upload_to_gcs(bucket, object_name, local_file):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name 
        file_name = service + '_tripdata_' + year + '-' + month + '.csv.gz'

        # download it using requests via a pandas df
        request_url = init_url + service + '/' + file_name
        print(f"Downloading file {request_url}")

        # upload it to gcs 
        upload_path = write_local(request_url, file_name)
        upload_to_gcs(BUCKET, f"{service}/{year}/{file_name}", file_name)
        print(f"The file was uploaded to GCS: {service}/{file_name}")

web_to_gcs('2019', 'fhv')
web_to_gcs('2020', 'fhv')
web_to_gcs('2019', 'green')
web_to_gcs('2020', 'green')
web_to_gcs('2019', 'yellow')
web_to_gcs('2020', 'yellow')