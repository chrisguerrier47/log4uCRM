from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    # Get all records and order them by 'updated_at' in descending order (most recent first)
    records = Record.objects.all().order_by('-updated_at')

    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Baby welcome to the party!")
            return redirect('home')
        else:
            messages.error(request, "You are not welcome to the party, please try again...")
            return redirect('home')

    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Joined The Party! Welcome!")
            return redirect('home')
    else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:

        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')
    


from django.contrib import messages
from django.shortcuts import redirect
from .models import Record

def delete_record(request, pk):
    if request.user.is_authenticated:
        # Fetch the record to delete
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        # Set a success message
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        # If the user is not authenticated, show an error message
        messages.error(request, "You must be logged in to delete a record.")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
            messages.success(request, "You must be logged in...")
            return redirect('home')
    
def update_record(request, pk):
     if request.user.is_authenticated:
         current_record = Record.objects.get(id=pk)
         form = AddRecordForm(request.POST or None, instance=current_record)
         if form.is_valid():
             form.save()
             messages.success(request, "Record Has Been Updated!")
             return redirect('home')
         return render(request, 'update_record.html', {'form':form})
     else:
          messages.success(request, "You must be logged in...")
          return redirect('home')
    