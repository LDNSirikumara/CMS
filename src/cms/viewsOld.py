from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request, *args, **kwargs):
    return render(request, 'index.html', {})

@login_required
def companies(request, *args, **kwargs):
    return render(request, 'companies.html', {})

@login_required
def employees(request, *args, **kwargs):
    return render(request, 'employees.html', {})


