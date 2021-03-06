from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView





# Redirects to the profile page
def home(request):
    redirect('/paper')

# The signup page
def signup(request):
    # Checks if the user is sending their data (POST) or getting the form (GET)
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        # Makes sure the user filled out the form correctly as dictated by forms.py
        if form.is_valid():
            user = form.save(commit=False)
            # Sets the user to deactive until they confirm email
            user.is_active = True
            # Saves the user to the server
            user.save()
            
            return render(request, 'accounts/please_confirm.html')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

# The activation page for new users
# The uidb64 and token are generated in signup
def activate(request, uidb64, token):
    # Tries to decode the uid and use it as a key to find a user
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # Sets the user to active
        user.is_active = True
        user.save()
        #profile.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return render(request, 'accounts/account_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')

def logoutLander(request):
    return redirect('/login')
    #return render(request, 'accounts/logout_lander.html')
