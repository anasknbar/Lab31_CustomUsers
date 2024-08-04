from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
# Create your views here.

def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  return render(request, "users/user.html")
  
def login_view(request):
  if request.method == "POST":
    # Accessing username and password from form data
    # username = request.POST.get("username")
    # password = request.POST.get("password")
    
    username = request.POST["username"]
    password = request.POST["password"]

    # Check if username and password are correct, returning User object if so
    user = authenticate(request, username=username, password=password)

    # If user object is returned, log in and route to index page:
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    # Otherwise, return login page again with new context
    else:
        return render(request, "users/login.html", {
            "message": "Invalid Credentials"
        })
  return render(request, "users/login.html")

def logout_view(request):
  logout(request)
  return render(request,"users/login.html",context={
    'message':'Logged Out'
  })
  

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'users/login.html',context={
              'message': 'sign-up successfully, try to login '})  # Redirect to a success page.
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})