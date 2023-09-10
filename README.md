# Baldev

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
