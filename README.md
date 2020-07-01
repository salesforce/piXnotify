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

notifier.set_title("Title").set_message("message").notify()
```

Available options are:
- set_title
- set_message
- set_app_icon (WIP)
- set_activate (WIP)
- set_url (WIP)
- set_group (WIP)
- set_sound (WIP)
- set_execute (WIP)

As you can see, a lot of these are still WIP. This is mainly because of OS specific behaviours that have not been extensively tested yet. 

## Development and contributions

Contributions are encouraged, please use Issues to communicate on improvements you may be working on. 

In order to accept your pull request, we need you to submit a CLA. You only need to do this once, so if you've done this for another Salesforce open source project, you're good to go. If you are submitting a pull request for the first time, just let us know that you have completed the CLA and we can cross-check with your GitHub username.

[Complete your CLA here](https://cla.salesforce.com/sign-cla).

Code must be formatted with [black](https://pypi.org/project/black/). You can reformat all code before submission with this command: `black .` .

## Code of conduct

Salesforce open-source projects are committed to providing a friendly, safe, and welcoming environment for all. 

You may read more in the [Code of Conduct](./CODE_OF_CONDUCT.md).

The goal of this code of conduct is to specify a baseline standard of behavior so that people with different social values and communication styles can work together effectively, productively, and respectfully in our open source community. It also establishes a mechanism for reporting issues and resolving conflicts.

All questions and reports of abusive, harassing, or otherwise unacceptable behavior in a Salesforce open-source project may be reported by contacting the Salesforce Open Source Conduct Committee at ossconduct@salesforce.com.