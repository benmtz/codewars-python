<img width="110px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png" />
<img width="110px" src="https://docs.codewars.com/logo.svg" />

# Codewars python

This repository is where I test my codewars kata solutions, you can find the original kata with the id on the first line of every solution.

## Installing environment

```sh
python -m venv env
./env/bin/pip install -r requirements.txt
```

## Useful commands

```sh
# Use the hooks folder to run pre-commit lint and test
git config core.hooksPath hooks
# Runing lint
./env/bin/pycodestyle katas
# Running tests
./env/bin/python -m unittest -f katas/*.py
```
