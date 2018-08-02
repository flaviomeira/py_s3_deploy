from unittest import TestCase
from py_s3_deploy import get_files_to_delete


class TestDeleteRemoved(TestCase):

    def test_should_delete_one_file(self):
        local_file = ['file1']
        remote_files = ['file1', 'file2']
        removed_files = get_files_to_delete(local_file, remote_files)
        assert ['file2'] == removed_files, removed_files

    def test_should_not_delete_file_with_extension(self):
        local_file = ['file1.exe', 'files2.exe']
        remote_files = ['file1.exe', 'files2.exe', 'program 2231.exe']
        removed_files = get_files_to_delete(local_file, remote_files)
        assert ['program 2231.exe'] == removed_files, removed_files

    def test_should_not_delete_any_file(self):
        local_file = ['file1.exe', 'files2.exe']
        remote_files = ['file1.exe', 'files2.exe']
        removed_files = get_files_to_delete(local_file, remote_files)
        assert [] == removed_files, removed_files

    def test_should_not_delete_empty_list(self):
        local_file = []
        remote_files = []
        removed_files = get_files_to_delete(local_file, remote_files)
        assert [] == removed_files, removed_files

    def test_should_not_get_error_with_none_types(self):
        local_file = None
        remote_files = None
        removed_files = get_files_to_delete(local_file, remote_files)
        assert [] == removed_files, removed_files

