import boto3
import sys


#BUCKET_NAME = "em-py-guardians"
#FILE_NAME  = "batch-18.csv"



access_key = 'AKIA4QK6X6VEBLI3CVOL'
secret_key = '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'
region = "us-east-1"
    # Create an S3 session using the access keys and region
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# Create an S3 client using the session
s3_client = session.client('s3')

def s3_down(FILE_NAME, BUCKET_NAME):
    LOCAL_FILE_PATH = f'/home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/CSV_s3/{FILE_NAME}'  # The path where you want to save the downloaded file locally
    # Download the file from S3
    s3_client.download_file(BUCKET_NAME, FILE_NAME, LOCAL_FILE_PATH)
    # s3_client.download_file(f"{BUCKET_NAME}, {OBJECT_KEY}, {LOCAL_FILE_PATH}")

    print(f"File downloaded successfully to {LOCAL_FILE_PATH}")

def move_file_to_trash(BUCKET_NAME, FILE_NAME):
    source = {
        'Bucket': BUCKET_NAME,
        'Key': FILE_NAME
    }
    destination = f"trash/{FILE_NAME}"

    try:
        # Copy the object to the "trash/" prefix
        s3_client.copy_object(CopySource=source, Bucket=BUCKET_NAME, Key=destination)

        # Delete the original object from the root folder
        s3_client.delete_object(Bucket=BUCKET_NAME, Key=FILE_NAME)

        print(f"File '{FILE_NAME}' moved to 'trash/' prefix in bucket '{BUCKET_NAME}'")
    except s3_client.exceptions.ClientError as e:
        print("Error:", e)



#s3_down(FILE_NAME, BUCKET_NAME)
#move_file_to_trash(BUCKET_NAME, FILE_NAME)
