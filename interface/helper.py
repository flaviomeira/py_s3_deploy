from functools import reduce
from hashlib import md5
import os


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
    filehash.update(open(file_path, 'rb').read())
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


def get_md5_recursively(path: str) -> dict:
    """
    Walks through a given directory to get the hashes of all files within it,
    including in subfolders.
    Args:
        str path:
        desired path.

    Returns:
        dictionary with all the tree of files and their md5.
    """
    def _closure():
        for x in os.walk(path):
            yield {k: v for k, v in directory_files_md5(x[0])}
    return reduce(lambda x, src: x.update(src) or x, _closure(), {})
