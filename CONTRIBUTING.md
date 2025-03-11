# Contributing

Thank you for your consideration in contributing.

This guide serves as a head start to running the project locally.

I look forward to merging your pull request to help make this project even better!

## Local development

Once the repository has been cloned locally, you'll need to setup an editable install to run the tests, as follows.

### Setup

Note that this guide will use pyenv will require [pyenv](https://github.com/pyenv/pyenv) to be installed.

First, create a virtual environment using `pyenv virtualenv ci-test`.

Then, activate the environment using `pyenv activate ci-test`. This will set the local python version specifically for `ci-test`.

Now you can install an editable version of `ci-test` using `python -m pip install --editable .` assuming you are within the `ci-test` folder.

You can now run the test suite using `python -m unittest` !

### Uninstall

To uninstall the editable install, run `python -m pip uninstall ci-test` from within the virtual environment.

To remove the virtual environment, run `pyenv virtualenv-delete ci-test`

