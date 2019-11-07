-DEPLOY: cd ansible && ansible-playbook site.yaml
-makemigrations: python manage.py makemigrations
-migrate: python manage.py migrate

SERVE-DEV: python manage.py runserver
SERVE-SSL: gunicorn service_web.wsgi:application --keyfile local/server.key --certfile local/server.crt

-test: python manage.py test
