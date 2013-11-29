Installation
============

1. In `settings.py` add `newsly` to your `INSTALLED_APPS`.
2. Add `(r'news/', include('newsly.urls')),` to your `urls.py`.
3. If you have south: `migrate newsly`, else syncdb

Settings
--------

+--------------------------------+-------------------------------------------------------+
| Setting                        | Default                                               |
+================================+=======================================================+
| NEWSLY_ADMIN_SEARCH_FIELDS     | `('title',)`                                          |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_AUTHOR_DISPLAY          | 'fullname'  ('fullname', 'username' or `False`)       |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_AUTO_AUTHOR             | `False`                                               |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_AUTO_DATE_PUBLISH       | `False`                                               |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_CATEGORIES              | `False`                                               |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_DATE_UNPUBLISH          | `True`                                                |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_DOCUMENTS_PATH          | 'uploads/newsly/%(slug)s/docs/%(filename)s'           |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_FIRST_THUMBNAIL_SIZE    | '190x190'                                             |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_GRPAPPELLI_TINYMCE      | `False`                                               |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_GRPAPPELLI_TINYMCE_CONF | 'website/js/tinymce_setup.js'                         |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_GRPAPPELLI_TINYMCE_SRC  | 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'     |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_PHOTOS_PATH             | 'uploads/newsly/%(slug)s/photos/%(filename)s'         |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_SEO                     | `True`                                                |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_STATIC_URL              | `settings.STATIC_ROOT`                                |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_STATIC_URL              | `settings.STATIC_URL`                                 |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_THUMBNAIL_SIZE          | '94x94'                                               |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_USE_TEASER              | `True`                                                |
+--------------------------------+-------------------------------------------------------+
| NEWSLY_VIDEOS_SIZE             | '240' (height is calculated from width)               |
+--------------------------------+-------------------------------------------------------+

Template tags
=============

```django
{% load newsly_tags %}

{% get_latest_news limit=10 as latest_news %}
{{ latest_news }}


{% get_latest_news author=1 category=2 limit=10 as latest_news %}

```


Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
