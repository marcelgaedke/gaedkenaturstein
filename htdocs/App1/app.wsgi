#!/usr/bin/python
import sys, os

sys.path.insert(0, '/var/www/ssd1400/priv/App1')
sys.path.insert(0, '/var/www/ssd1400/priv/venv/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'App1.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()