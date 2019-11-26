from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import NewCallForm, ModifyCallForm
from .models import Call

def is_teammember(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 1

@user_passes_test(is_teammember)
def new_call(request):
    if request.method == 'POST':
        form = NewCallForm(request.POST)
        if form.is_valid():
            form.instance.teammember = request.user.teammember
            form.save()

    else:
        form = NewCallForm()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvel Appel",
            'form':form,
        }
    )

@user_passes_test(is_teammember)
def update_calls(request):      
    calls = Call.objects.filter(teammember= request.user.id)
    return render(
        request,
        'calls/update_calls.html',
        {
            'calls_list': calls,
        }
    )

@user_passes_test(is_teammember)
def update_call(request, call_id):             
    call = Call.objects.get(id=call_id)    
    if request.method == 'POST':
        form = ModifyCallForm(request.POST, instance=call)
        if form.is_valid():           
            form.save()
    else:
        form = ModifyCallForm(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': 'title test',
            'form': form,
        }
    )  