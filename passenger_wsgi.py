# -*- coding: utf-8 -*-
import os
import sys

# sys.path.insert(0, '/var/www/u0000006/data/www/faq-reg.ru/project_name')
# sys.path.insert(1, '/var/www/u0000006/data/djangoenv/lib/python2.7/site-packages')

sys.path.insert(0, '/var/www/u0830091/data/www/safu-engineering.ru')
sys.path.insert(1, '/var/www/u0830091/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'safu.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
