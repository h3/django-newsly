from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, TemplateView, DetailView

from newsly.models import *

class NewsView(ListView):
    template_name = 'newsly/news_list.html'
    paginate_by = 3

    def get_queryset(self):
        a = self.request.GET.get('a', None)
        y = self.request.GET.get('y', None)
        m = self.request.GET.get('m', None)

        if a:
            qs = News.objects.filter(author=a)
        elif y and m:
            qs = News.objects.filter(date_added__year=y, date_added__month=m)
        else:
            qs = News.objects.filter()

        return qs
    
    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['date_list']   = News.objects.values('date_added')
        context['author_list'] = News.objects.values('author').order_by('author').distinct()
        return context


class NewsDetail(DetailView):
    template_name = 'newsly/news_detail.html'
    model = News    
