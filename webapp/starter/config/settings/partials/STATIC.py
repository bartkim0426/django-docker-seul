import os

from .BASE import ROOT_DIR, CONFIG_DIR

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_DIRS = (
    CONFIG_DIR.path('static'),
)
