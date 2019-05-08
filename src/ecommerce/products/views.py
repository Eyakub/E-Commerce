from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404

from .models import Product
from ..carts.models import Cart


# Create your views here.
class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = 'products/featured-detail.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all()


# class base View
class ProductListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     # print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


# function base View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found..')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('Uhmmm')
        return instance


# class base View
class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')

        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesn't match")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


# function base View
def product_detail_view(request, pk=None, *args, **kwargs):
    qs = Product.objects.filter(id=pk)
    print(qs)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404('Product doesnt exist')
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
