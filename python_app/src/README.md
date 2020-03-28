NOTE: sample database db.sqlite3 committed just to avoid migrate in the docker for the demonstration. 

# Usage


## Prepare IDE

Open this project with root as djproj in the IDE.

In the IDE create a new "Python remote debug" config.

Find the "pydevd-pycharm.egg" file found in debug-eggs/ of the Pycharm Pro installation and copy it in the tools
directory besides the .git-keep file

Now run the config with debug.

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

# Testing the debug

Set a breakpoint in the IDE either in the app.py.
Then just run the ```docker-compose up``` (make sure the remote debug config is active)