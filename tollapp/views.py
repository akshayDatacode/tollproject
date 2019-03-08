from django.shortcuts import render
from django.db import models
from .models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth.models import User


# Create your views here.

from .forms import *

def TollCmpReg(request):

    form = TollCmpReg_form()
    if request.method == 'POST':
        form = TollCmpReg_form(request.POST)
        if form.is_valid():
            u = form.save()
            p = TollCmpReg_Model.objects.all()

            return render(request, 'display.html', {'p':p})
            #   return HttpResponseRedirect('/display')
        else:
            form_class = TollCmpReg_form()

    return render(request, 'TollCmpReg_Form.html', {
        'form': form,
    })

def TaxpayerReg(request):

    form = TaxpayerReg_form()
    if request.method == 'POST':
        form = TaxpayerReg_form(request.POST)
        if form.is_valid():
            u1 = form.save()
            p1 = TaxpayerReg_Model.objects.all()

            return render(request, 'display.html', {'p1':p1})
            #   return HttpResponseRedirect('/display')
        else:
            form_class = TaxpayerReg_form()

    return render(request, 'TaxpayerReg_Form.html', {
        'form': form,
    })

def display(request):
    p = TollCmpReg_Model.objects.all()

    return render(request, 'display.html', {'p':p})
            
    p1 = TaxpayerReg_Model.objects.all()

    return render(request, 'display.html', {'p1':p1})
  
     

