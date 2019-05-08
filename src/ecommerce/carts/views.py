from django.shortcuts import render, redirect
from .models import Cart
from ecommerce.products.models import Product

# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    # del request.session['cart_id']
    # request.session['cart_id'] = '12'
    # cart_id = request.session.get('cart_id', None)
    # # if cart_id is None:     # and isinstance(cart_id, int):
    # #     cart_obj = cart_create()
    # #     request.session['cart_id'] = cart_obj.id
    # # else:
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count() == 1:
    #     print('cart ID exists')
    #     cart_obj = qs.first()   # if this cart doesn't have any user
    #     if request.user.is_authenticated and cart_obj.user is None:
    #         cart_obj.user = request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)  # this should handle user authenticated or not
    #     request.session['cart_id'] = cart_obj.id
    return render(request, "carts/home.html", {})

    # print(request.session)  # on the request
    # print(dir(request.session))
    # request.session.set_expiry(300) # 5 minutes
    # key = request.session.session_key
    # print(key)
    # 'session_key', 'set_expiry'
    # request.session['user'] = request.user.username    # Setter of SESSIOn


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(product_obj)  # cart_obj.products.add(product_id)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    # return redirect(product_obj.get_absolute_url())
    return redirect('cart:home')
