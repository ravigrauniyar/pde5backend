# This is only for testing purposes. Will be removed after integration with frontend.

import os
import requests
from django.conf import settings
from account.decorators import debug_only
from django.http import HttpResponse, HttpResponseRedirect

@debug_only
def google_login(request):
    auth_url = f'https://accounts.google.com/o/oauth2/auth?' \
               f'client_id={settings.GOOGLE_CLIENT_ID}&' \
               f'redirect_uri={settings.REDIRECT_URI}&' \
               f'scope=email profile openid&' \
               f'response_type=code'
    return HttpResponseRedirect(auth_url)

@debug_only
def google_callback(request):
    code = request.GET.get('code')
    
    token_url = 'https://accounts.google.com/o/oauth2/token'
    token_payload = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': settings.REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    token_response = requests.post(token_url, data=token_payload)

    if token_response.status_code == 200:
        tokens = token_response.json()
        access_token = tokens.get('access_token')
        return HttpResponse(access_token)
    return HttpResponse("Invalid credentials")
    