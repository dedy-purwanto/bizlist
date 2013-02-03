from django.views.generic import ListView, DetailView

from articles.models import Article

class ViewMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(ViewMixin, self).get_context_data(*args, **kwargs)
        articles = Article.objects.all().order_by('-date_created')

        context['articles'] = articles

        return context


class ArticleListView(ViewMixin, ListView):

    template_name = 'articles/list.html'
    paginate_by = 5
    model = Article

    def get_queryset(self, *args, **kwargs):
        qs = Article.objects.all().order_by('-date_created')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)

        return context


class ArticleDetailView(ViewMixin, DetailView):

    template_name = 'articles/detail.html'
    model = Article

    def get_object(self, *args, **kwargs):
        object = Article.objects.get(pk=self.kwargs['pk'])
        return object

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        return context

