from django.conf import settings

PHOTOS_PATH    = getattr(settings, 'NEWSLY_PHOTOS_PATH', 'uploads/newsly/%(slug)s/photos/%(filename)s')
DOCUMENTS_PATH = getattr(settings, 'NEWSLY_DOCUMENTS_PATH', 'uploads/newsly/%(slug)s/docs/%(filename)s')

