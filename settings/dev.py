from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
"""STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE_SECRET key>')"""

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://218509b4.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'josephmartinlodge@gmail.com'

