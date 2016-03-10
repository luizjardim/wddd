# EVENTEX

Sistema de Eventos encomendado pela morena.

[![Build Status](https://travis-ci.org/luizjardim/wddd.svg?branch=master)](https://travis-ci.org/luizjardim/wdd
[![Code Health](https://landscape.io/github/luizjardim/wddd/master/landscape.svg?style=flat)](https://landscape.io/github/luizjardim/wddd/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:luizjardim/eventex.git wddd
cd wddd
python -m venv .wddd
source .wddd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie um instância no Heroku.
2. Envie as configurações para o Heroku
3. Defina um SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstância
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```