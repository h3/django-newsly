from django.conf import settings

STATIC_URL     = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_URL)
STATIC_ROOT    = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_ROOT)
PHOTOS_PATH    = getattr(settings, 'NEWSLY_PHOTOS_PATH', 'uploads/newsly/%(slug)s/photos/%(filename)s')
DOCUMENTS_PATH = getattr(settings, 'NEWSLY_DOCUMENTS_PATH', 'uploads/newsly/%(slug)s/docs/%(filename)s')
AUTHOR_DISPLAY = getattr(settings, 'NEWSLY_AUTHOR_DISPLAY', 'fullname') # 'fullname', 'username', False
