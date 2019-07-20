from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='dict-tools',
    version='0.1.0',
    description='Utilities for dealing with dictionaries',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='dictionaries',
    url='https://github.com/firba1/dict-tools',
    author='Ben Bariteau',
    author_email='ben.bariteau@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['dict_tools'],
)
