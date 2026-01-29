import boto3
from PIL import Image
import io
import urllib.parse

s3 = boto3.client('s3')
DEST_BUCKET = "image-resized-bucket-thumbnail"

def lambda_handler(event, context):
    for record in event['Records']:
        src_bucket = record['s3']['bucket']['name']
        src_key = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        response = s3.get_object(
            Bucket=src_bucket,
            Key=src_key
        )

        img = Image.open(response['Body'])
        img.thumbnail((300, 300))

        buffer = io.BytesIO()
        img.save(buffer, format=img.format)
        buffer.seek(0)

        s3.put_object(
            Bucket=DEST_BUCKET,
            Key=f"thumb-{src_key}",
            Body=buffer,
            ContentType=response['ContentType']
        )

    return {"status": "success"}
