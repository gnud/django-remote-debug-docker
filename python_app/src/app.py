import os
import sys

# Set variables backed by .env config
host = os.getenv('host', 'localhost')
port = os.getenv('port', 51234)
pydevd_path = os.getenv('pydevd', 'pydevd-pycharm.egg')
pydevd_enabled = '1' in os.environ.get('pydevd_enabled', '1')

if pydevd_enabled:
    sys.path.append(pydevd_path)
    print(sys.path)  # test to see current paths
    # help('modules') # for testing to see module pydevd
    import pydevd

    pydevd.settrace(host, port=port, stdoutToServer=True, stderrToServer=True)


print('this will end app')
