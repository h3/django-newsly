from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, TemplateView, DetailView

from newsly.models import *
from newsly.conf import settings as newsly_settings


class NewsView(ListView):
    template_name = 'newsly/news_list.html'
    paginate_by = 4

    def get_queryset(self):
        a = self.request.GET.get('a', None)
        c = self.request.GET.get('c', None)
        y = self.request.GET.get('y', None)
        m = self.request.GET.get('m', None)

        if a:
            qs = News.published.filter(author=a)
        elif c:
            if c == 'None':
                qs = News.published.filter(category__isnull=True)
            else:
                qs = News.published.filter(category=c)
        elif y and m:
            qs = News.published.filter(date_publish__year=y, date_publish__month=m)
        else:
            qs = News.published.filter()

        return qs

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['date_list']   = News.published.values('date_publish')
        context['category_list']   = News.published.values('category', 'category__title', 'category__pk').order_by('category__title').distinct()
        context['author_list'] = News.published.values('author', 'author__username', \
                'author__first_name', 'author__last_name').order_by('author__username').distinct()
        context['grappelli_tinymce'] = newsly_settings.GRPAPPELLI_TINYMCE
        return context


class NewsDetail(DetailView):
    template_name = 'newsly/news_detail.html'
    model = News

    def get_object(self):
        try:
            return News.published.get(slug=self.kwargs.get('slug'))
        except News.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['video_size'] = newsly_settings.VIDEOS_SIZE
        context['first_thumbnail_size'] = newsly_settings.FIRST_THUMBNAIL_SIZE
        context['thumbnail_size'] = newsly_settings.THUMBNAIL_SIZE
        context['grappelli_tinymce'] = newsly_settings.GRPAPPELLI_TINYMCE
        return context
