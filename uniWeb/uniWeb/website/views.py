from django.shortcuts import render,redirect
from .models import Members
from .forms import MemberForm

# Create your views here.

def home(request):
    return render(request, 'home.html' , {})

def join(request):

    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        return render(request, 'join.html' , {})
    
def manage(request):
    members = Members.objects.all()
    return render(request, 'manage.html' , {'members': members})


def delete(request, phone):
    try:
        member = Members.objects.get(phone=phone)
        member.delete()
    except Members.DoesNotExist:
        # Member with the specified phone number does not exist
        # You can handle this case, for example, by redirecting to the manage page with a message
        return redirect('manage')

    return redirect('manage')

def update(request,phone):
    member = Members.objects.get(phone=phone)
    return render(request, 'update.html' , {'members': member})


def do_update(request,phone):
    fname=request.POST.get("fname")
    lname=request.POST.get("lname")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    age=request.POST.get("age")

    member = Members.objects.get(phone=phone)

    member.fname= fname  
    member.lname= lname  
    member.email= email  
    member.phone= phone  
    member.age= age

    member.save()

    return redirect('manage')