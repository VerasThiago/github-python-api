#!/bin/bash

echo "Creating migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating super user..."

create-superuser() {
    local username="test"
    local email="test@gmail.com"
    local password="test"
    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="$username").exists():
    User.objects.create_superuser("$username", "$email", "$password")
else:
    print('User "{}" exists already, not created'.format("$username"))
EOF
}

create-superuser

echo "Running server on 0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000

echo "done!"
