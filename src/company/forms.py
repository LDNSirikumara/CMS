from django import forms
from .models import Company
from .models import Employee

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields= ('name','email','logo','website')

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields= ('f_name','l_name','company','email','phone')