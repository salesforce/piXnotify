# piXnotify

This project is an attempt to build a cross-platform notification library in python.

It heavily relies on platform-dependant notification libraries, namely 

- [pync](https://github.com/SeTeM/pync)
- [notify2](https://notify2.readthedocs.io/en/latest/)

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

## Code of conduct

Salesforce open-source projects are committed to providing a friendly, safe, and welcoming environment for all. 

You may read more in the [Code of Conduct](./CODE_OF_CONDUCT.md).

The goal of this code of conduct is to specify a baseline standard of behavior so that people with different social values and communication styles can work together effectively, productively, and respectfully in our open source community. It also establishes a mechanism for reporting issues and resolving conflicts.

All questions and reports of abusive, harassing, or otherwise unacceptable behavior in a Salesforce open-source project may be reported by contacting the Salesforce Open Source Conduct Committee at ossconduct@salesforce.com.