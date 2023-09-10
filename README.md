# Baldev
[![Documentation Status](https://readthedocs.org/projects/Baldev/badge/?version=latest)](https://Baldev.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Akhil-Sharma30/Baldev/main.svg)](https://results.pre-commit.ci/latest/github/Akhil-Sharma30/Baldev/main)
[![codecov](https://codecov.io/gh/Akhil-Sharma30/Baldev/branch/main/graph/badge.svg?token=L6ObHKhaZ7)](https://codecov.io/gh/Akhil-Sharma30/Baldev)
[![discussion](https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github)](https://github.com/Akhil-Sharma30/Baldev/discussions)

[![Python Versions](https://img.shields.io/pypi/pyversions/Baldev)](https://pypi.org/project/Baldev/)
![License](https://img.shields.io/github/LICENSE/Akhil-Sharma30/Baldev?color=blue)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\

## Install dependencies
### MacOS
1. Install the python packages in virutal env
```
pip install -r requirements.txt
```
2.  Check that pyobjc is installed `(pip show pyobjc)`,**(Ignore the below step if working.)**

#### If not install with `pip install pyobjc`. 
```
open this file baldev-bot/lib/python3.11/site-packages/pyttsx3/drivers/nsss.py
```
> replace this in line 14
```
self = objc.super(NSSpeechDriver, self).init()
```
