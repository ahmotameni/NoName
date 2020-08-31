from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from NoNameApp.forms import SignUpForm


@login_required
def vote(request):
    return HttpResponse('Vote')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.sex = form.cleaned_data.get('sex')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponse('Done!')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
