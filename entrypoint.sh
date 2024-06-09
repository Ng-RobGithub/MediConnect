#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Run database migrations
python manage.py migrate --noinput

# Execute the CMD from the Dockerfile
exec "$@"
