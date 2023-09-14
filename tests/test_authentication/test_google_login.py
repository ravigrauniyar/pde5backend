import pytest
import requests
from django.urls import reverse
# from rest_framework.
from account.views.access_token_genrator_view import google_login


def test_google_access_token_generation():
    response = reverse('google-access-token-generate')
    assert response is not None

def test_google_login(api_client):
    pass