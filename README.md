[![Build Status](https://travis-ci.org/flaviomeira/py_s3_deploy.svg?branch=master)](https://travis-ci.org/flaviomeira/py_s3_deploy)
# Python S3 Deploy

AWS deployment made easy.

## Getting Started

To effectively make the deployment, you'll need to pass the local path (root of the application) and the bucket name

```
python py_s3_deploy.py --local-path <path> --bucket-name <bucket>
```

This will upload the whole tree to the bucket passed using the default profile on your aws credentials file.
If you want to use different credentials, you can use the --profile (-p) flag:

```
python py_s3_deploy.py -P <path> -B <bucket> -p <profile>
```

Now, in order to remotely delete files which are not in the local project anymore, the --delete-removed(-d) flag is needed

```
python py_s3_deploy.py -P <path> -B <bucket> -d
```

Finally, if you want to upload only files with different hashes (modified files) among the new files, there's the --etag (-e) flag

```
python py_s3_deploy.py -P <path> -B <bucket> -e
```

## Running the tests

```
tox
```

### Unit testing:

For now, we're using the unittest default lib for writing the tests and mocking.
Use the existent tests as a model to write yours.

### Why to unit test:

The unit tests validate the interface's functionalities and help us with maintenance of the system, it's important to write tests for EVERYTHING.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/flaviomeira/py_s3_deploy/tags). 

## Authors

* **Flavio Meira** - *Initial work and development* - [flaviomeira](https://github.com/flaviomeira)
* **Leonardo Rodrigues** - *development* - [Lelor](https://github.com/Lelor)

## Acknowledgments
* This project is inspired by the great work made in the npm [s3-deploy](https://www.npmjs.com/package/s3-deploy)
