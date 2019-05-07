from django.shortcuts import render
from .models import Cart


# Create your views here.
def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('new cart created')
    return cart_obj


def cart_home(request):
    # del request.session['cart_id']
    request.session['cart_id'] = '12'
    cart_id = request.session.get('cart_id', None)
    # if cart_id is None:     # and isinstance(cart_id, int):
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print('cart ID exists')
        cart_obj = qs.first()
    else:
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    return render(request, "carts/home.html", {})

    # print(request.session)  # on the request
    # print(dir(request.session))
    # request.session.set_expiry(300) # 5 minutes
    # key = request.session.session_key
    # print(key)
    # 'session_key', 'set_expiry'
    # request.session['user'] = request.user.username    # Setter of SESSIOn
