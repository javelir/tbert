from setuptools import setup
from tbert import __version__, __description__, __url__, __author__, \
    __author_email__, __keywords__

NAME = 'tbert'

setup(
    name=NAME,
    version=__version__,
    description=__description__,
    long_description='See ' + __url__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    keywords=__keywords__,

    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[NAME],
    install_requires=['torch~=0.4.1'],
    entry_points={
        'console_scripts': [
            'ilabs_bulk_predict=ilabs.client.ilabs_bulk_predict:main',
            'ilabs_dv=ilabs.client.ilabs_datavault_api:main'
        ]
    }
)