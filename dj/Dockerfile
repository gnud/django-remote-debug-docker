FROM python:3.7.4-stretch

WORKDIR /app/

ADD djproj .
ADD tools .


# 1. Basic python development setup
# 2. Clean apt
# 3. Install pip requirements
# 4. Install pip mw package
# 5. Cache cleanup


RUN apt-get update \
    && apt-get install vim less python3-dev musl-dev -y \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

    #&& python --version\
    #&& /usr/bin/python --version\
    #&& pip --version\
    #&& pip list\
    #&& rm -rf /var/lib/apt/lists/* \
    #&& rm -rf /libs/
 
CMD [ "gunicorn", "-c", "/app/gunicorn_live.conf.py", "djproj.wsgi:application"]

#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8888"]