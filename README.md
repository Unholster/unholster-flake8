# unholster-flake8

## Instalación con pip

`pip install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Instalación con pipenv

`pipenv install git+https://github.com/Unholster/unholster-flake8.git@<tag-version>#egg=unholster-flake8`

## Instalación con Poetry

`poetry add git+https://github.com/Unholster/unholster-flake8.git@<tag-version>`

## Uso

El archivo de configuración `tox.ini` que se recomienda es el siguiente:
```
[flake8]
exclude = .venv
format = ${cyan}%(path)s:${yellow_bold}%(row)d:${green_bold}%(col)d: ${red_bold}%(code)s ${reset}%(text)s
application-import-names = <nombre-aplicación>
select = C,E,F,W,I,Q,B,B9,T,A
ignore = W503, E501
import-order-style = smarkets
inline-quotes = '
max-line-length = 100
```

Luego de instalar, ejecutar `flake8` normalmente.
