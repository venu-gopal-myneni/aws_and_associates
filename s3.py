"""
When you call boto3.Session() without arguments, it looks for credentials using the following order:

📚 Boto3 Credential Resolution Chain
Environment variables
(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, etc.)

Shared credential file (~/.aws/credentials)

Uses the [default] profile if no profile is specified

Config file (~/.aws/config)

For region and profile info

IAM Role for Amazon EC2

If running on an EC2 instance or container with a role
"""

import boto3
import json

# Let's use Amazon S3
# Create an S3 client (optionally using a profile)
session = boto3.Session(profile_name="default")  # omit if using default
s3 = session.client("s3")
# List buckets
response = s3.list_buckets()

# Print bucket names
for bucket in response["Buckets"]:
    print(bucket["Name"])

bucket_name = "<bucket-name>"

try:
    response = s3.get_bucket_policy(Bucket=bucket_name)
    policy = response["Policy"]
    # Pretty print the policy JSON
    print(json.dumps(json.loads(policy), indent=4))
except s3.exceptions.from_code("NoSuchBucketPolicy"):
    print(f"No bucket policy is attached to {bucket_name}")
except Exception as e:
    print(f"Error: {e}")
