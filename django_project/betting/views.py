from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'betting/home.html')

@login_required
def about(request):
    return render(request, 'betting/about.html')
