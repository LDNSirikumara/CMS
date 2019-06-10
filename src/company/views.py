from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Company
from .models import Employee
from .forms import CompanyForm, EmployeeForm

@login_required
def index(request, *args, **kwargs):
    querysetC = Company.objects.filter()
    paginatorC = Paginator(querysetC,10)
    page_request_varC = 'page'
    pageC = request.GET.get(page_request_varC)
    try:
        paginatedC_queryset = paginatorC.page(pageC)
    except PageNotAnInteger:
        paginatedC_queryset = paginatorC.page(1)
    except EmptyPage:
        paginatedC_queryset = paginatorC.page(paginatorC.num_pages)


    querysetE =Employee.objects.filter()
    paginatorE = Paginator(querysetE,10)
    page_request_varE = 'page'
    pageE= request.GET.get(page_request_varE)
    try:
        paginatedE_queryset = paginatorE.page(pageE)
    except PageNotAnInteger:
        paginatedE_queryset = paginatorE.page(1)
    except EmptyPage:
        paginatedE_queryset = paginatorE.page(paginatorE.num_pages)

    context={
        'company_list': paginatedC_queryset,
        'page_request_varC':page_request_varC,

        'employee_list': paginatedE_queryset,
        'page_request_varE':page_request_varE,
    }
    return render(request, 'index.html', context)

@login_required
def companies(request, *args, **kwargs):
    querysetC = Company.objects.filter()
    paginatorC = Paginator(querysetC,10)
    page_request_varC = 'page'
    pageC = request.GET.get(page_request_varC)
    try:
        paginatedC_queryset = paginatorC.page(pageC)
    except PageNotAnInteger:
        paginatedC_queryset = paginatorC.page(1)
    except EmptyPage:
        paginatedC_queryset = paginatorC.page(paginatorC.num_pages)

    context={
        'company_list': paginatedC_queryset,
        'page_request_varC':page_request_varC,
    }
    return render(request, 'companies.html', context)

@login_required
def employees(request, *args, **kwargs):
    querysetE =Employee.objects.filter()
    paginatorE = Paginator(querysetE,10)
    page_request_varE = 'page'
    pageE= request.GET.get(page_request_varE)
    try:
        paginatedE_queryset = paginatorE.page(pageE)
    except PageNotAnInteger:
        paginatedE_queryset = paginatorE.page(1)
    except EmptyPage:
        paginatedE_queryset = paginatorE.page(paginatorE.num_pages)

    context={
        'employee_list': paginatedE_queryset,
        'page_request_varE':page_request_varE,
    }
    return render(request, 'employees.html', context)

# Company def----------------------------------------------------------------

def create_Company(request):
    title = 'Add'
    form = CompanyForm(request.POST or None, request.FILES or None)
    if request.method =="POST":
        if form.is_valid(): 
            form.save()
            # return redirect(reverse('company_list', kwargs={
            #     'id': form.instance.id
            # }))
            return redirect(reverse('company_list'))
            
    return render(request,"create_company.html", {'form':form, 'title':title})

def update_Company(request,id):
    title = 'Update'
    company = get_object_or_404(Company, id = id)
    form = CompanyForm(
        request.POST or None, 
        request.FILES or None, 
        instance=company)

    if request.method =="POST":
        if form.is_valid(): 
            form.save()

            return redirect(reverse('company_list'))
            
    return render(request,"create_company.html", {'form':form, 'title':title})

def delete_Company(request,id):
    company = get_object_or_404(Company, id = id)
    company.delete()
    return redirect(reverse('company_list'))


def company(request, id):
    company= get_object_or_404(Company, id=id)
    context={
        'company':company,
    }
    return render(request, 'company.html',context)


# Employee def----------------------------------------------------------------

def create_Employee(request):
    title = 'Add'
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if request.method =="POST":
        if form.is_valid(): 
            form.save()
            return redirect(reverse('employee_list'))
            
    return render(request,"create_employee.html", {'form':form, 'title':title})

def update_Employee(request,id):
    title = 'Update'
    employee = get_object_or_404(Employee, id = id)
    form = EmployeeForm(
        request.POST or None, 
        request.FILES or None, 
        instance=employee)

    if request.method =="POST":
        if form.is_valid(): 
            form.save()

            return redirect(reverse('employee_list'))
            
    return render(request,"create_employee.html", {'form':form, 'title':title})

def delete_Employee(request,id):
    employee = get_object_or_404(Employee, id = id)
    employee.delete()
    return redirect(reverse('employee_list'))


# def employee(request, id):
#     employee= get_object_or_404(Employee, id=id)
#     context={
#         'employee':employee,
#     }
#     return render(request, 'employee.html',context)
