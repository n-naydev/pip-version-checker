# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pip_version_checker']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pip-version-checker',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Nayden Naydev',
    'author_email': 'n.naydev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)