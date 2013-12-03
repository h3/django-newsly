import os
import datetime

from django.core.urlresolvers import reverse
from django import template

from newsly.models import News

register = template.Library()


@register.assignment_tag
def get_latest_news(*args, **kwargs):
    """
    Returns a sorted list of news

    {% get_latest_news author=1 category=2 limit=10 as latest_news %}
    """
    limit    = kwargs.get('limit', None)
    author   = kwargs.get('author', None)
    category = kwargs.get('category', None)
    qs       = News.published.all()

    if author:   qs = qs.filter(author_id=author)
    if category: qs = qs.filter(category_id=category)

    return limit and qs[0:limit] or qs


@register.simple_tag()
def embed_player(v, w):
    """
    Returns an Youtube embed player for a given video URL
    """
    html = '<iframe width="%(w)s" height="%(h)s" src="http://www.youtube.com/embed/%(src)s" frameborder="0" allowfullscreen></iframe>'
    try:
        if "embed" not in v:
            v = v.split('?v=')[1].split('&')[0]
        return html % {'w': str(w), 'src': v, 'h': int(int(w) * 0.75) }
    except:
        return ''


@register.filter()
def get_file_extension(f):
    """
    Returns a file extension for a given path or filename

    >>> get_file_extension("test.pdf")
    pdf

    >>> get_file_extension("/tmp/test.pdf")
    pdf

    """
    basename, ext = os.path.splitext(str(f))
    return ext.replace('.', '').lower()
