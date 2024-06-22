#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

pwd
# ls
# echo $PYTHONPATH

# Create .env file with database configuration
echo -e "Hi Ula"

cat << EOF > .env
DB_NAME=test1
DB_USER=root
DB_PASSWORD=123
DB_HOST=mydb
DB_PORT=3307
EOF

poetry shell

echo -e "Hi Ula migrate"
# Run database migrations
# poetry run python manage.py migrate
python manage.py migrate

echo -e "Hi Ula runserver"
# Start the Django development server
# poetry run python manage.py runserver 0.0.0.0:80
python manage.py runserver 0.0.0.0:80
