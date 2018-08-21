from argparse import ArgumentParser
import os

from boto3 import client as boto3_client

from args import configure_parser
from interface.remote_actions import S3Interface
from interface.helper import get_files_to_delete

s3 = boto3_client('s3')
parser = ArgumentParser(description='Python S3 deploy.')
args = configure_parser(parser)


def main():
    s3_interface = S3Interface(s3)
    _local_files = os.listdir(args.local_path)
    _remote_files = s3_interface.get_remote_files(args.bucket_name)
    files_to_delete = get_files_to_delete(local_files=_local_files,
                                          remote_files=[x['Key'] for x in _remote_files])

    files_to_delete = {'Objects': [{'Key': x} for x in files]}
    if args.delete_removed:
        for item in s3_interface.delete_aws_files(files_to_delete,
                                                  args.bucket_name):
            print(item)

    if args.etag:
        s3_interface.upload_only_different_files(args.bucket_name)


if __name__ == "__main__":
    main()
