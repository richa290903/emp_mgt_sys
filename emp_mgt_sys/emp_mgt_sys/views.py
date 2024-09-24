from django.shortcuts import render,redirect,get_object_or_404
from emp.models import emp
from django.contrib import messages


def home(request):
      return render(request,"home.html")

def table(request):
      data={}
      empdata = emp.objects.all()  
      try:
            if request.method=="POST":
                  emp_photo=emp(request.POST,request.FILES)
                  emp_photo = request.FILES.get('emp_photo') 
                  fn=request.POST.get('fn')
                  ln=request.POST.get('ln')
                  dob=request.POST.get('dob')
                  cn=request.POST.get('cn')
                  ea=request.POST.get('ea')
                  ra=request.POST.get('ra')
                  insertquery=emp(emp_photo=emp_photo,first_name=fn,last_name=ln,dob=dob,contact_no=cn,email=ea,address=ra)
                  insertquery.save()
                  messages.success(request, 'Employee inserted Successfully.')
                  empdata=emp.objects.all()
                  

            if request.method == "GET":
                  search = request.GET.get('search')
                  if search:
                        from django.db.models import Q
                        empdata = emp.objects.filter(
                              Q(first_name__icontains=search) |
                              Q(last_name__icontains=search) |
                              Q(id__icontains=search) |
                              Q(dob__icontains=search)
                        )
                  if not empdata.exists():
                        s = "No Data Found......."
            else:
                  s = "No search term provided."
            data={'empdata':empdata}

      except Exception as e:
            messages.error(request, f"Data Insert error: {e}")
            messages.error(request, f"Data display error: {e}")

      return render(request,"table1.html",{'empdata':empdata})

def delete(request,id):
      try:
            deletequery=emp.objects.get(id=id)
            deletequery.delete()
            messages.success(request,"Data Deleted Successfully")
      except Exception as e:
            messages.error(request,f"Data Delete error:{e}")
      return redirect('/table')

def edit(request,id):
      try:
            empdata = get_object_or_404(emp, id=id)
            if request.method == 'POST':
                  empdata.emp_photo=emp(request.POST,request.FILES)
                  empdata.emp_photo = request.FILES.get('emp_photo') 
                  empdata.first_name = request.POST.get('first_name')
                  empdata.last_name = request.POST.get('last_name')
                  empdata.dob=request.POST.get('dob')
                  empdata.contact_no=request.POST.get('cn')
                  empdata.email=request.POST.get('ea')
                  empdata.address=request.POST.get('ra')
                  empdata.save()  
                  messages.success(request, 'Employee Updated Successfully.')
                  return redirect('/table')    
      except Exception as e:
            messages.error(request,f"Data Update error:{e}")     
      return render(request,'update.html',{'emp':empdata})

