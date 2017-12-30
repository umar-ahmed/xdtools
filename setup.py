"""
Contains information for PyPi.
"""

from setuptools import setup

setup(
    name='xdtools',
    packages=['xdtools', 'xdtools.utils', 'xdtools.artwork', 'xdtools.style'],
    version='0.0.2',
    description='An unofficial Python API for Adobe Experience Design',
    author='Umar Ahmed',
    author_email='umar.ahmed@mail.utoronto.ca',
    url='https://github.com/umar-ahmed/xdtools',
    download_url='https://github.com/umar-ahmed/xdtools/archive/0.0.2.tar.gz',
    keywords=['adobe', 'xd', 'ui', 'ux'],
    license='MIT',
    zip_safe=False
)
