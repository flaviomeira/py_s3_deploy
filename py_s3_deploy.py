import os

from boto3 import client as boto3_client

s3 = boto3_client('s3')

BUCKET = 'test2207'


def get_files_to_delete(local_files, remote_files) -> list:
    if type(local_files) != list or type(remote_files) != list:
        return []
    return [x for x in remote_files if x not in local_files]


def get_remote_files(bucket_name=BUCKET) -> list:
    s3_objects = s3.list_objects(Bucket=bucket_name)
    return s3_objects['Contents']


def delete_aws_files(files_to_delete: dict, bucket_name=BUCKET) -> list:
    deleted_files = s3.delete_objects(Bucket=bucket_name, Delete=files_to_delete)
    return deleted_files['Deleted']


def main():
    local_path = 'C:\\Users\\flaviomeira10\\Desktop\\s3test'
    _local_files = os.listdir(local_path)
    _remote_files = get_remote_files()
    files = get_files_to_delete(local_files=_local_files,
                                remote_files=[x['Key'] for x in _remote_files])

    files_to_delete = {'Objects': [{'Key': x} for x in files]}
    deleted = delete_aws_files(files_to_delete) if files else None
    if deleted:
        print('Deleted files: ')
        list(map(print, deleted))


if __name__ == "__main__":
    main()
