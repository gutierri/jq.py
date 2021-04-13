from setuptools import setup

import jq

def long_description():
    with open('README.rst', encoding='utf8') as f:
        return f.read()

setup(
    name='jq.py',
    version=jq.__version__,
    description=jq.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type='text/x-rst',
    author='Gutierri Barboza',
    license='GPLv3+',
    scripts=['jq.py'],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
