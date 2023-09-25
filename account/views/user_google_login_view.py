import jwt

from account.models import UserAccount
from account.utils import generate_access_token, generate_refresh_token
from account.serializers.user_profile_serializer import UserDetailSerailizer
from account.serializers.google_login_serializer import GoogleLoginSerializer
from account.services.google_services import get_google_user, validate_google_access_token

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.conf import settings


class UserGoogleLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        """
        This function takes user request as input. Request contains access_token generated and given by google.
        Passing the access token to get_google_user function will return the user data. This user data is either retrieved or created.
        New access and refresh token is then to provided to the user in reponse.
        """
        # Get the access token from the request POST data
        serailizer = GoogleLoginSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        access_token = serailizer.validated_data['access_token']

        # Validate the Google access token
        if not validate_google_access_token(access_token):
            return Response("Invalid access token", status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve user data from google using the access token
        user_data = get_google_user(access_token)

        # Create or get a UserAccount instance based on the user's email
        user_instance, created = UserAccount.objects.get_or_create(
            email = user_data["email"],
            defaults= {
                "username": user_data['email'],
                "first_name": user_data['given_name'],
                "last_name": user_data['family_name'],
                "display_name": user_data['name'],
                "avatar": user_data['picture']
            }
        )

        # Generate access and refresh tokens
        access_token = generate_access_token(user_instance)
        refresh_token = generate_refresh_token(user_instance)

        # Create a response with access token and set a cookie with the refresh token
        data = {"access_token": access_token, "refresh_token": refresh_token}

        response =  Response(
            data=data,
            status=status.HTTP_202_ACCEPTED,
        )
        response.set_cookie(key="refreshtoken", value=refresh_token, httponly=True)

        return response


@api_view(["GET"])
def profile(request):
    if request.user:
        user = request.user
        serializer = UserDetailSerailizer(user)
        return Response({"user": serializer.data})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def refresh(request):    
    """
    This view function takes request as input. Request contains refresh_token.
    Refresh token is checked for its validity and new access token is returned in reponse if valid.
    """
    # Get the refresh token from the request data
    refresh_token = request.data.get('refresh_token')
    try:
        # Decode the refresh token using the Django secret key
        refresh_token = refresh_token.split(" ")[1]
        payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms='HS256'
        )

    except jwt.ExpiredSignatureError:
        return Response('Expired Refresh Token' ,status=status.HTTP_401_UNAUTHORIZED)

    
    # Retrieve the user associated with the refresh token
    user = UserAccount.objects.filter(id=payload.get("user_id"), is_active=True).first()

    if user is None:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)

    # Generate a new access token and return it in the response
    access_token = generate_access_token(user)
    return Response({"access_token": access_token}, status=status.HTTP_201_CREATED)