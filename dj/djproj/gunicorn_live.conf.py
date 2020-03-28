import os

host = os.environ.get('web_host', '0.0.0.0')
port = os.environ.get('web_port', 8000)
workers = os.environ.get('workers', 1)
threads = os.environ.get('threads', 1)
request = os.environ.get('request', 1)
max_requests = os.environ.get('max_requests', 0)
max_requests_jitter = os.environ.get('max_requests_jitter', 0)

bind = f'{host}:{port}'
loglevel = 'debug'
capture_output = '1' in os.environ.get('capture_output', '1')
