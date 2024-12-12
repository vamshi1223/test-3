from django.shortcuts import render
from django.contrib.auth import logout
from .models import Feedback, Contact

# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def adminlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email and password match the expected credentials
        if email == 'admin@gmail.com' and password == 'adminstd':
            return redirect('admindashboard')  # Redirect to the admin dashboard
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, './adminportal/adminlogin.html')  # Render the login template

# admindashboard
def admindashboard(request):
    return render (request,"./adminportal/admindashboard.html")

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phonenumber = request.POST.get("phonenumber")
        email = request.POST.get("email")
        yourmessage = request.POST.get("yourmessage")
        
        # Save the data to the Feedback model
        contact_entry = Contact(firstname=firstname, lastname=lastname,phonenumber=phonenumber, email=email, yourmessage=yourmessage)
        contact_entry.save()
    return render (request,"./userportal/contact.html")

def nav(request):
    return render (request,"./userportal/nav.html")

def home(request):
    return render (request,"./userportal/home.html")

def feedback(request):
     if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Save the data to the Feedback model
        feedback_entry = Feedback(name=name, email=email, message=message)
        feedback_entry.save()
     return render(request, "./userportal/feedback.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomUser
import random

def generate_user_id(username):
    # Generate a simple user ID based on username and random number
    user_id = f'{username[:3]}{random.randint(1000, 9999)}'
    return user_id

def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user_id = generate_user_id(username)
        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            full_name=full_name,
            password=password,
        )
        user.save()
        return redirect('login')
    return render(request, './userportal/signup.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or another page after login
        else:
            # Authentication failed
            return render(request, './userportal/userlogin.html', {'error': 'Invalid email or password.'})
    
    return render(request, './userportal/userlogin.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Assuming your CustomUser model has a 'full_name' field
    user_profile = {
        'full_name': request.user.full_name,
        'email': request.user.email,
        # Add more fields as necessary
    }

    return render(request, './userportal/profile.html', {'user_profile': user_profile})



from django.shortcuts import render
from .models import StudentProfile

def student_details_view(request):
    students = StudentProfile.objects.select_related('user').all()
    return render(request, 'student_details.html', {'students': students})


