# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ambari_lld',
    version='0.0.1',
    description='Ambari alerts as Zabbix LLD items',
    long_description=long_description,
    url='https://github.com/vide/zabbix_ambari',
    author='Davide Ferrari',
    author_email='vide80@gmail.com',
    license='GPLv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Topic :: System :: Monitoring',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'],
    keywords='ambari zabbix lld',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'ambari_zabbix_lld=ambari_lld:main',
        ],
    },
)
