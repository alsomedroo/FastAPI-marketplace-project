import boto3
import uuid

from app.core.config import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
    AWS_BUCKET,
    AWS_REGION,
)

# Optional safety check (VERY useful)
if not all([AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET]):
    raise RuntimeError("AWS S3 environment variables are missing")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

def upload_image(file):
    key = f"products/{uuid.uuid4()}.jpg"
    s3.upload_fileobj(file, AWS_BUCKET, key)
    return f"https://{AWS_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"
