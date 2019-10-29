-DEPLOY: cd ansible && ansible-playbook site.yaml
-makemigrations: DOTENV=dotenv.env python manage.py makemigrations
-migrate: DOTENV=dotenv.env python manage.py migrate

SERVE-DEV: DOTENV=dotenv.env python manage.py runserver
SERVE-SSL: DOTENV=dotenv.env gunicorn service_web.wsgi:application --keyfile local/server.key --certfile local/server.crt
