FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
# dependencies for building Python packages
&& apt-get install -y build-essential \
# psycopg2 dependencies
&& apt-get install -y libpq-dev postgresql-client \
# Translations dependencies
&& apt-get install -y gettext \
# Additional dependencies
&& apt-get install -y procps \
# cleaning up unused files
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
&& rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./wagtail_app/requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt

COPY ./compose/local/django/entrypoint.sh /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start.sh /start
RUN chmod +x /start

WORKDIR /app/wagtail_app

ENTRYPOINT ["/entrypoint"]
