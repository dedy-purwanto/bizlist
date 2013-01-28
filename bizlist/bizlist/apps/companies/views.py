from django.views.generic import ListView, FormView
from django.contrib import messages

from references.models import State, Category
from .models import Company, Product
from .forms import InquiryForm

class ListViewMixin(object):

    def get_context_data(self, *args, **kwargs):
        context = super(ListViewMixin, self).get_context_data(*args, **kwargs)
        selected_category = None

        try:
            state = State.objects.get(slug=self.kwargs['state'])
        except State.DoesNotExist:
            state = None

        try:
            category = Category.objects.get(slug=self.kwargs['category'])
            selected_category = category
        except Category.DoesNotExist:
            category = None

        try:
            sub_category = Category.objects.get(slug=self.kwargs['sub_category'])
            selected_category = sub_category
        except Category.DoesNotExist:
            sub_category = None


        context['selected_category'] = selected_category
        context['category'] = category
        context['sub_category'] = sub_category
        context['state'] = state
        context['selected_category_slug'] = 'all-categories' if category is None else category.slug
        context['selected_sub_category_slug'] = 'all-subcategories' if sub_category is None else sub_category.slug
        context['selected_state_slug'] = 'all' if state is None else state.slug

        context['states'] = State.objects.all().order_by('title')
        context['categories'] = Category.objects.filter(parent=None).order_by('title')
        if category is not None:
            context['sub_categories'] = Category.objects.filter(parent=category).order_by('title')

        return context


class CompanyDetailView(FormView):
    form_class = InquiryForm
    template_name = 'companies/company_detail.html'

    def form_valid(self, form):
        form.save(company=self.get_object())
        message = "Your inquiry has been sent. Thank you."
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(CompanyDetailView, self).form_valid(form)

    def get_object(self, *args, **kwargs):
        slug = self.kwargs['company_slug']
        return Company.objects.get(slug=slug)

    def get_success_url(self, *args, **kwargs):
        return self.request.get_full_path()

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(*args, **kwargs)

        context['object'] = self.get_object()

        return context


class CompanyListView(ListViewMixin, ListView):

    paginate_by = 2
    model = Company
    template_name = 'companies/company_list.html'

    def get_queryset(self):

        qs = super(CompanyListView, self).get_queryset()

        try:
            state = State.objects.get(slug=self.kwargs['state'])
            qs = qs.filter(state=state)
        except State.DoesNotExist:
            pass

        try:
            sub_category = Category.objects.get(slug=self.kwargs['sub_category'])
            qs = qs.filter(categories=sub_category)
        except Category.DoesNotExist:
            try:
                category = Category.objects.get(slug=self.kwargs['category'])
                qs = qs.filter(categories=category)
            except Category.DoesNotExist:
                pass

        return qs


    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)
        return context



class ProductListView(ListViewMixin, ListView):

    paginate_by = 2
    model = Product
    template_name = 'companies/product_list.html'

    def get_queryset(self):

        qs = super(ProductListView, self).get_queryset()

        try:
            state = State.objects.get(slug=self.kwargs['state'])
            qs = qs.filter(company__state=state)
        except State.DoesNotExist:
            pass

        try:
            sub_category = Category.objects.get(slug=self.kwargs['sub_category'])
            qs = qs.filter(category=sub_category)
        except Category.DoesNotExist:
            try:
                category = Category.objects.get(slug=self.kwargs['category'])
                qs = qs.filter(category=category)
            except Category.DoesNotExist:
                pass

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


class ProductDetailView(FormView):
    form_class = InquiryForm
    template_name = 'companies/product_detail.html'

    def form_valid(self, form):
        form.save(company=self.get_object().company, product=self.get_object())
        message = "Your inquiry has been sent. Thank you."
        messages.add_message(self.request, messages.SUCCESS, message)
        return super(ProductDetailView, self).form_valid(form)

    def get_object(self, *args, **kwargs):
        slug = self.kwargs['product_slug']
        company_slug = self.kwargs['company_slug']
        return Product.objects.get(company__slug=company_slug, slug=slug)

    def get_success_url(self, *args, **kwargs):
        return self.request.get_full_path()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)

        context['object'] = self.get_object()

        return context
