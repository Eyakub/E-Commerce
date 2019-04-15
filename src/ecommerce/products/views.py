from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.


# class base View
class ProductListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


# function base View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


# class base View
class ProductDetailView(generic.DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # print(context)
        return context


# function base View
def product_detail_view(request, pk=None, *args, **kwargs):
    print(pk)
    instance = Product.objects.get(id=pk)
    # instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/details.html", context)
