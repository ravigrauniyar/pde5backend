import jwt
import datetime
from django.conf import settings

def generate_access_token(user):
    access_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        "iat": datetime.datetime.utcnow()
    }

    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY
    )

    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow()
    }

    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY
    )

    return refresh_token