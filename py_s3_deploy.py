from argparse import ArgumentParser

from boto3 import Session
from args import configure_parser
from interface.remote_actions import S3Interface


parser = ArgumentParser(description='Python S3 deploy.')
args = configure_parser(parser)
session = Session(profile_name=args.profile)
s3 = session.client('s3')


def main():
    s3_interface = S3Interface(s3)
    if args.delete_removed:
        print('Deleted files:')
        s3_interface.delete_removed_files(args.local_path, args.bucket_name)

    if args.etag:
        print('\nUploading files')
        s3_interface.upload_only_different_files(args.bucket_name, args.local_path)
    else:
        print('\nUploading files')
        s3_interface.upload_files_from_local_path(args.bucket_name,
                                                  args.local_path)


if __name__ == "__main__":
    main()
