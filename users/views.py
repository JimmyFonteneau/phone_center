from django.shortcuts import render
from django.http import HttpResponse

# View.
def hello_old(request):
    print("Bonjour")
    # return HttpResponse("Hello word!")
    return JsonResponse({ 'message': 'hello worold' })

def hello(request):
    return render (
        request,
        'users/hello.html',
        {
            'message': "Hello world"
        }
    )