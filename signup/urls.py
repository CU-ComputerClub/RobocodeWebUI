from django.conf.urls import patterns, include, url

urlpattends=patterns(
    url(r'^/signup$', 'signup.views.signup_page')
)