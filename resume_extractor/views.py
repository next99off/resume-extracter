from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def resume(request):
    return render(request, 'resume_extractor/resume.html', {'today':datetime.today()})

# @login_required(login_url="/admin")
# def authorized(request):
#     return render(request, 'home/authorized.html', {})  
