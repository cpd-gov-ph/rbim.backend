import boto3
import config
import calendar
import constants
from datetime import datetime


def check_file_extension(images):
    extention_validation = True
    for img in images:
        extention = img.name.split('.')[-1]
        if extention not in constants.OCR_FILE_EXTENSION:
            extention_validation = False
            break
    return extention_validation


def upload_images_to_s3(images, survey_id):
    images_ = []
    media_path = 'media/'
    date = datetime.utcnow()
    utc_timestamp = calendar.timegm(date.utctimetuple())
    bucket_name = config.AWS_STORAGE_BUCKET_NAME
    s3 = boto3.resource('s3',
                        aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)
    for img in images:
        image_name = f"{str(survey_id).split('-')[-1]}_{utc_timestamp}_{img.name.replace(' ', '_')}"
        s3.Object(bucket_name, f'media/{image_name}').put(Body=img)
        images_.append(f"{config.AWS_S3_HOST}" + media_path + f"{image_name}")
    return images_
