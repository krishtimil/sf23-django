import json
from django.shortcuts import render, redirect
from ExpenseTracker.forms import ExpenseForm
from ExpenseTracker.helper_functions import *
from ExpenseTracker.models import ExpenseRecord
# Create your views here.

def dashboard(request):
    records = ExpenseRecord.objects.all().values()
    context = {}
    for i, data in enumerate(get_data()):
        context[f"{fields[i]}"] = data
    
    return render(request, "ExpenseTracker/dashboard.html", {'records':records, "data_json":json.dumps(context)})

def add_expense(request):
    context = {}
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard)
        
    form = ExpenseForm()
    context['form'] = form
    return render(request, "ExpenseTracker/add_expense.html", context)