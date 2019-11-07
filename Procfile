-DEPLOY: cd ansible && ansible-playbook site.yaml
-makemigrations: python manage.py makemigrations
-migrate: python manage.py migrate

SERVE-DEV: python manage.py runserver
SERVE-SSL: DOTENV=dotenv.env gunicorn service_web.wsgi:application --keyfile local/server.key --certfile local/server.crt

-test: DOTENV=dotenv.env python manage.py test
