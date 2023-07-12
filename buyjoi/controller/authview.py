import email
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from email import message
from telnetlib import STATUS
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from buyjoi.forms import CustomUserForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib import messages

@csrf_exempt
def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to continue..")
            return redirect('/login')
    context = {
        'form':form
    }
    return render(request, "register.html" , context)


# def loginpage(request):
#     if request.user.is_authenticated:
#         messages.warning(request, "You are already logged in")
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             name = request.POST.get('username')
#             passwd = request.POST.get('password')
#             user = authenticate(request, username=name, password=passwd)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Logged in Successfully..")
#                 return redirect("/")
#             else:
#                 messages.error(request, "Invalid Email or Password")
#                 return redirect("/login")
            
    
#         return render(request, "login.html")

#manav code for login
def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            login_input = request.POST.get('username')  # Assuming the login input field is named 'login_input'
            passwd = request.POST.get('password')

            # Check if the login input is an email
            if '@' in login_input:
                # Authenticate using email
                try:
                    user = User.objects.get(email=login_input)
                    user = authenticate(request, username=user.username, password=passwd)
                except User.DoesNotExist:
                    user = None
            else:
                # Authenticate using username
                user = authenticate(request, username=login_input, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully..")
                return redirect("/")
            else:
                messages.error(request, "Invalid Email or Password")
                return redirect("/login")

        return render(request, "login.html")
    
    
@login_required(login_url='loginpage')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully..")
    
    return render(request, "logout.html")


@login_required(login_url='loginpage')
def account(request):
    if request.user.is_authenticated:
        return render(request, "account.html")
    else:
        messages.error(request, "Kindly login to access this section, Thank you.")
        return redirect("/")


def otp_verify(request):
    # if 'otp' not in request.session:
    #     return redirect('forgotpassword')
    
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        
        if otp_input and stored_otp and otp_input == stored_otp:
            # OTP verification successful
            return redirect('new_password')
        else:
            messages.error(request, "Invalid OTP")
    
    return render(request, 'otp_verify.html')

def new_password(request):
    if 'otp' not in request.session:
        return redirect('forgotpassword')
    
    if request.method == 'POST':
        # Update the user's password
        password = request.POST.get('password')
        user = User.objects.get(email=user.email)
        user.set_password(password)
        user.save()
        
        # Clear OTP from session
        del request.session['otp']
        
        messages.success(request, "Password updated successfully. You can now login with your new password.")
        return redirect('login')
    
    return render(request, 'new_password.html')


def forgotpassword(request):
    if request.method == 'POST':
        login_input = request.POST.get('username')
        if login_input:
            user = None
            if '@' in login_input:
                try:
                    user = User.objects.get(email=login_input)
                except User.DoesNotExist:
                    messages.error(request, "Invalid email ID")
            else:
                try:
                    user = User.objects.get(username=login_input)
                except User.DoesNotExist:
                    messages.error(request, "Invalid mobile number")
            
            if user:
            
            # Generate and send OTP to user
            # otp = generate_otp()  # Implement your own OTP generation logic
            # send_otp_to_user(user, otp)  # Implement your own OTP sending logic
            
            # # Store the OTP in session for verification
            # request.session['otp'] = otp
            
                messages.success(request, "OTP sent successfully")
                return redirect('otp_verify')
        else:
            messages.error(request, "You must enter a mobile number or email")
    
    return render(request, "forgot_password.html")







