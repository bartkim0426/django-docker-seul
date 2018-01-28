import os

from .BASE import ROOT_DIR, CONFIG_DIR

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(ROOT_DIR, 'mediafiles')
# MEDIA_ROOT = str(ROOT_DIR('mediafiles'))
MEDIA_ROOT = '/srv/media-files'
MEDIA_DIRS = (
    str(ROOT_DIR.path('media')),
)
