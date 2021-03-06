Docker Django
-------------

[![Circle CI](https://circleci.com/gh/erroneousboat/docker-django/tree/master.svg?style=shield)](https://circleci.com/gh/erroneousboat/docker-django/tree/master)

## Usage
```bash
$ git clone https://github.com/bartkim0426/django-docker-seul.git
# when delpoy
$ docker-compose up
# when development
$ docker-compose -f docker-compose-dev.yml up
```

Now you can access the application at <https://localhost> and the admin site
at <https://localhost/admin>.

## Settings
### Have to change `development.env` and `development_local.env`
- `NGINX_SERVER_NAME` : add server name
### `uwsgi` settings
- in `webapp/config/django-uwsgi.ini`
### `Nginx` settings: HAVE TO set up before build image
- In `services/webserver/config/nginx.tmpl`

## Processes (deploying)
### -1. Build and run `db`
- Using `postgres:9.6` image
- Create volumes at `psql-data` in project dir. (Using `development.env`)
### -2. Build and run `webapp`
- using `webapp/Dockerfile` to build. 
- Add `webapp/config/requirements.txt`, `webapp/config/start.sh/`, `webapp/starter` to projectand `pip install`
- Run `adduser` and `chown` commands
- Run `webapp/config/start.sh`: migrate => collectstatic => starting uWSGI
### -3. Build and run `webserver`
- Using `services/webserver/Dockerfile` to build
- Add `start.sh`, `nginx.tmpl`
- Run `start.sh` => Starting Nginx

## Using multiple project
- Can change port in `development_local.env`: `NGINX_PORT`, and `NGINX_SERVER_NAME`
- Ex) `NGINX_PORT=8000`, `NGINX_SERVER_NAME=localhost:8000`
- Then you can access `localhost:8000` with existing `localhost` docker-compose



## Following To-do list
[X] `chmod 755` to `media` directory in `webapp`, `webserver`
[X] `postgres` database volumes checking
[X] Not deploy at once
[X] Changing dev environment nginx port 


## Folder structure

```
$ tree -L 1 --dirsfirst
.
├── config              # files needed for configuration
├── services            # services that support the webapp
├── webapp              # actual webapp
├── circle.yml          # circle ci setup file
├── docker-compose.yml  # docker-compose setup with container orchestration instructions
├── LICENSE             # license for this project
└── README.md           # this file
```

## Setting up

### Docker
See installation instructions at: [docker documentation](https://docs.docker.com)

```bash
$ curl -sSL https://get.docker.com/ubuntu/ | sudo sh
```

### Docker Compose
Install [docker compose](https://github.com/docker/compose), see installation
instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/):

```bash
# Install with PyPi
$ pip install docker-compose

# or install via curl
curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Check the [github project](https://github.com/docker/docker-compose/releases) for new releases

### Django
Create django project in the `webapp` folder or copy a project to the `webapp`
folder or use the sample project enclosed in this project and go directly to
the section 'Fire it up':

```bash
# be sure you have Django installed on your system
$ django-admin startproject <name_project>
```

Edit `config/environment/development.env` file and add the name of your
project at `DJANGO_PROJECT_NAME` or just leave it as is to start the default
application.


Edit the `settings.py` file with the correct database credentials and static
root:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

STATIC_ROOT = '/srv/static-files'
```

### Environment variables
The file `config/environment/development.env` contains the environment
variables needed in the containers. You can edit this as you see fit, and at
the moment these are the defaults that this project uses. However when you
intend to use this, keep in mind that you should keep this file out of version
control as it can hold sensitive information regarding your project. The file
itself will contain some commentary on how a variable will be used in the
container.

## Fire it up
Start the container by issuing one of the following commands:
```bash
$ docker-compose up             # run in foreground
$ docker-compose up -d          # run in background
```

## Other commands
Build images:
```bash
$ docker-compose build
$ docker-compose build --no-cache       # build without cache
```

See processes:
```bash
$ docker-compose ps                 # docker-compose processes
$ docker ps -a                      # docker processes (sometimes needed)
$ docker stats [container name]     # see live docker container metrics
```

See logs:
```bash
# See logs of all services
$ docker-compose logs

# See logs of a specific service
$ docker-compose logs -f [service_name]
```

Run commands in container:
```bash
# Name of service is the name you gave it in the docker-compose.yml
$ docker-compose run [service_name] /bin/bash
$ docker-compose run [service_name] python /srv/starter/manage.py shell
$ docker-compose run [service_name] env
```

Remove all docker containers:
```bash
docker rm $(docker ps -a -q)
```

Remove all docker images:
```bash
docker rmi $(docker images -q)
```

### Some commands for managing the webapp
To initiate a command in an existing running container use the `docker exec`
command.

```bash
# Find container_name by using docker-compose ps

# restart uwsgi in a running container.
$ docker exec [container_name] touch /etc/uwsgi/reload-uwsgi.ini

# create migration file for an app
$ docker exec -it [container-name] \
    python /srv/[project-name]/manage.py makemigrations scheduler

# migrate
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py migrate

# get sql contents of a migration
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py sqlmigrate [appname] 0001

# get to interactive console
$ docker exec -it [container-name] \
    python3 /srv/[project-name]/manage.py shell

# testing
docker exec [container-name] \
    python3 /srv/[project-name]/manage.py test
```

## Troubleshooting
Q: I get the following error message when using the docker command:

```
FATA[0000] Get http:///var/run/docker.sock/v1.16/containers/json: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS? 

```

A: Add yourself (user) to the docker group, remember to re-log after!

```bash
$ usermod -a -G docker <your_username>
$ service docker restart
```

Q: Changes in my code are not being updated despite using volumes.

A: Remember to restart uWSGI for the changes to take effect.

```bash
# Find container_name by using docker-compose ps
$ docker exec [container_name] touch /etc/uwsgi/reload-uwsgi.ini
```
