from django.shortcuts import render, redirect

def first(request):
    return render(request, 'first.html')
    

def second(request):
    return render(request, 'second.html')
    
def thrid(request):
    return render(request, 'third.html')
    
def firth(request):
    return render(request, 'firth.html')
    

        

    