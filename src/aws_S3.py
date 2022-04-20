import boto
import boto.s3
import sys
import time
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJJVNU2RORRH6P5NQ'
AWS_SECRET_ACCESS_KEY = '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'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

def upload(file_path, file_name, bucket_name):

    bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

    #testfile = "/home/pi/Desktop/hhh.png"
    print 'Uploading %s to Amazon S3 bucket %s' % \
       (file_path, bucket_name)

    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()


    k = Key(bucket)
    k.key = file_name
    k.set_contents_from_filename(file_path,
        cb=percent_cb, num_cb=10)
