import os
from argparse import ArgumentParser

from boto3 import client as boto3_client
from args import configure_parser
from interface.remote_actions import S3Interface

s3 = boto3_client('s3')
parser = ArgumentParser(description='Python S3 deploy.')
args = configure_parser(parser)


def main():
    s3_interface = S3Interface(s3)
    _local_files = os.listdir(args.local_path)
    _remote_files = s3_interface.get_remote_files(args.bucket_name)
    files = s3_interface.get_files_to_delete(local_files=_local_files,
                                             remote_files=[x['Key'] for x in _remote_files])

    files_to_delete = {'Objects': [{'Key': x} for x in files]}
    if args.delete_removed:
        deleted = s3_interface.delete_aws_files(files_to_delete, args.bucket_name) if files \
            else None
        print('Deleted files:')
        list(map(print, deleted)) if deleted else print('There is no files to delete')


if __name__ == "__main__":
    main()
