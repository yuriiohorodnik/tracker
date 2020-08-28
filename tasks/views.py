from django.shortcuts import render
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    login_check = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password_field'],
                                    )
            login_check = login(request, new_user)
            if not login_check:
                return render(request, "/", {"login_error": "Something wrong"})
    return render(request, "tasks/projects.html", {"auttth": login_check})


def edit_task(request):
    return render(request, "tasks/edit.html") 


def show_projects(request):
    return render(request, "tasks/projects.html")


def sign_up(request):
    return render(request, "tasks/sign_up.html")


def get_tasks(request):
    return render(request, "tasks/tasks.html")