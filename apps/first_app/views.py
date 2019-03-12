from django.shortcuts import render, HttpResponse

#def index(request):
    #return HttpResponse("climate")

def index(request):
    return render(request, 'first_app/main.html')
