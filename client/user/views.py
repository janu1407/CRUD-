from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Client
# Create your views here.

def index(request):
    users = Client.objects.all()
    return render(request, 'users/index.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        user = Client(
            user_id=request.POST['user_id'],
            user_name=request.POST['user_name'],
            user_email=request.POST['user_email'],
            user_password=request.POST['user_password'],
            user_address=request.POST['user_address'],
            user_phone=request.POST['user_phone'],
            status=request.POST['status']
        )
        user.save()
        return redirect('index')
    return render(request, 'users/create_user.html')

def update_user(request, user_id):
    user = Client.objects.get(user_id=user_id)
    # user = get_object_or_404(Client, uuid=user_id)
    if request.method == 'POST':
        user.user_name = request.POST['user_name']
        user.user_email = request.POST['user_email']
        user.user_password = request.POST['user_password']
        user.user_address = request.POST['user_address']
        user.user_phone = request.POST['user_phone']
        user.status = request.POST['status']
        user.save()
        return redirect('index')
    return render(request, 'users/update_user.html', {'user': user})

def delete_user(request, user_id):
    user = Client.objects.get(user_id=user_id)
    user.delete()
    return redirect('index')


