import random
from datetime import datetime, timedelta
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
                return redirect('home')

                # OTP verified, now remove it from session
                request.session.pop("otp", None)
                request.session["otp_sent"] = False

            else:
                messages.error(request, "Invalid OTP. Try again.")
                return redirect('login')

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
        return redirect("register")

def register(request):
    if request.method == 'POST':

        # ---------- SEND OTP ----------
        if 'send_otp' in request.POST:
            phone = request.POST.get("phone", "").strip()
            email = request.POST.get("email", "").strip()
            name = request.POST.get("full_name", "").strip()

            if not phone.isdigit() or len(phone) != 10:
                messages.error(request, "Enter a valid 10-digit number")
                return redirect('register')

            # store data in session
            request.session["reg_phone"] = phone
            request.session["reg_name"] = name
            request.session["reg_email"] = email

            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['otp_sent'] = True

            print(f"OTP for {phone} is : {otp}")
            messages.success(request, 'OTP Sent Successfully')
            return redirect('register')

        # ---------- VERIFY OTP ----------
        elif 'verify_otp' in request.POST:
            entered_otp = request.POST.get('otp', "").strip()

            if str(entered_otp) == str(request.session.get("otp")):
                userprofile.objects.create(
                    phone=request.session["reg_phone"],
                    full_name=request.session["reg_name"],
                    email=request.session["reg_email"],
                )

                # login user
                request.session["phone"] = request.session["reg_phone"]
                request.session["profile_completed"] = True

                # cleanup
                request.session.pop("otp", None)
                request.session.pop("otp_sent", None)

                messages.success(request, "Welcome to NearFix!")
                return redirect("home")

            else:
                messages.error(request, "Invalid OTP")
                return redirect("register")

    return render(request, "register.html")
def profile(request):
    return render(request,'profile.html')
def logout(request):
        request.session.flush()  # removes all session data (phone, OTP, profile_completed)
        return redirect('login')