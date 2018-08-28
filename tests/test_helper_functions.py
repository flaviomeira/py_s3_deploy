from unittest import TestCase
import os
import shutil

from interface.helper import file_md5, directory_files_md5, get_md5_recursively, directory_files_recursively


class TestHelperFunctions(TestCase):

    def setUp(self):
        if 'tmp' not in os.listdir():
            os.mkdir('tmp')
            os.mkdir('tmp/test')
        with open(os.path.join('tmp', 'test1'), 'w') as f:
            f.write('foo')
        with open(os.path.join('tmp', 'test2'), 'w') as f:
            f.write('bar')
        with open(os.path.join('tmp', 'test', 'test_subfolder'), 'w') as f:
            f.write('barz')

    def tearDown(self):
        shutil.rmtree('tmp')

    def test_calculate_file_md5(self):
        result = file_md5(os.path.join('tmp', 'test2'))
        expected_result = (os.path.join('tmp', 'test2'), '37b51d194a7513e45b56f6524f2d51f2') 
        self.assertEqual(expected_result, result)

    def test_calculate_directory_files_md5(self):
        result = directory_files_md5('tmp')
        expected_result = [(os.path.join('tmp', 'test2'), '37b51d194a7513e45b56f6524f2d51f2'), 
                           (os.path.join('tmp', 'test1'), 'acbd18db4cc2f85cedef654fccc4a4d8')]
        self.assertEqual(expected_result, result)

    def test_calculate_md5_recursively_without_full_path(self):
        result = get_md5_recursively('tmp', full_path=False)
        expected_result = [('test2', '37b51d194a7513e45b56f6524f2d51f2'),
                           ('test1', 'acbd18db4cc2f85cedef654fccc4a4d8'),
                           (os.path.join('test', 'test_subfolder'), '8aaa7be4d67f40014c46c2393c9350b0')]
        self.assertEqual(expected_result, result)

    def test_calculate_md5_recursively_with_full_path(self):
        result = get_md5_recursively('tmp', full_path=True)
        expected_result = [(os.path.join('tmp', 'test2'), '37b51d194a7513e45b56f6524f2d51f2'),
                           (os.path.join('tmp', 'test1'), 'acbd18db4cc2f85cedef654fccc4a4d8'),
                           (os.path.join('tmp', 'test', 'test_subfolder'), '8aaa7be4d67f40014c46c2393c9350b0')]
        self.assertEqual(expected_result, result)
    
    def test_get_files_recursively_without_full_path(self):
        result = directory_files_recursively('tmp', full_path=False)
        expected_result = ['test2', 'test1', 'test/test_subfolder']
        self.assertEqual(expected_result, result)

    def test_get_files_recursively_with_full_path(self):
        result = directory_files_recursively('tmp', full_path=True)
        expected_result = [os.path.join('tmp', 'test2'),
                           os.path.join('tmp', 'test1'),
                           os.path.join('tmp', 'test/test_subfolder')]
        self.assertEqual(expected_result, result)
