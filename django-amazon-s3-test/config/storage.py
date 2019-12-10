from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage


# ----------------- Static ----------------- #
class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION
    default_acl = 'public-read'


# ----------------- Media ----------------- #
class MediaStorage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
    file_overwrite = False


class PublicMediaStorage(MediaStorage):
    default_acl = 'public-read'


class PrivateMediaStorage(MediaStorage):
    default_acl = 'private'
