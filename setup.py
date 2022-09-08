import datetime
from setuptools import setup

version_replace = str(datetime.date.today()).replace('-', '.')

setup(name='NASA_API', 
version= version_replace.replace('20', ''), 
description='pull data from nasa open api',
author='ryan',
packages=['NASA_API'],
install_requires=["discord.py", "PyYAML", "requests"],
zip_safe=False)
