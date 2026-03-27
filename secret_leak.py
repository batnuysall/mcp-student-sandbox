# filepath: [secret_leak.py](http://_vscodecontentref_/1)
# ...existing code...
import os

def connect():
    aws_secret = os.environ.get("AWS_SECRET_KEY")
    if not aws_secret:
        raise RuntimeError("Missing AWS_SECRET_KEY environment variable")
    # Do not print secrets. Use aws_secret to initialize clients securely.
    # e.g. boto3.client('s3', aws_access_key_id=..., aws_secret_access_key=aws_secret)
# ...existing code...
