from setuptools import setup

setup(
    name='unholster-flake8',
    version='0.3.0',
    description='Flake8 Dependencies',
    url='git@github.com:Unholster/unholster-flake8.git',
    author='Unholster',
    author_email='',
    license='unlicense',
    packages=['unholster-flake8'],
    install_requires=[
        'flake8>=3.8,<3.9',
        'flake8-bugbear==20.11.1',
        'flake8-builtins==1.5.3',
        'flake8-colors>=0.1',
        'flake8-commas>=2.0,<3',
        'flake8-comprehensions>=3.3,<3.4',
        'flake8-debugger>=4.0,<4.1',
        'flake8-eradicate>=1.0,<1.1',
        'flake8-import-order>=0.18,<0.19',
        'flake8-print>=4.0,<4.1',
        'flake8-quotes>=3.2,<3.3',
        'pep8-naming>=0.11,<0.12',
    ],
    zip_safe=False,
)
