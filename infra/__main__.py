import json
import mimetypes
from pathlib import Path

from pulumi import export, FileAsset
from pulumi_aws import s3


web_bucket = s3.Bucket(
    's3-website.linhart.tech',
    website=s3.BucketWebsiteArgs(
        index_document='index.html'
    )
)

content_dir = Path('../www')
for path in content_dir.glob('**/*'):
    if not path.is_file():
        continue
    filename = str(path.relative_to(content_dir))
    filepath = str(path)
    content_type, content_encoding = mimetypes.guess_type(filepath)
    obj = s3.BucketObject(
        filename,
        bucket=web_bucket.id,
        source=FileAsset(filepath),
        content_type=content_type,
        content_encoding=content_encoding
    )

def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Principal': '*',
            'Action': [
                's3:GetObject'
            ],
            'Resource': [
                f'arn:aws:s3:::{bucket_name}/*'
            ]
        }]
    })

bucket_name = web_bucket.id
bucket_policy = s3.BucketPolicy(
    's3-website-bucket-policy',
    bucket=bucket_name,
    policy=bucket_name.apply(public_read_policy_for_bucket)
)

export('bucket_name', web_bucket.id)
export('website_url', web_bucket.website_endpoint)
