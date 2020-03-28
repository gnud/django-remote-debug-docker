NOTE: sample database db.sqlite3 committed just to avoid migrate in the docker for the demonstration. 

# Usage


## Prepare IDE

Open this project with root as djproj in the IDE.

In the IDE create a new "Python remote debug" config.

Find the "pydevd-pycharm.egg" file found in debug-eggs/ of the Pycharm Pro installation.

Now run the config with debug.

Please adjust the .env file before start, mainly the IP ADDRESS has to be your host address.

to run docker project

```bash
docker-compose up
```

to rebuild docker compose project

```bash
docker-compose up --build
```

to rebuild docker compose project (if paranoid)

```bash
docker-compose up --build --force-rebuild
```

make sure you run

```bash
docker-compose exec pyapp1 python manage.py collectstatic
```

If you want to see the admin in full style.

# Testing the debug

Set a breakpoint in the IDE either in the admin.py or models.py of the myapp django app of the save method.
Then open the admin at the contacts model and try to Add a new record by clicking save.
Expected to suspend on the breakpoint.


**NOTE**: As seen in the Dockerfile only gunicorn aka wsgi.py works, any command including runserver will not
work, somehow they are blocked.

# .env variables

host - remote debugger host (your machine IDE)
port - remote debugger
web_host - gunicorn
web_port - gunicorn
pydevd_path - full path to the egg
pydevd_enabled - 1 to enable, 0 to disable
static_path - Django settings STATIC_ROOT path
