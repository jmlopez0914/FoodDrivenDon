from django.shortcuts import render
from django.http import HttpResponse
from .models import Registrant, Question

# Create your views here.
def index(request):
    return render(request, "Registration/index.html")

def about(request):
    return render(request, "Registration/about.html")

def addRegistrant(request):
    return render(request, "Registration/volunteerRegistry.html")

def addRegistrant_Submission(request):
    print("Hello form is submitted.")
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    home_address = request.POST["home_address"]
    city = request.POST["city"]
    state = request.POST["state"]
    pickup_date = request.POST["pickup_date"]

    registrant_info = Registrant(full_name=full_name, email=email, home_Address=home_address,
                                city=city, state=state, pickup_date=pickup_date)

    registrant_info.save()

    return render(request, "Registration/form_complete.html")


def addQuestion(request):
    print("Question is submitted")
    question = request.POST["question"]
    email = request.POST["question_email"]

    question_info = Question(email = email, question = question)
    question_info.save()

    return render(request, "Registration/form_complete.html")
