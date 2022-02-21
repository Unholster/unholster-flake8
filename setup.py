from setuptools import setup

setup(
    name='unholster-flake8',
    version='0.5.0',
    description='Flake8 Dependencies',
    url='git@github.com:Unholster/unholster-flake8.git',
    author='Unholster',
    author_email='',
    license='unlicense',
    packages=['unholster-flake8'],
    install_requires=[
        'flake8>=4.0,<4.1',
        'flake8-bugbear==22.1.11',
        'flake8-builtins==1.5.3',
        'flake8-colors>=0.1',
        'flake8-commas>=2.0,<3',
        'flake8-comprehensions>=3.7,<3.8',
        'flake8-debugger>=4.0,<4.1',
        'flake8-eradicate>=1.2,<1.3',
        'flake8-import-order>=0.18,<0.19',
        'flake8-print>=4.0,<4.1',
        'flake8-quotes>=3.3,<3.4',
        'pep8-naming>=0.12,<0.13',
    ],
    zip_safe=False,
)
