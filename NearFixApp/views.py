import random
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userprofile
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userprofile

def login(request):
    otp_sent = False

    if request.method == "POST":

        # Send OTP button
        if "send_otp" in request.POST:
            phone = request.POST.get("phone", "").strip()
            if not phone.isdigit() or len(phone) != 10:
                messages.error(request, "Enter a valid 10-digit phone number.")
            else:
                otp = random.randint(1000, 9999)
                request.session["otp"] = otp
                request.session["phone"] = phone
                request.session["otp_sent"] = True
                otp_sent = True

                print(f"OTP for {phone}: {otp}")  
                messages.success(request, "OTP sent")

        # Verify OTP button
        elif "verify_otp" in request.POST:
            entered_otp = request.POST.get("otp", "").strip()
            otp_sent = True

            phone = request.session.get("phone")  # ✅ get phone from session

            if "otp" in request.session and str(entered_otp) == str(request.session.get("otp")):
                messages.success(request, "OTP verified successfully!")

                # OTP verified, now remove it from session
                request.session.pop("otp", None)
                request.session["otp_sent"] = False

                # Check if profile exists
                if userprofile.objects.filter(phone=phone).exists():
                    request.session['profile_completed'] = True
                    return redirect('home')  # ✅ returning user goes home
                else:
                    request.session['profile_completed'] = False
                    return redirect('register')  # ✅ first-time user goes to profile

            else:
                messages.error(request, "Invalid OTP. Try again.")

    else:
        request.session["otp_sent"] = False

    context = {
        "phone": request.session.get("phone", ""),
        "otp_sent": request.session.get("otp_sent", False)
    }
    return render(request, "login.html", context)



def home(request):
     phone = request.session.get("phone")  # get phone of logged-in user
     profile = None
     if phone:
        profile = userprofile.objects.filter(phone=phone).first()  # fetch profile
        return render(request, "home.html", {"profile": profile})
     else:
        # If no phone in session, redirect to login
        return redirect("login")

def register(request):
     phone = request.session.get("phone")
     if not phone:
        return redirect("login")
     if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        
        userprofile.objects.create(
            phone=phone,
            full_name=full_name,
            email=email,
        )
        request.session["profile_completed"] = True
        return redirect('home')

     return render(request, "register.html")
def profile(request):
    return render(request,profile.html)
def logout(request):
        request.session.flush()  # removes all session data (phone, OTP, profile_completed)
        return redirect('login')