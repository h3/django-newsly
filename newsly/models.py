import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.db.models.signals import post_delete

from positions.fields import PositionField
from positions.managers import PositionManager

from newsly.utils import file_cleanup, get_news_photo_path, get_news_document_path
from newsly.conf import settings


class PublishedNewsManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(PublishedNewsManager, self).get_query_set()\
                    .exclude(date_unpublish__lte=now).exclude(date_publish__gte=now)


class NewsCategory(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    slug  = models.CharField(_("Slug"), max_length=250)
    def __unicode__(self):
        return u'%s' % self.title


class News(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    slug  = models.CharField(_("Slug"), max_length=250)
    author = models.ForeignKey(User)

    teaser = models.TextField(_("Text"))
    body  = models.TextField(_("Text"))

    date_added     = models.DateTimeField(auto_now_add=True)
    date_updated   = models.DateTimeField(auto_now=True)
    date_publish   = models.DateTimeField(blank=True, null=True)
    date_unpublish = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey(NewsCategory, blank=True, null=True)
    meta_description = models.CharField(_("Meta description"), max_length=165, blank=True, null=True)
    meta_keywords = models.CharField(_("Meta keywords"), max_length=250, blank=True, null=True)

    objects   = models.Manager()
    published = PublishedNewsManager()

    def save(self, *args, **kwargs):
        if self.date_publish is None:
            self.date_publish = datetime.datetime.now()
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('newsly-detail', args=[self.slug])

    def get_author_display(self):
        if settings.AUTHOR_DISPLAY:
            if settings.AUTHOR_DISPLAY == 'username':
                return self.author.username
            elif settings.AUTHOR_DISPLAY == 'fullname':
                a = "%s %s".strip() % (self.author.first_name, self.author.last_name)
                if a.strip() != '': 
                    return a.strip()
                else:
                    return self.author.username
        return False
        
    
    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-date_publish', )
        verbose_name = _('News')
        verbose_name_plural = _('News')


class NewsMediaBase(models.Model):
    title       = models.CharField(_("Title"), max_length=250)
    is_visible  = models.BooleanField(_('Is Visible'), default=True)
    date_added  = models.DateTimeField(auto_now_add=True)
    news        = models.ForeignKey(News)
    position    = PositionField()

    objects     = PositionManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('position', '-date_added',)
        abstract = True


class NewsPhoto(NewsMediaBase):
    photo = models.ImageField(_('Photo'), upload_to=get_news_photo_path)
    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
post_delete.connect(file_cleanup, sender=NewsPhoto, dispatch_uid="NewsPhoto.file_cleanup")


class NewsVideo(NewsMediaBase):
    video = models.URLField(_('URL'), max_length=250) 
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')


class NewsDocument(NewsMediaBase):
    document = models.FileField(_('Document (fr)'), upload_to=get_news_document_path)
    
    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
post_delete.connect(file_cleanup, sender=NewsDocument, dispatch_uid="NewsDocument.file_cleanup")
