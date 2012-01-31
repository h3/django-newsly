# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from news.models import *

try:
    from grappellifit.admin import TranslationAdmin, TranslationStackedInline
    ModelAdmin = TranslationAdmin
    StackedInlineAdmin = TranslationStackedInline
except:
    ModelAdmin = admin.ModelAdmin
    StackedInlineAdmin = admin.StackedInline


class NewsVideoInline(StackedInlineAdmin):
    model = NewsVideo
    extra = 1


class NewsPhotoInline(StackedInlineAdmin):
    model = NewsPhoto
    extra = 1


class NewsDocumentInline(StackedInlineAdmin):
    model = NewsDocument
    extra = 1


class NewsAdmin(ModelAdmin):
    list_display = ('title', 'date_added')
    list_filter = ('author',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_added'
    inlines = [NewsPhotoInline, NewsVideoInline, NewsDocumentInline]
    class Media:
        js = [
            '%sgrappelli/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.STATIC_URL,
            '%swebsite/js/tinymce_setup.js' % settings.STATIC_URL,
        ]
admin.site.register(News, NewsAdmin)
