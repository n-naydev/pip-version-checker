# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["pip_version_checker"]

package_data = {"": ["*"]}

setup_kwargs = {
    "name": "pip-version-checker",
    "version": "0.1.0",
    "description": "",
    "long_description": None,
    "author": "Nayden Naydev",
    "author_email": "n.naydev@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "python_requires": ">=3.8,<4.0",
    "entry_points": {
        "console_scripts": ["pip_version_check=pip_version_checker.cli:main"],
    },
    "install_requires": [
        "requests==2.26.0",
        "packaging==21.3",
        "dparse==0.5.1",
        "click==8.0.3",
        "toml==0.10.2",
    ],
}


setup(**setup_kwargs)
