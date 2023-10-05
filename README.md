# yourbuddy

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/Akhil-Sharma30/yourbuddy/workflows/CI/badge.svg
[actions-link]:             https://github.com/Akhil-Sharma30/yourbuddy/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/yourbuddy
[conda-link]:               https://github.com/conda-forge/yourbuddy-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/Akhil-Sharma30/yourbuddy/discussions
[pypi-link]:                https://pypi.org/project/yourbuddy/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/yourbuddy
[pypi-version]:             https://img.shields.io/pypi/v/yourbuddy
[rtd-badge]:                https://readthedocs.org/projects/yourbuddy/badge/?version=latest
[rtd-link]:                 https://yourbuddy.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->
## Install dependencies
### MacOS
1. Install the python packages in virutal env
```

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