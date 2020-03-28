FROM python:3.7.4-stretch

WORKDIR /app/

ADD src .
ADD tools .


# 1. Basic python development setup
# 2. Clean apt
# 3. Cache cleanup


RUN apt-get update \
    && apt-get install vim less python3-dev musl-dev -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /libs/ \

ENTRYPOINT ["/usr/bin/python", "app.py"]
