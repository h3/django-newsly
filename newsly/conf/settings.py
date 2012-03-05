from django.conf import settings

STATIC_URL     = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_URL)
STATIC_ROOT    = getattr(settings, 'NEWSLY_STATIC_URL', settings.STATIC_ROOT)
PHOTOS_PATH    = getattr(settings, 'NEWSLY_PHOTOS_PATH', 'uploads/newsly/%(slug)s/photos/%(filename)s')
DOCUMENTS_PATH = getattr(settings, 'NEWSLY_DOCUMENTS_PATH', 'uploads/newsly/%(slug)s/docs/%(filename)s')
AUTHOR_DISPLAY = getattr(settings, 'NEWSLY_AUTHOR_DISPLAY', 'fullname') # 'fullname', 'username', False
GRPAPPELLI_TINYMCE = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE', False)
GRPAPPELLI_TINYMCE_SRC = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE_SRC',  'admin/tinymce/jscripts/tiny_mce/tiny_mce.js')
GRPAPPELLI_TINYMCE_CONF = getattr(settings, 'NEWSLY_GRPAPPELLI_TINYMCE_CONF', 'website/js/tinymce_setup.js')
