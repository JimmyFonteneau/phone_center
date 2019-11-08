from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# View.
def hello(request):
    print("Bonjour")
    # return HttpResponse("Hello word!")
    return JsonResponse({ 'message': 'hello' })