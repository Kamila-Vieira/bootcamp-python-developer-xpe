from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def index(request):
  users = User.objects.all()
  context = {
    'users': users
  }
  return render(request, 'index.html', context=context)
  
def create(request):
  if request.method == 'GET':
    form = UserForm()
    
    context = {
      'form': form
    }
    return render(request, 'form.html', context=context)
  else:
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect(index)
    
def update(request, user_id):
  user = User.objects.get(pk=user_id)
  
  if request.method == 'POST':
    form = UserForm(request.POST, instance=user)
    
    if form.is_valid():
      form.save()
      return redirect(index)
  else:
    form = UserForm(instance=user)
    context = {
      'form': form
    }
    return render(request, 'form.html', context=context)
    
def delete(request, user_id):
  user = User.objects.get(pk=user_id)
  user.delete()
  return redirect(index)
  
def confirm_delete(request, user_id, user_name):
  context = {
    'user_id': user_id,
    'user_name': user_name
  }
  return render(request, 'modal.html', context=context)