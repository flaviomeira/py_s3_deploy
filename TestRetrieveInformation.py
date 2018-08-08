from unittest import TestCase, main
from unittest.mock import patch

from py_s3_deploy import get_remote_files, s3


class TestGetRemoteFiles(TestCase):

    def setUp(self):
        self.bucket_name = 'test2207'
        self.local_path = 'tests'

    def test_retrieve_file_info_from_bucket(self):
        with patch.object(s3, 'list_objects', return_value={'Contents': ['test1', 'test2', 'test3']}):
            retrieved_files = get_remote_files(self.bucket_name)
            self.assertEqual(['test1', 'test2', 'test3'], retrieved_files)


if __name__ == '__main__':
    main()
