FROM python:3

# FROM python:3
# ENV PYTHONUNBUFFERED=1
# RUN apt-get update && apt-get install -y postgresql-client && pip install psycopg2==2.8.6
# WORKDIR /testproject
# COPY requirements.txt /testproject/
# RUN pip install -r requirements.txt
# COPY . /testproject/

ENV C_FORCE_ROOT 1

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

# Install PostgreSQL dependencies
RUN apt-get update && \
    pip install --upgrade pip && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*


# Step 1: Install any Python packages
# ----------------------------------------

ENV PYTHONUNBUFFERED 1
RUN mkdir /var/app
WORKDIR  /var/app
COPY requirements.txt /var/app/requirements.txt
# TODO: Remove this line
RUN pip install psycopg2==2.8.6  
RUN pip install -r requirements.txt

# Step 2: Copy Django Code
# ----------------------------------------

COPY . /var/app/.

EXPOSE 8080

CMD ["/var/app/runserver.sh"]