import requests

def validate_google_access_token(access_token):
    """
    This function takes access_token as input. It sends this token to the google token validating api.
    It returns token info if token is validated else returns False
    """
    token_info_url = "https://oauth2.googleapis.com/tokeninfo"
    params = {"access_token": access_token}

    token_info_response = requests.get(token_info_url, params=params)

    if token_info_response.status_code == 200:
        token_info = token_info_response.json()

        # Check if the token is valid
        return not "error_description" in token_info
    return False
    
"""
This function takes access_token as input.
It sends a get request containing access_token to the google api and get the user info.
It returns that user_data if available
"""
def get_google_user(access_token):
    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)
    if user_info_response.status_code == 200:
        user_data = user_info_response.json()
        return user_data
    return None