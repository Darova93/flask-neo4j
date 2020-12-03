from flask_restful import Resource, Api, reqparse, abort, marshal, fields, request
from google.cloud import storage

class ImageUpload(Resource):
    def post(self):
        # storage_client = storage.Client()
        # buckets = list(storage_client.list_buckets())
        # return buckets
        client = storage.Client()
        # https://console.cloud.google.com/storage/browser/[bucket-id]/
        bucket = client.get_bucket('david-gcloud-bucket')
        blob = bucket.blob('remote/path/to/file.txt')
        print(blob.download_as_string())
        blob.upload_from_string('New contents!')
        blob2 = bucket.blob('remote/path/storage.txt')
        blob2.upload_from_filename(filename='/local/path.txt')

        return blob.public_url

        # """Process the uploaded file and upload it to Google Cloud Storage."""
        # uploaded_file = request.files.get('file')

        # if not uploaded_file:
        #     return 'No file uploaded.', 400

        # # Create a Cloud Storage client.
        # gcs = storage.Client()

        # # Get the bucket that the file will be uploaded to.
        # bucket = gcs.get_bucket('')

        # # Create a new blob and upload the file's content.
        # blob = bucket.blob(uploaded_file.filename)

        # blob.upload_from_string(
        #     uploaded_file.read(),
        #     content_type=uploaded_file.content_type
        # )

        # # The public URL can be used to directly access the uploaded file via HTTP.
        # return blob.public_url