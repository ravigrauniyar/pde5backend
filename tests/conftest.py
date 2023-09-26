import pytest
import requests
from rest_framework.test import APIClient
from tests.test_authentication.email_signup_test_data import EmailSignupFactory


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client():
    client = APIClient()
    new_user = EmailSignupFactory(email="test@user.com", password="testuser")

    login_credentials = {
        "email": "test@user.com",
        "password": "testuser"
    }

    response = requests.post("http://localhost:8000/api/account/login/email/", data=login_credentials)
    response.raise_for_status()

    access_token = response.json()["access_token"]

    client =  APIClient()

    client.credentials(HTTP_AUTHORIZATION=f'Token {access_token}')
    client.force_authenticate(user=new_user)

    return client