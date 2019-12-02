 # -*- coding:utf-8 -*-
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('my_first_test')
blob = bucket.blob('cat.jpg')
# blob = bucket.blob('バケット内のパス/ファイル名') でも可能
blob.upload_from_filename('/Users/kambayt01/Desktop/cat.jpg')