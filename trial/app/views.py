from django.shortcuts import render
from app.models import UserRegistrationModel

# Create your views here.

def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = UserRegistrationModel.objects.create(user_name=username, password=password)

    return render(request, "project1.html")