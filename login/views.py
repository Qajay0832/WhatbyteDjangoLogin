from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,"index.html")
def signup(request):
    return render(request,"signup.html")
def login(request):
    return render(request,"login.html")
def forgetPassword(request):
    return render(request,"forgetpass.html")
def resetPassword(request):
    return render(request,"resetpass.html")
def dashboard(request):
    return render(request,"dashboard.html")
def profile(request):
    return render(request,"profile.html")
def changepassword(request):
    return render(request,"changepassword.html")
# def saveUser(request):
#     if request.method=="POST":
#         name=request.POST.get("username")
#         email=request.POST.get("email")
#         password=request.POST.get("password")
#         changepassword=request.POST.get("changepassword")
#         users.save()
#     return render(request,'login.html')