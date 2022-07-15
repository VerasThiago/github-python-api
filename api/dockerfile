FROM python:3

ENV C_FORCE_ROOT 1

# Install PostgreSQL dependencies
RUN apt-get update && \
    pip install --upgrade pip && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*


ENV PYTHONUNBUFFERED 1
RUN mkdir /var/app
WORKDIR  /var/app
COPY requirements.txt /var/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /var/app/.

ENTRYPOINT ["/var/app/entrypoint.sh"]