import os

AWS_ACCESS_KEY_ID = 'GQ753OBSBFSUB3WYRBJG' 
AWS_SECRET_ACCESS_KEY = '6eKj3tFY8NcAhBrL9SXFWYRac74LkjpD1+/lSCLwgNk' 
AWS_STORAGE_BUCKET_NAME="econometricdatasolutions"
AWS_S3_ENDPOINT_URL='https://sfo3.digitaloceanspaces.com'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


AWS_LOCATION="https://econometricdatasolutions.sfo3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "secondDashboard.cdn.backends.MediaRootS3Boto3Storage"

STATICFILES_STORAGE = "secondDashboard.cdn.backends.StaticRootS3BotoStorage"
