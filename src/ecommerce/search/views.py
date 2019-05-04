from django.shortcuts import render
from django.views.generic import ListView

from ecommerce.products.models import Product


# Create your views here.
class SearchProductView(ListView):
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        """
            __icontains
            __iexact
        """
        request = self.request
        method_dict = request.GET
        # print(request.GET)
        query = request.GET.get('q', None)
        # print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.features()
