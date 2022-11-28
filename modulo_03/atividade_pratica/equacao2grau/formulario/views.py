from django.shortcuts import render
from .forms import EquacaoForm
from .models import Equacao

def index(request):
    if request.method == 'GET':
        form = EquacaoForm()
        context = {
            'form': form, 
            'result': False
        }
    elif request.method == 'POST':
        modelform = Equacao()
        form = EquacaoForm(request.POST, instance=modelform)
        if form.is_valid():
            uncommitedform = form.save(commit=False)
            uncommitedform.save()
            context = {
                'form': form, 
                'result': uncommitedform
            }
        return render(request, 'form/index.html', context=context)
    else:
        return render(request, 'form/index.html', context=context)