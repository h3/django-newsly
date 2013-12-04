from django.conf import settings

STATIC_URL     = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_URL)
STATIC_ROOT    = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_ROOT)
PHOTOS_PATH    = getattr(settings, 'NEWSLY_PHOTOS_PATH', 'uploads/newsly/%(slug)s/photos/%(filename)s')
DOCUMENTS_PATH = getattr(settings, 'NEWSLY_DOCUMENTS_PATH', 'uploads/newsly/%(slug)s/docs/%(filename)s')
AUTHOR_DISPLAY = getattr(settings, 'NEWSLY_AUTHOR_DISPLAY', 'fullname') # 'fullname', 'username', False
GRPAPPELLI_TINYMCE = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE', False)
GRPAPPELLI_TINYMCE_SRC = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE_SRC',  'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js')
GRPAPPELLI_TINYMCE_CONF = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE_CONF', 'website/js/tinymce_setup.js')

VIDEOS_SIZE = getattr(settings, 'NEWSLY_VIDEOS_SIZE', '240')
FIRST_THUMBNAIL_SIZE = getattr(settings, 'NEWSLY_FIRST_THUMBNAIL_SIZE', '190x190')
THUMBNAIL_SIZE = getattr(settings, 'NEWSLY_THUMBNAIL_SIZE', '94x94')

ADMIN_SEARCH_FIELDS = getattr(settings, 'NEWSLY_ADMIN_SEARCH_FIELDS', ('title',))

USE_TEASER = getattr(settings, 'NEWSLY_USE_TEASER', True)
AUTO_AUTHOR = getattr(settings, 'NEWSLY_AUTO_AUTHOR', False)
DATE_PUBLISH = getattr(settings, 'NEWSLY_DATE_PUBLISH', True)
DATE_UNPUBLISH = getattr(settings, 'NEWSLY_DATE_UNPUBLISH', True)
CATEGORIES = getattr(settings, 'NEWSLY_CATEGORIES', False)
SEO = getattr(settings, 'NEWSLY_SEO', True)
