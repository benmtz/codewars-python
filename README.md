# Codewars python

This repository is where I test my codewars kata solutions, you can find the original kata with the id on the first line of every solution.

## Installing environment

```sh
python -m venv env
./env/bin/pip install -r requirements.txt
```

## Userful commands

```sh
# Use the hooks folder to run pre-commit lint and test
git config core.hooksPath hooks
./env/bin/pycodestyle katas # Run lint
./env/bin/python -m unittest -f katas/*.py # Run tests


```
