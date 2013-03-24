from django.shortcuts import render
from signup.models import *
from signup.forms import *

def signup_page(response):
    form = SignupForm()
    values = {}
    values["form"] = form
    return render_to_response(request, 'signupform.html', values)