# Profile
from django.http import HttpRequest
from django.shortcuts import render, redirect
from app.models import Profile
from app.forms import ProfilesForm

def profiles_index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/profiles/index.html',
        {
            'profiles': Profile.objects.all()
        }
    )

def profiles_add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = ProfilesForm()
        return render(
            request,
            'app/profiles/add.html',
            {
                'form': form
            }
        )
    else:
        form = ProfilesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/profiles')


def profiles_edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProfilesForm()
        else:
            profile = Profile.objects.get(pk=id)
            form = ProfilesForm(instance=profile)
        return render(
            request,
            'app/profiles/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = ProfilesForm(request.POST)
        else:
            profile = Profile.objects.get(pk=id)
            form = ProfilesForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('/profiles')


def profiles_delete(request, id):
    profile = Profile.objects.get(pk=id)
    profile.delete()
    return redirect('/profiles')