import jwt
import pytest
import datetime

from unittest.mock import patch, Mock

from django.urls import reverse
from django.conf import settings

from rest_framework import status
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@patch('account.services.google_services.validate_google_access_token', return_value=True)
@patch('account.services.google_services.get_google_user', return_value=True)
@pytest.mark.django_db
def test_google_login_valid(mock_get_google_user, mock_validate_google_access_token, api_client):
    # Mock the API response when making the POST request
    mock_response = Mock(status_code=status.HTTP_202_ACCEPTED)
    mock_response.json.return_value = {"access_token": "mock_access_token", "refresh_token": "mock_refresh_token"}

    # Patch the api_client.post method to return the mock_response
    with patch.object(api_client, 'post', return_value=mock_response):
        # Create a mock valid access token
        mock_token_payload = {
            "iss": "accounts.google.com",  # Issuer (Google)
            "sub": "mock_user_id",         # User ID
            "email": "test@user.com",      # User's email address
            "aud": "your_client_id",       # Your application's client ID
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Expiration time (1 hour from now)
            "iat": datetime.datetime.utcnow(),  # Issued at time
        }

        google_api_secret_key = settings.GOOGLE_CLIENT_SECRET

        mock_access_token = jwt.encode(mock_token_payload, google_api_secret_key, algorithm='HS256')

        # Send a POST request with the mock access token
        response = api_client.post(reverse('google-login'), {"access_token": mock_access_token}, format='json')

        assert response.status_code == status.HTTP_202_ACCEPTED