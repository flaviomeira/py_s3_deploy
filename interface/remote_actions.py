class S3Interface:
    def __init__(self, s3):
        self.s3 = s3

    @staticmethod
    def get_files_to_delete(local_files, remote_files) -> list:
        if not '__iter__' in dir(local_files) or not '__iter__' in dir(remote_files):
            return []
        return [x for x in remote_files if x not in local_files]


    def get_remote_files(self, bucket_name: str) -> list:
        s3_objects = self.s3.list_objects(Bucket=bucket_name)
        return s3_objects['Contents']


    def delete_aws_files(self, files_to_delete: dict, bucket_name: str) -> list:
        deleted_files = self.s3.delete_objects(Bucket=bucket_name, 
                                               Delete=files_to_delete)
        return deleted_files['Deleted']