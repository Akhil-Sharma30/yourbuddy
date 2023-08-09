# Baldev

1. pip install -r requirements.txt
2.  Check that pyobjc is installed `(pip show pyobjc)`, if not install as pip install pyobjc. 
3. open this file `baldev-bot/lib/python3.11/site-packages/pyttsx3/drivers/nsss.py`
4. replace this in line 14 `self = objc.super(NSSpeechDriver, self).init()`
3. run Recognize.py file