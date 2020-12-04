from flask_restful import Resource, Api, reqparse, abort, marshal, fields, request
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from google.cloud import storage

from data.image import imageFields
from data.error import errorFields

class ImageUpload(Resource):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    BUCKET = 'david-gcloud-bucket'
    FILE_PATH = 'images/' 

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "file", 
            type=FileStorage, 
            required=True, 
            help="You must provide a file", 
            location="files"
        )

    def post(self):
        args = self.reqparse.parse_args()
        file = args['file']

        if file.filename == '':
            return 'The file must contain a name', 400
        if file and self.allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            client = storage.Client()
            bucket = client.get_bucket(self.BUCKET)
            blob = bucket.blob(self.FILE_PATH+file.filename)
            blob.upload_from_string(file.read(), content_type=file.content_type)
            # print(blob.download_as_string())

            image = {
                "filename": blob.name,
                "size": blob.size,
                "type": blob.content_type,
                "path": '',
                "publicUrl": blob.public_url,
            }
            return marshal(image, imageFields), 201

        # blob2 = bucket.blob('remote/path/storage.txt')
        # blob2.upload_from_filename(filename='/local/path.txt')

        # # Get the bucket that the file will be uploaded to.
        # bucket = gcs.get_bucket('')

        # # Create a new blob and upload the file's content.
        # blob = bucket.blob(uploaded_file.filename)

        # blob.upload_from_string(
        #     uploaded_file.read(),
        #     content_type=uploaded_file.content_type
        # )

    def get(self):
        # storage_client = storage.Client()
        # buckets = list(storage_client.list_buckets())
        # return buckets
        return True

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS