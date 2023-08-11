from django.urls import path
from cookie_app.views import home, get_cookie, delete_cookie

urlpatterns = [
    path('', home, name='homepage'),
    path('get_cookie/', get_cookie),
    path('delete_cookie/', delete_cookie),
]
