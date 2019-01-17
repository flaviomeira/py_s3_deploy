import os
import shutil

from unittest import TestCase, main
from unittest.mock import patch

from interface.remote_actions import S3Interface
from boto3 import client as boto3_client

class StubS3:
    def list_objects():
        return 

    def delete_objects():
        return

class TestRemoteActions(TestCase):

    def setUp(self):
        self.s3 = StubS3()
        self.bucket_name = 'test2207'
        self.local_path = 'tests'
        if 'tmp' not in os.listdir():
            os.mkdir('tmp')
        with open('tmp/test1', 'w') as f:
            f.write('foo')
    
    def tearDown(self):
        shutil.rmtree('tmp')

    def test_retrieve_file_info_from_bucket(self):
        with patch.object(self.s3, 'list_objects', return_value={'Contents': ['test1', 'test2', 'test3']}):
            interface = S3Interface(self.s3)
            retrieved_files = interface.get_remote_files(self.bucket_name)
            self.assertEqual(['test1', 'test2', 'test3'], retrieved_files)

    def test_delete_file_from_bucket(self):
        with patch.object(self.s3, 'delete_objects', return_value={'Deleted': ['test1']}):
            interface = S3Interface(self.s3)
            deleted_files = interface.delete_aws_files([{'Key': 'test1'}], self.bucket_name)
            self.assertEqual(['test1'], deleted_files)

    def test_get_only_different_files(self):
        with patch.object(self.s3, 
                          'list_objects',
                          return_value={'Contents':
                              [{'Key': 'test1', 'ETag': '"acbd18db4cc2f85cedef654fccc4a4d8"'}]}):
            interface = S3Interface(self.s3)
            result = interface.get_files_to_upload(self.bucket_name, 'tmp')
            self.assertEqual([], result)
