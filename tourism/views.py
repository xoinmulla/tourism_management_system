from django.shortcuts import render,redirect
from .models import Destination, Package,Review
from .models import ContactMessage  # Import the model
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        # Save message to database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Send confirmation email (optional)
        send_mail(
            "New Contact Message",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            "your-email@example.com",  # Replace with your email
            ["admin@example.com"],  # Replace with the admin email
            fail_silently=False,
        )

        return redirect("contact")  # Redirect to the same page

    return render(request, "contact.html")

def home(request):
    return render(request, 'home.html')

def packages(request):
    all_packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': all_packages})

def destination(request):
    destination = Destination.objects.all()
    print(destination)  # Debugging line to check data
    return render(request, 'destination.html', {'destination': destination})

def reviews(request):
    reviews_list = Review.objects.all().order_by('-date')  # Fetch all reviews
    return render(request, 'reviews.html', {'reviews': reviews_list})


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm  # We'll create this next

# Register View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Change 'home' to your landing page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View (optional if using Django's built-in one)
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
