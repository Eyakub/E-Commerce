from django.shortcuts import render
from .models import Cart


# Create your views here.
def cart_home(request):
    # del request.session['cart_id']
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:     # and isinstance(cart_id, int):
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id
        print('New Cart created')
    else:
        print('Card ID exist')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/home.html", {})

    # print(request.session)  # on the request
    # print(dir(request.session))
    # request.session.set_expiry(300) # 5 minutes
    # key = request.session.session_key
    # print(key)
    # 'session_key', 'set_expiry'
    # request.session['user'] = request.user.username    # Setter of SESSIOn
