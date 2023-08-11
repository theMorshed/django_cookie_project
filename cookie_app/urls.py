from django.urls import path
from cookie_app.views import home, get_cookie, delete_cookie, set_session, get_session, delete_session

urlpatterns = [
    path('', home, name='homepage'),
    path('get_cookie/', get_cookie),
    path('delete_cookie/', delete_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session, name='get_session'),
    path('delete_session/', delete_session),
]
