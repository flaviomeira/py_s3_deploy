import os
from argparse import ArgumentParser

from boto3 import client as boto3_client
from args import configure_parser
from interface.remote_actions import S3Interface
from interface.helper import get_files_to_delete, print_list

s3 = boto3_client('s3')
parser = ArgumentParser(description='Python S3 deploy.')
args = configure_parser(parser)


def main():
    s3_interface = S3Interface(s3)
    if args.delete_removed:
        print_list(s3_interface.delete_removed_files(args.local_path, args.bucket_name))

    if args.etag:
        print_list(s3_interface.upload_only_different_files(args.bucket_name, args.local_path))


if __name__ == "__main__":
    main()
