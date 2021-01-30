import pulumi
from pulumi_aws import s3

# 기존 코드에서 웹사이트 속성을 추가한다.
bucket = s3.Bucket('my-bucket',
    website=s3.BucketWebsiteArgs(
        index_document="index.html",
    ))

# acl='public-read'
# 어떤 유저든 사이트에 접속해 index 파일에 접근할 수 있도록 한다.
# content_type='text/html'
# 파일의 타입이 html임을 명시한다.
bucketObject = s3.BucketObject(
    'index.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket,
    content=open('site/index.html').read(),
)

# 유저들이 접근할 수 있는 url 엔드포인트 export
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
