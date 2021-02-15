"""
WSGI config for SeeDCorp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/seedch/SeeDCorp/SeeDCorp')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/seedch/venvSeedCorp/lib/python3.9/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SeeDCorp.settings')

application = get_wsgi_application()
