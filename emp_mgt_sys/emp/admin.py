from django.contrib import admin
from emp.models import emp
class empadmin(admin.ModelAdmin):
      list_display=('emp_photo','first_name','last_name','dob','contact_no','email','address')

admin.site.register(emp,empadmin)
