from django.db import models

class Company(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField(blank=True)
    logo    = models.ImageField(upload_to='logo',blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={
            'id':self.id
        })

    def get_update_url(self):
        return reversed('update_company', kwargs={
            'id':self.id
        })

    def get_delete_url(self):
        return reversed('delete_company', kwargs={
            'id':self.id
        })
    

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url


class Employee(models.Model):
    f_name    = models.CharField(max_length=20)
    l_name   = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10)
    company    = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.f_name, self.l_name)


    def get_absolute_url(self):
        return reverse('emplyee_detail', kwargs={
            'id':self.id
        })

    def get_update_url(self):
        return reversed('update_emplyee', kwargs={
            'id':self.id
        })

    def get_delete_url(self):
        return reversed('delete_emplyee', kwargs={
            'id':self.id
        })
