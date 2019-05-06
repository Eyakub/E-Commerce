from django.shortcuts import render


# Create your views here.
def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:     # and isinstance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print('Card ID exist')
    return render(request, "carts/home.html", {})

    # print(request.session)  # on the request
    # print(dir(request.session))
    # request.session.set_expiry(300) # 5 minutes
    # key = request.session.session_key
    # print(key)
    # 'session_key', 'set_expiry'
    # request.session['user'] = request.user.username    # Setter of SESSIOn
