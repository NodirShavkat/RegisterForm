from django.shortcuts import render, redirect
from .forms import VolunteerForm

def register_volunteer(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("thanks")
    else:
        form = VolunteerForm()
    return render(request, "registration_form.html", {"form": form})

def thanks(request):
    return render(request, "thanks.html")
