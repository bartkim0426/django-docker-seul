import os

from .BASE import ROOT_DIR, CONFIG_DIR

# for integrate all static to staticfiles after migration
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# STATIC_ROOT = '/srv/static-files'
STATICFILES_DIRS = (
    str(ROOT_DIR.path('staticfiles')),
)
