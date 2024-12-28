
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from hospitalapp.models import Department,User,Doctors,Patient
from django.contrib.auth import authenticate,login,logout
from .models import Booking
from .forms import BookingForm
# Create your views here.
def addD(request):
    
    if request.method=="GET":
      return render(request,'addD.html')
    elif request.method=="POST":
       dep=request.POST['department']
       x=Department.objects.create(Dep_Name=dep)
       x.save()
       return HttpResponse("<script>alert('added successfully');</script>")
def adminhome(request):
   return render(request,'adminH.html')
   
def doctorreg(request):
   if request.method=="GET":
      data=Department.objects.all()
      return render(request,'dreg.html',{'data1':data})
   elif request.method=="POST":
      f=request.POST['fname']
      l=request.POST['lname']
      u=request.POST['uname']
      p=request.POST['pass']
      e=request.POST['email']
      a=request.POST['add']
      ph=request.POST['phone']
      q=request.POST['qual']
      d=request.POST['dep']
      x=User.objects.create_user(first_name=f,last_name=l,username=u,password=p,email=e,usertype='doctor')
      x.save()
      y=Doctors.objects.create(user_id=x,Dep_id_id=d,Address=a,Phoneno=ph,Qualifications=q)
      y.save()
      return HttpResponse("<script>alert('successfully registerd');</script>")
def homeH(request):
   return render(request,'homeh.html')
def patientreg(request):
   if request.method=="GET":
      
      return render(request,'patientreg.html')
   
   elif request.method=="POST":
      f=request.POST['fname']
      l=request.POST['lname']
      u=request.POST['uname']
      p=request.POST['pass']
      e=request.POST['email']
      ag=request.POST['age']
      a=request.POST['add']
      ph=request.POST['phone']
      
      x=User.objects.create_user(first_name=f,last_name=l,username=u,password=p,email=e,usertype='patient',is_active=True)
      x.save()
      y=Patient.objects.create(user_id=x,Age=ag,Address=a,Phone=ph)
      y.save()
      return HttpResponse("<script>alert('Registraton successful');</script>")
def loginh(request):
    if request.method=="GET":
        return render(request,'loginsh.html')
    elif request.method=="POST":
        un=request.POST['uname']
        ps=request.POST['pass']
        print(un,ps)
        user=authenticate(request,username=un,password=ps)
        if user is not None and user.usertype=="doctor":
            login(request,user)
            request.session['doc_id']=user.id 
            return redirect(doctorhome)
        elif user is not None and user.usertype=="patient" and user.is_active==1:
            login(request,user)
            request.session['pat_id']=user.id
            return redirect(patienthome)
        elif user is not None and user.is_superuser==1:
            return redirect(adminhome)    
        else:
            return HttpResponse("<script>alert('Invalid Username or Password');</script>")
    return HttpResponse("not ok")
def doctorhome(request):
    return render(request,'doctorhome.html')
def patienthome(request):
    return render(request,'patienthome.html')
def lgout(request):
   logout(request)
   return redirect(loginh)
def updateprofiledr(request):
   doct=request.session.get('doc_id')
   dr=Doctors.objects.get(user_id_id=doct)
   uss=User.objects.get(id=doct)
   return render(request,'updateprdr.html',{'view':dr,'data':uss})
def update_Doctors(request,uid):
   if request.method=="POST":
      doct=Doctors.objects.get(id=uid)
      tid=doct.user_id_id
      user=User.objects.get(id=tid)
      user.first_name=request.POST['first_name']
      user.last_name=request.POST['last_name']
      user.email=request.POST['email']
      user.save()
      doct.Address=request.POST['address']
      doct.Phoneno=request.POST['phone']
      doct.Qualifications=request.POST['qual']
      doct.save()
      return HttpResponse("Success")
def updateprofilep(request):
   pat=request.session.get('pat_id')
   st=Patient.objects.get(user_id_id=pat)
   us=User.objects.get(id=pat)
   return render(request,'updateprpat.html',{'view':st,'data':us})
def update_patient(request,uid):
   if request.method=="POST":
      stud=Patient.objects.get(id=uid)
      sid=stud.user_id_id
      user=User.objects.get(id=sid)
      user.first_name=request.POST['first_name']
      user.last_name=request.POST['last_name']
      user.email=request.POST['email']
      user.save()
      stud.Address=request.POST['address']
      stud.Phone=request.POST['phone']
      stud.Age=request.POST['age']

      stud.save()
      return HttpResponse("Success")
def create_or_update_booking(request, booking_id=None):
    patient = get_object_or_404(Patient, user_id=request.user)  # Assuming the logged-in user is a patient

    if booking_id:
        # Editing an existing booking
        booking = get_object_or_404(Booking, id=booking_id, patient=patient)
    else:
        # Creating a new booking
        booking = None

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.patient = patient
            booking.save()
            return HttpResponse("Booking Successful")
    else:
        form = BookingForm(instance=booking)

    return render(request, 'create_booking.html', {'form': form, 'booking': booking})
def list_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'list_bookings.html', {'bookings': bookings})

def approve_booking(request, booking_id):
    # Retrieve the booking object
    bookings = get_object_or_404(Booking, id=booking_id)
    
    # Set the 'approved' field to True
    bookings.approved = True
    
    # Save the booking object
    bookings.save()
    
    # Redirect to the list of bookings
    return redirect(list_bookings)
def approved_bookings(request):
    approved_bookings = Booking.objects.filter(approved=True)
    return render(request, 'approved_bookings.html', {'bookings': approved_bookings})
def dview(request):
    data1 = Doctors.objects.all()  # Fetch all doctors' data
    return render(request, 'drview.html', {'data1': data1})  # Pass the data to the template
# views.py
def view_bookings_by_doctor(request):
    # Fetch all doctors
    doctors = Doctors.objects.all()

    # Create a dictionary to store bookings by doctor
    bookings_by_doctor = {}
    for doctor in doctors:
        bookings = Booking.objects.filter(doctor=doctor)
        bookings_by_doctor[doctor] = bookings

    return render(request, 'bookings_by_doctor.html', {'bookings_by_doctor': bookings_by_doctor})


