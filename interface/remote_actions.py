import os

from interface.helper import (get_md5_recursively, file_md5, directory_files_recursively,
                              get_files_to_delete)


class S3Interface:
    def __init__(self, s3):
        self.s3 = s3

    def delete_removed_files(self, local_path: str, bucket_name: str):
        """
        Removes from the target bucket only files that are no longer in the given path.
        Args:
            str local_path:
                path to look for the files.
            str bucket_name:
                name of the bucket

        Returns:
            list of the deleted files.
        """
        remote_files = self.get_remote_file_names(bucket_name)
        local_files = directory_files_recursively(local_path)
        files_to_delete = get_files_to_delete(local_files, remote_files)
        if files_to_delete.get('Objects')
            return self.delete_aws_files(files_to_delete, bucket_name)
        else:
            return []

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
        return s3_objects.get('Contents', [])

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

    def _upload_file(self, bucket_name: str, file_: str):
        """
        Uploads a single file to the bucket.
        Args:
            str bucket_name:
                name of the bucket.
            str file_:
                file name.
        Returns:
            None
        """
        with open(file_, 'rb') as data:
            self.s3.upload_fileobj(data, bucket_name, file_)

    def upload_files(self, bucket_name: str, files: list):
        """
        Uploads a list of files to the bucket.
        Args:
            str bucket_name:
                name of the bucket.
            list files:
                list of the names of files to be uploaded.
        Returns:
            None
        """
        for file_ in files:
            self._upload_file(bucket_name, file_)

    def upload_only_different_files(self, bucket_name: str, path: str):
        """
        Uploads only files that have their names and MD5 hashes (ETag)
        different from the remote ones.
        Args:
            str bucket_name:
                name of the bucket.
            str path:
                path to the file or directory to be uploaded.
        Returns:
            list of files that have been uploaded.
        """
        files = self.get_files_to_upload(bucket_name, path)
        self.upload_files(bucket_name, list(map(lambda x: x[0], files)))
        return files

    def get_remote_files_etag(self, bucket_name: str):
        """
        Gets the remote files ETag (MD5 hash).
        Args:
            str bucket_name:
                name of the bucket.

        Returns:
            Generator with the file names and their ETags.
        """
        files = self.get_remote_files(bucket_name)
        for item in files:
            yield (item['Key'], item['ETag'][1:-1])

    def get_remote_file_names(self, bucket_name: str) -> list:
        """
        Gets only the names of the remote files.
        Args:
            str bucket_name:
                name of the bucket.

        Returns:
            list of the remote file names
        """
        return list(map(lambda x: x.get('Key'), self.get_remote_files(bucket_name)))

    def get_files_to_upload(self, bucket_name, path: str):
        """
        Compares the file names and their MD5 hashes (ETags) in order to filter
        only the new and modified ones.
        Args:
            str bucket_name:
                name of the bucket.
            str path:
                path to the file or directory.
        Returns:
            list of items that are different from the bucket.
        """
        local_files = get_md5_recursively(path) if os.path.isdir(path) else [file_md5(path)]
        for file_ in self.get_remote_files_etag(bucket_name):
            if file_ in local_files:
                local_files.remove(file_)
        return local_files
