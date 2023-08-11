from django.shortcuts import render, redirect
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


def set_session(request):
    data = {
        'name': 'Kuddus',
        'age': 24,
        'language': 'bangla'
    }
    request.session.update(data)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    return render(request, 'set_session.html')

def get_session(request):
    name = request.session.get('name')
    language = request.session.get('language')
    return render(request, 'get_session.html', {'name': name, 'language': language})

def delete_session(request):
    if request.session.get('name'):
        del request.session['name']
    # request.session.flush() #for delete complete session use this code
    return redirect('get_session')