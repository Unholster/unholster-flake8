# unholster-flake8

## Instalación con pip

`pip install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Instalación con pipenv

`pipenv install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>#egg=unholster-flake8`

## Instalación con Poetry

`poetry add git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Instalación con PDM

`pdm add unholster-flake8 @ git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Uso

El archivo de configuración `tox.ini` que se recomienda es el siguiente:
```
[flake8]
exclude = .venv
format = %(cyan)s%(path)s%(reset)s:%(yellow)s%(bold)s%(row)d%(reset)s:%(green)s%(bold)s%(col)d%(reset)s: %(red)s%(bold)s%(code)s %(reset)s%(text)s
application-import-names = <nombre-aplicación>
select = C,E,F,W,I,Q,B,B9,T,A
ignore = W503, E501
import-order-style = smarkets
inline-quotes = '
max-line-length = 100
```

Luego de instalar, ejecutar `flake8` normalmente.
