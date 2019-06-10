from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from company.views import (index,companies, employees,
company,create_Company, update_Company, delete_Company,
create_Employee,update_Employee,delete_Employee)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('employees/', employees ,name='employee_list'),
    
    # path('employees/<id>/', employee, name='employee_detail'),
    path('addemployees/', create_Employee, name='create_employee'),
    path('employees/<id>/update/', update_Employee, name='update_employee'),
    path('employees/<id>/delete/', delete_Employee, name='delete_employee'),



    path('companies/', companies, name='company_list'),
    path('companies/<id>/', company, name='company_detail'),
    path('addcompany/', create_Company, name='create_company'),
    path('companies/<id>/update/', update_Company, name='update_company'),
    path('companies/<id>/delete/', delete_Company, name='delete_company'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)