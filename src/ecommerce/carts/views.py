from django.shortcuts import render, redirect
from .models import Cart
from ecommerce.products.models import Product
from ecommerce.orders.models import Order
from ecommerce.accounts.forms import LoginForm
from ecommerce.billing.models import BillingProfile
# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj,
    }
    return render(request, "carts/home.html", context)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
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

    # print(request.session)  # on the request
    # print(dir(request.session))
    # request.session.set_expiry(300) # 5 minutes
    # key = request.session.session_key
    # print(key)
    # 'session_key', 'set_expiry'
    # request.session['user'] = request.user.username    # Setter of SESSIOn


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print('Show message to user, product is gone?')
            return redirect('cart:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
        print(cart_obj.products.count())
    return redirect('cart:home')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    print(cart_obj)
    print(cart_created)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
        
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
    }
    return render(request, "carts/checkout.html", context)
