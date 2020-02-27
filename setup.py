from setuptools import setup

setup(
    name='unholster-flake8',
    version='0.0.1',
    description='Flake8 Dependencies',
    url='git@github.com:Unholster/unholster-flake8.git',
    author='Unholster',
    author_email='',
    license='unlicense',
    packages=['unholster-flake8'],
    intstall_requires=[
        'flake8',
    ],
    zip_safe=False
)