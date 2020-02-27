from setuptools import setup

setup(
    name='unholster-flake8',
    version='0.1.0',
    description='Flake8 Dependencies',
    url='git@github.com:Unholster/unholster-flake8.git',
    author='Unholster',
    author_email='',
    license='unlicense',
    packages=['unholster-flake8'],
    install_requires=[
        'flake8==3.7.9',
        'flake8-colors==0.1.6',
        'flake8-commas==2.0.0',
        'flake8-comprehensions==3.2.2',
        'flake8-debugger==3.2.1',
        'flake8-import-order==0.18.1',
        'flake8-quotes==2.1.1',
    ],
    zip_safe=False
)