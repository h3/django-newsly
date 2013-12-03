# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from newsly.models import *
from newsly.conf import settings

if settings.GRPAPPELLI_TINYMCE:
    NEWSLY_JS = [
        '%s%s' % (settings.STATIC_URL, settings.GRPAPPELLI_TINYMCE_SRC),
        '%s%s' % (settings.STATIC_URL, settings.GRPAPPELLI_TINYMCE_CONF)]
else:
    NEWSLY_JS = []

try:
    from grappellifit.admin import TranslationAdmin, TranslationStackedInline
    ModelAdmin = TranslationAdmin
    StackedInlineAdmin = TranslationStackedInline
except:
    ModelAdmin = admin.ModelAdmin
    StackedInlineAdmin = admin.StackedInline


ADMIN_FIELDSET = []
FIELDS = []
ADMIN_LIST_DISPLAY = ['title', 'author', 'date_added']

if not settings.AUTO_AUTHOR:
    FIELDS.append('author')

if settings.CATEGORIES:
    FIELDS.append('category')
    ADMIN_LIST_DISPLAY.append('category')

if not settings.AUTO_DATE_PUBLISH:
    FIELDS.append('date_publish')
    ADMIN_LIST_DISPLAY.append('date_publish')

if settings.DATE_UNPUBLISH:
    FIELDS.append('date_unpublish')
    ADMIN_LIST_DISPLAY.append('date_unpublish')

ADMIN_FIELDSET.append((_('Title'), {
    'fields': ('title', 'slug',)
}))

if settings.USE_TEASER:
    ADMIN_FIELDSET.append((_('Teaser'), {
        'fields': ('teaser',)
    }))

ADMIN_FIELDSET.append((_('Content'), {
    'fields': ('body',)
}))

if len(FIELDS):
    ADMIN_FIELDSET.append((None, {'fields': FIELDS}))

if settings.SEO:
    ADMIN_FIELDSET.append((_('SEO'), {
        'fields': ('meta_keywords', 'meta_description',)
    }))




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
    list_filter = ('author',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_publish'
    inlines = [NewsPhotoInline, NewsVideoInline, NewsDocumentInline]

    list_display = ADMIN_LIST_DISPLAY
    search_fields = settings.ADMIN_SEARCH_FIELDS
    fieldsets = ADMIN_FIELDSET

    def save_model(self, request, obj, form, change):
        if settings.AUTO_AUTHOR:
            obj.author = request.user
        obj.save()

    class Media:
        # FIXME: This might clash with TranslationAdmin.Media.js ..
        js = NEWSLY_JS

admin.site.register(News, NewsAdmin)


class NewsCategoryAdmin(ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

if settings.CATEGORIES:
    admin.site.register(NewsCategory, NewsCategoryAdmin)
