from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import Task



@login_required
def dashboard(request):  # main screen
    return render(request, 'dashboard.html',{'section':'dashboard'})