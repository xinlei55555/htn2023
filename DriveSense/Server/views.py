from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from Server.models import *
import json


# Create your views here.
def login_required(view):
    def updated_view(request):
        try:
            if request.session["logged_in"] == True:
                return view(request)
            else:
                return redirect(login)
        except KeyError:
            return redirect(login)
    return updated_view

def not_logged_in_required(view):
    def updated_view(request):
        try:
            if request.session["logged_in"] == False:
                return view(request)
            else:
                return redirect(homepage)
        except KeyError:
            return view(request)
    
    return updated_view

def create_cookies(view):
    def updated_view(request):
        try:
            request.session['loged_in']
        except:
            request.session['loged_in'] = False
            pass
        
        try:
            request.session['username']
        except:
            request.session['username'] = None
            pass
        return view(request)
    return updated_view

@not_logged_in_required
@create_cookies
def login(request):
    if request.method == 'POST':
        content = json.loads(request.content)
        if Users.objects.filter(username=content['username']):
            if Users.objects.filter(username=content['username']).filter(password=content['password']):
                


@login_required
def index(request):
    return 0
