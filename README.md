# Modern Django Example

## Requirements

- Python3.6+

### Optional requirements

- Go1.8.3+

## Setup

Create virtual environment and activate virtual environment.

```
make env
source env/bin/activate
```

Install dependencies.

```
make deps
```

Execute migrations.

```
make migrate
```

Create administrator account.

```
make superuser
```

## Run

```
./manage.py web runserver
```

- API Token Endpoint: http://127.0.0.1:8000/auth/token/
- API Endpoint: http://127.0.0.1:8000/api/
- Admin site: http://127.0.0.1:8000/admin/

See docs/REDME.org
