from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect

from .forms import NewCallForm, ModifyCallForm, CustomerCallForm, CustomerModifyCallForm, CustomerModifyCallFormSolved, ModifyCallFormTeamMember
from .models import Call

def is_teammember(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 1

def is_customer(user=None):    
    if user == None:
        return false   
    return user.is_customer

def is_superuser(user=None):    
    if user == None:
        return false   
    return user.is_superuser

# Methods pour les teammember

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

@user_passes_test(is_teammember)
def calls_free(request):      
    calls = Call.objects.filter(teammember=None)
    return render(
        request,
        'calls/calls_free.html',
        {
            'calls_list': calls,
        }
    )

@user_passes_test(is_teammember)
def update_teammember(request, call_id):      
    call = Call.objects.get(id=call_id) 
    if request.method == 'POST':
        form = ModifyCallFormTeamMember(request.POST, instance=call)
        if form.is_valid():           
            form.save()
            return HttpResponseRedirect(reverse("calls:calls_free"))
    else:
        form = ModifyCallFormTeamMember(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': 'Modifier l\'appel',
            'form': form,
        }
    )

# créer un nouveau call

@user_passes_test(is_customer)
def customer_new_call(request):
    if request.method == 'POST':
        form = CustomerCallForm(request.POST)      
        if form.is_valid():            
            form.instance.customer = request.user.customer
            form.save()
            return HttpResponseRedirect(reverse("calls:customer_my_calls"))       

    else:
        form = CustomerCallForm()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvel Appel",
            'form':form,
        }
    )

# Méthodes liés aux calls unsolved

@user_passes_test(is_customer)
def customer_my_calls_unsolved(request):          
    calls = Call.objects.filter(customer= request.user.id, solved= False)        
    return render(
        request,
        'calls/customer_view_calls.html',
        {
            'calls_list': calls
        }
    )

@user_passes_test(is_customer)
def customer_update_unresolve_call(request, call_id):
    call = Call.objects.get(id=call_id) 
    if request.method == 'POST':
        form = CustomerModifyCallForm(request.POST, instance=call)
        if form.is_valid():           
            form.save()
            return HttpResponseRedirect(reverse("calls:customer_my_calls_unsolved"))
    else:
        form = CustomerModifyCallForm(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': 'Modifier l\'appel',
            'form': form,
        }
    ) 

# Méthodes liés aux calls solved

@user_passes_test(is_customer)
def customer_my_calls_solved(request):          
    calls = Call.objects.filter(customer= request.user.id, solved= True)        
    return render(
        request,
        'calls/customer_view_calls_solved.html',
        {
            'calls_list': calls
        }
    )

@user_passes_test(is_customer)
def customer_update_resolved_call(request, call_id):
    call = Call.objects.get(id=call_id) 
    if request.method == 'POST':
        form = CustomerModifyCallFormSolved(request.POST, instance=call)
        if form.is_valid():           
            form.save()
            return HttpResponseRedirect(reverse("calls:customer_my_calls_solved"))
    else:
        form = CustomerModifyCallFormSolved(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': 'Modifier l\'appel',
            'form': form,
        }
    )


# super user Calls inférieur à 6 

@user_passes_test(is_superuser)
def calls_under_six(request):          
    calls = Call.objects.filter(note__lte = 6)        
    return render(
        request,
        'calls/under_six.html',
        {
            'calls_list': calls
        }
    )