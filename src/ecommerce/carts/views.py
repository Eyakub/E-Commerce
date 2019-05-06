from django.shortcuts import render


# Create your views here.
def cart_home(request):
    print(request.session)  # on the request
    print(dir(request.session))
    # request.session.set_expiry()
    # request.session.session_key
    'session_key', 'set_expiry'
    return render(request, "carts/home.html", {})
