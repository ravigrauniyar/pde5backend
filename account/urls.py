from django.urls import path
from account.views import access_token_genrator_view, user_email_signup_login_view, user_google_login_view

urlpatterns = [
    path('google/callback/', access_token_genrator_view.google_callback, name='google-callback'),
    path('login/', access_token_genrator_view.google_login, name='google-access-token-generate'),
    path('login/email/', user_email_signup_login_view.UserEmailSignInView.as_view(), name='email-login'),
    path('login/google/', user_google_login_view.UserGoogleLoginView.as_view(), name='google-login'),
    path('profile/', user_google_login_view.profile),
    path('signup/email/', user_email_signup_login_view.UserEmailSignUpView.as_view(), name='email-signup'),
    path('token/refresh/', user_google_login_view.refresh, name='token-refresh'),
]   