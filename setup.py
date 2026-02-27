"""
Flask-Script-NG
-----------------

A fork of Flask-Script for modern Flask and Python.

Links
`````

* `Flask-Script documentation <http://flask-script.readthedocs.org>`_
* `Original Flask-Script repository <https://github.com/smurfix/flask-script>`_


"""
import sys
from setuptools import setup

version='2.1'

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# https://github.com/pypa/virtualenv/pull/259)
try:
    import multiprocessing
except ImportError:
    pass

install_requires = ['Flask>=2.2.4']

setup(
    name='Flask-Script-NG',
    version=version,
    url='https://github.com/makise-homura/flask-script-ng',
    download_url = 'https://github.com/makise-homura/flask-script-ng/tarball/v'+version,
    license='BSD',
    author='Dan Jacob, Matthias Urlichs, Igor Molchanov',
    author_email='danjac354@gmail.com, matthias@urlichs.de, akemi_homura@kurisa.ch',
    maintainer='Igor Molchanov',
    maintainer_email='akemi_homura@kurisa.ch',
    description='Scripting support for modern Flask and Python',
    long_description=__doc__,
    packages=[
        'flask_script_ng'
    ],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[
        'pytest>=7.0',
    ],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
