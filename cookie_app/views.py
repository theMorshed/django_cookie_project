from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    response = render(request, 'set_cookie.html')
    # response.set_cookie('name', 'morshed')
    # response.set_cookie('name', 'morshed', expires=60)
    response.set_cookie('name', 'morshed', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')  
    return response
