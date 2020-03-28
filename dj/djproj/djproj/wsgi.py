"""
WSGI config for djproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproj.settings')


import os
import sys
# Set variables backed by .env config
host = os.getenv('host', 'localhost')
port = int(os.getenv('port', 51234))
pydevd_path = os.getenv('pydevd_path', 'pydevd-pycharm.egg')
pydevd_enabled = '1' in os.environ.get('pydevd_enabled', '1')
print(pydevd_path)

if pydevd_enabled:
    try:
        sys.path.append(pydevd_path)
        print(sys.path)  # test to see current paths
        # help('modules') # for testing to see module pydevd
        import pydevd

        print(f'pydevd will listen at {host}:{port}')
        pydevd.settrace(host, port=port, stdoutToServer=True, stderrToServer=True, suspend=True)
        print(f'pydevd listening at {host}:{port}')
    except Exception as e:
        print(f'pydevd server timeout at {host}:{port}')

application = get_wsgi_application()
