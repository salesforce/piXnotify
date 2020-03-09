# piXnotify

This project is an attempt to build a cross-platform notification library in python.

It heavily relies on platform-dependant notification libraries, namely 

- [pync](https://github.com/SeTeM/pync)
- [notify2](https://notify2.readthedocs.io/en/latest/)
- [win10toast](https://pypi.org/project/win10toast/)

You could also use [plyer](https://github.com/kivy/plyer/tree/master/plyer) project which aims to provide a whole set of cross platform features such as notifications, camera manipulation ...

## Setup

Run 
```
pip install .
``` 
or 
```
python setup.py sdist
python setup.py install
```

This will install platform-specific python packages, specified in python.py .

## Usage

Typical package usage will be:

```
from piXnotify import notifier

notifier.setTitle("Title").setMessage("message").notify()
```
