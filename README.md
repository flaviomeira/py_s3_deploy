[![Build Status](https://travis-ci.org/flaviomeira/py_s3_deploy.svg?branch=master)](https://travis-ci.org/flaviomeira/py_s3_deploy)
# Python S3 Deploy

AWS deployment made easy.

## Getting Started

The first step is to clone the repository:

```
git clone git@github.com:flaviomeira/py_s3_deploy.git
```

Then go to the project folder and install the requirements:

```
pip install tox
```
You're ready to go


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
