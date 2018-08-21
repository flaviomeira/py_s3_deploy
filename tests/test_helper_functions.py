from unittest import TestCase
import os
import shutil

from interface.helper import file_md5, directory_files_md5, get_md5_recursively


class TestRemoteActions(TestCase):

    def setUp(self):
        if 'tmp' not in os.listdir():
            os.mkdir('tmp')
        with open('tmp/test1', 'w') as f:
            f.write('foo')
        with open('tmp/test2', 'w') as f:
            f.write('bar')

    def tearDown(self):
        shutil.rmtree('tmp')

    def test_calculate_file_md5(self):
        result = file_md5('tmp/test2')
        expected_result = ('tmp/test2', '37b51d194a7513e45b56f6524f2d51f2') 
        self.assertEqual(expected_result, result)

    def test_calculate_directory_files_md5(self):
        result = directory_files_md5('tmp')
        expected_result = [('tmp/test2', '37b51d194a7513e45b56f6524f2d51f2'), 
                           ('tmp/test1', 'acbd18db4cc2f85cedef654fccc4a4d8')]
        self.assertEqual(expected_result, result)

    def test_calculate_md5_recursively(self):
        result = get_md5_recursively('tmp')
        expected_result = [('tmp/test2', '37b51d194a7513e45b56f6524f2d51f2'),
                           ('tmp/test1', 'acbd18db4cc2f85cedef654fccc4a4d8')]
        self.assertEqual(expected_result, result)
