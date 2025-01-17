from django.urls import path
from .views import AuthURL, spotify_callback, login_and_connect_spotify, delete_account_view

app_name = 'spotify'  # Add this to name the app, which can be helpful for namespacing

urlpatterns = [
    path('get-auth-url/', AuthURL.as_view(), name='get_auth_url'),  # Ensure this matches
    path('redirect/', spotify_callback, name='callback'),
    path('login/', login_and_connect_spotify, name='login_and_connect_spotify'),
    path('delete-account/', delete_account_view, name='delete_account'),
]
