import os
import shutil

from unittest import TestCase, main
from unittest.mock import patch

from interface.remote_actions import S3Interface
from boto3 import client as boto3_client


class TestRemoteActions(TestCase):

    def setUp(self):
        self.s3 = boto3_client('s3')
        self.bucket_name = 'test2207'
        self.local_path = 'tests'
        os.mkdir('tmp')

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
