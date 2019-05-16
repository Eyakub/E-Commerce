from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from src.ecommerce.ecom.forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    # if not request.user.is_authenticated():
    #     return LoginForm
    # print(request.session.get('first_name', 'Unknown'))   # GETTER of SESSION
    context = {
        'title': 'Hello world',
        'name': 'MD. Eyakub Sorkar',
    }
    if request.user.is_authenticated:
        context['premium_content'] = 'yeahhhhhhhh'
    return render(request, 'home_page.html', context)


def about_page(request):
    return render(request, 'home_page.html', {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to the contact page.',
        'form': contact_form,
        'brand': 'new Brand name',
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('full_name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    # print('User logged in')
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # context['form'] = LoginForm()
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())
        if user is not None:
            login(request, user)
            # Redirect to a success page
            # context['form'] = LoginForm()
            return redirect('test/login')
        else:
            print('Error')

    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        print(form.cleaned_data)
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)
