#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    try:
        proj = sys.argv[1]
        argv = [sys.argv[0]] + sys.argv[2:]
    except IndexError:
        print('Argument is missing.: manage.py PROJECT COMMAND (ex: ./manage.py web runserver)')
        sys.exit(1)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{}.settings".format(proj))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(argv)
