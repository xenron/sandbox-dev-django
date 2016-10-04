from django.conf import settings
from django.contrib.auth import (
    SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY,
    get_user_model
)
from django.contrib.sessions.backends.db import SessionStore

from selenium import webdriver


def create_session_cookie(username, password, create_instance):

    if create_instance:
        # First, create a new test user
        user_model = get_user_model()
        user = user_model.objects.create_user(username=username, password=password)
    else:
        user = get_user_model()
        user = user.objects.get(username=username, password=password)

    # Then create the authenticated session using the new user credentials
    session = SessionStore()
    session[SESSION_KEY] = user.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()

    # Finally, create the cookie dictionary
    cookie = {
        'name': settings.SESSION_COOKIE_NAME,
        'value': session.session_key,
        'secure': False,
        'path': '/',
    }
    return cookie


def get_test_browser():
    # browser = webdriver.PhantomJS()
    browser = webdriver.Firefox()
    # browser = webdriver.Chrome()
    return browser
