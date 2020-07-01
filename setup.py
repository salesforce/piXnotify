#  Copyright (c) 2020, salesforce.com, inc.
#   * All rights reserved.
#   * SPDX-License-Identifier: BSD-3-Clause
#   * For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGES = [
    "piXnotify",
    "piXnotify.OSNotifiers",
    "piXnotify.OSNotifiers.macosx",
    "piXnotify.OSNotifiers.linux",
    "piXnotify.OSNotifiers.windows",
]


def os_requires(packages_list, os_name):
    return [f'{package};platform_system=="{os_name}"' for package in packages_list]


MAC_REQUIRES = os_requires(["pync==2.0.3"], "Darwin")
LINUX_REQUIRES = os_requires(["notify2==0.3.1"], "Linux")
WINDOWS_REQUIRES = os_requires(["win10toast==0.9"], "Windows")

PACKAGE_REQUIREMENTS = []
PACKAGE_REQUIREMENTS.extend(MAC_REQUIRES)
PACKAGE_REQUIREMENTS.extend(LINUX_REQUIRES)
PACKAGE_REQUIREMENTS.extend(WINDOWS_REQUIRES)

setuptools.setup(
    name="piXnotify",
    version="0.0.1",
    author="franck.barbedor",
    author_email="franck.barbedor@salesforce.com",
    description="A cross-platform notifications library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salesforce/piXnotify/",
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=PACKAGE_REQUIREMENTS,
)
