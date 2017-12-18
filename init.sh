#!/bin/bash
python manage.py migrate && \
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'root123')" && \
python manage.py runserver 0.0.0.0:8000