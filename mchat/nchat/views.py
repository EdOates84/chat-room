from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'nchat/index.html')

def room(request,room_name):
    return render(request, 'nchat/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name))
    })    

#def my_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
#        return render(request, 'nchat/index.html', {'myuser':username})
#    else:
#        return HttpResponse('Invalid')


