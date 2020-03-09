import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

PACKAGES = [
    'piXnotify',
    'piXnotify.OSNotifiers',
    'piXnotify.OSNotifiers.macosx',
    'piXnotify.OSNotifiers.windows',
    'piXnotify.OSNotifiers.linux',
]


def os_requires(packages_list, os_name):
    return [f'{package};platform_system=="{os_name}"' for package in packages_list]


MAC_REQUIRES = os_requires(["pync"], "Darwin")
LINUX_REQUIRES = os_requires(["notify2"], "Linux")

PACKAGE_REQUIREMENTS = []
PACKAGE_REQUIREMENTS.extend(MAC_REQUIRES)
PACKAGE_REQUIREMENTS.extend(LINUX_REQUIRES)

setuptools.setup(
    name="piXnotify",
    version="0.0.1",
    author="franck.barbedor",
    author_email="franck.barbedor@salesforce.com",
    description="A cross-platform notificartion library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.soma.salesforce.com/franck-barbedor/piXnotify",
    packages=PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=PACKAGE_REQUIREMENTS
)
