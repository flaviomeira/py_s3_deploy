from functools import reduce
from hashlib import md5
from typing import Iterable
import os


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
        if not '__iter__' in dir(local_files) or not '__iter__' in dir(remote_files):
            return {'Objects': []}
        return {'Objects': [{'Key': x} for x in remote_files if x not in local_files]}


def file_md5(file_path: str) -> tuple:
    """
    Calculates the MD5 hash of a file.
    Args:
        str file_path:
            path to the file
    
    Returns:
        tuple containing the file path and the calculated MD5
    """
    filehash = md5()
    with open(file_path, 'rb') as f:
        filehash.update(f.read())
    return file_path, filehash.hexdigest()


def directory_files_md5(path: str) -> list:
    """
    Calculates the md5 of all the files in a given directory.
    Args:
        str path:
            desired path.
    
    Returns:
        list of tuples with the file names and hashes in the following format:
            [('file1', 'hash1'),
             ('file2', 'hash2')]
    """
    files = []
    for file_ in os.listdir(path):
        file_dir = os.path.join(path, file_)
        if not os.path.isdir(file_dir):
            files.append(file_md5(file_dir))
    return files


def get_md5_recursively(path: str) -> list:
    """
    Walks through a given directory to get the hashes of all files within it,
    including in subfolders.
    Args:
        str path:
            desired path.
    
    Returns:
        list of all the tree of files and their md5 in the following format:
            [('file1', 'hash1'),
             ('module/file2', 'hash2')]
    """
    hashes = map(lambda x: directory_files_md5(x[0]), os.walk(path))
    return reduce(lambda crr, src: crr + src, hashes)


def directory_files(path: str) -> list:
    """
    Gets all the directory files.
    Args:
        str path:
            desired path.
    
    Returns:
        list of file names
    """
    files = []
    for file_ in os.listdir(path):
        file_dir = os.path.join(path, file_)
        if not os.path.isdir(file_dir):
            files.append(file_dir)
    return files


def directory_files_recursively(path: str) -> list:
    """
    Gets a list with all the files within the given path, recursively.
    Args:
        str path:
            desired path.
    Returns:
        list of file paths.
    """
    roots = map(lambda x: directory_files(x[0]), os.walk(path))
    files = reduce(lambda crr, src: crr + src, roots)
    if path == '.':
        files = list(map(lambda x: x[2:], files))
    return files


def print_list(list_: list):
    for item in list_:
        print(item)