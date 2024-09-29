#!/bin/bash

# Wait for the database to be ready (optional, but recommended)
# Adjust the sleep duration as necessary
sleep 10

# Apply migrations
python manage.py makemigrations
python manage.py migrate

echo "Running tests..."
python manage.py test jiradata

# # Create superuser if it doesn't already exist
# if ! python manage.py shell -c "from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(username='admin').exists())"; then
#     echo "Creating superuser..."
#     echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', '${SUPERUSER_PASSWORD}')" | python manage.py shell
# else
#     echo "Superuser already exists."
# fi

# Start the Django development server
exec python manage.py runserver 0.0.0.0:8000