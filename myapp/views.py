from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def youtube(request):
    return render(request,'youtube.html')

def market(request):
    return render(request,'market.html')

def sign(request):
    return render(request,'login.html')
