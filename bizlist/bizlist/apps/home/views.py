from django.views.generic import TemplateView

from references.models import Category, State
from companies.models import Company

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):

        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['states'] = State.objects.all().order_by('title')

        categories = Category.objects.filter(parent=None)

        categories_column = []
        categories_rows = 8

        for i in range(0,99):
            categories_column.append(categories[i * categories_rows : (i * categories_rows) + categories_rows])
            if i * categories_rows > categories.count() - 1:
                break

        if len(categories_column[len(categories_column)-1]) == 0:
            categories_column.pop()



        context['categories_column'] = categories_column

        context['featured_companies'] = Company.objects.filter(featured=True)[:3]


        return context
