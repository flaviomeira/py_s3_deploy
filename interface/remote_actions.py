from typing import Iterable


class S3Interface:
    def __init__(self, s3):
        self.s3 = s3

    @staticmethod
    def get_files_to_delete(local_files: Iterable, remote_files: Iterable) -> list:
        """
        Compare the local and remote files to check if files were removed.
        Args:
            list local_files:
                filenames from the user's filesystem.

            list remote_files:
                filenames from the remote server

        Returns:
            list with the files that should be deleted from the remote server
        """
        if '__iter__' not in dir(local_files) or '__iter__' not in dir(remote_files):
            return []
        return [x for x in remote_files if x not in local_files]

    def get_remote_files(self, bucket_name: str) -> list:
        """
        Gets the bucket's file names.
        Args:
            str bucket_name:
                name of the bucket to be checked.

        Returns:
            list with the file names.
        """
        s3_objects = self.s3.list_objects(Bucket=bucket_name)
        return s3_objects['Contents']

    def delete_aws_files(self, files_to_delete: dict, bucket_name: str) -> list:
        """
        Deletes files from the bucket.
        Args:
            list files_to_delete:
                list of dicts with the name of files to be deleted in the following format:
                    [{'Key': 'file1'},
                     {'Key': 'file2'}
                     {'Key': 'filex'}]
            str bucket_name:
                name of the bucket.
        Returns:
            list of the deleted files.
        """
        deleted_files = self.s3.delete_objects(Bucket=bucket_name,
                                               Delete=files_to_delete)
        return deleted_files['Deleted']

    def _upload_file(self, file_: str):
        """
        TODO: implement function
        """
        raise NotImplementedError

    def upload_files(self, files: list):
        for file_ in files:
            self._upload_file(file_)
