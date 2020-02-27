# unholster-flake8

## Instalación con pip:

`pip install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Instalación con pipenv:

`pipenv install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>#egg=unholster-flake8`

## Uso

El archivo de configuración `tox.ini` que se recomienda es el siguiente:
```
[flake8]
exclude = */migrations/*.py,*_settings.py,settings.py,celery.py,*/base/models/__init__.py,*/base/__init__.py,docs
format = ${cyan}%(path)s${reset}:${yellow_bold}%(row)d${reset}:${green_bold}%(col)d${reset}: ${red_bold}%(code)s${reset} %(text)s
max-line-length = 100
inline-quotes = '
ignore = W503
application-import-names = <nombre-aplicación>
import-order-style = smarkets
```

Luego de instalar, ejecutar flake8 normalmente.
