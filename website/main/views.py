from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsUpdateView(UpdateView):
    model = Military
    template_name = 'main/create.html'

    fields = ['number','dislocation','type_troops','companies']

class NewsDeleteView(DeleteView):
    model = Military
    success_url='/military'
    template_name = 'main/delete.html'

class NewsDeleteView2(DeleteView):
    model = Type_troop
    success_url='/type_troops'
    template_name = 'main/delete.html'

class NewsDeleteView3(DeleteView):
    model = Companies
    success_url='/companies'
    template_name = 'main/delete.html'

class NewsDeleteView4(DeleteView):
    model = Employees
    success_url='/employees'
    template_name = 'main/delete.html'

class NewsDeleteView5(DeleteView):
    model = Dislocatio
    success_url='/dislocation'
    template_name = 'main/delete.html'


class NewsUpdateView2(UpdateView):
    model = Type_troop
    template_name = 'main/create2.html'

    fields = ['title']



class NewsUpdateView3(UpdateView):
    model = Companies
    template_name = 'main/create3.html'

    fields = ['title','number_employees']



class NewsUpdateView4(UpdateView):
    model = Employees
    template_name = 'main/create4.html'

    fields = ['fist_name','companies','post','year_birth','year_enlistment','length_service','honors','military_activies']



class NewsUpdateView5(UpdateView):
    model = Dislocatio
    template_name = 'main/create5.html'

    fields = ['country','city','address','squar']





class NewsDetailView(DetailView):
    model = Military
    template_name = 'main/details_view.html'
    context_object_name = 'military'

class NewsDetailView2(DetailView):
    model = Type_troop
    template_name = 'main/details_view2.html'
    context_object_name = 'type_troops'

class NewsDetailView3(DetailView):
    model = Companies
    template_name = 'main/details_view3.html'
    context_object_name = 'companies'

class NewsDetailView4(DetailView):
    model = Employees
    template_name = 'main/details_view4.html'
    context_object_name = 'employees'

class NewsDetailView5(DetailView):
    model = Dislocatio
    template_name = 'main/details_view5.html'
    context_object_name = 'dislocation'


def index(request):
    return render(request, 'main/index.html',)

def military(request):
    me = Military.objects.all()
    return render(request, 'main/template1.html',{'me':me})

def type_troops(request):
    ty = Type_troop.objects.all()
    return render(request, 'main/template2.html',{'ty':ty})

def companies(request):
    co=Companies.objects.all()
    return render(request, 'main/template3.html',{'co':co})

def employees(request):
    em=Employees.objects.all()
    return render(request, 'main/template4.html',{'em':em})

def dislocation(request):
    di=Dislocatio.objects.all()
    return render(request, 'main/template5.html',{'di':di})

def create(request):
    error=''
    if request.method == 'POST':
        form = MilitaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('military')
        else:
            error="Форма была не верной"
    form= MilitaryForm()

    data= {
       'form': form,
        'error':error
    }
    return render(request, 'main/create.html', data)

def create2(request):
    error=''
    if request.method == 'POST':
        form = Type_troopsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_troops')
        else:
            error="Форма была не верной"
    form= Type_troopsForm()

    data= {
       'form': form,
        'error':error
    }
    return render(request, 'main/create2.html',data)

def create3(request):
    error=''
    if request.method == 'POST':
        form = CompaniesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies')
        else:
            error="Форма была не верной"
    form= CompaniesForm()

    data= {
       'form': form,
        'error':error
    }
    return render(request, 'main/create3.html',data)

def create4(request):
    error=''
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            error="Форма была не верной"
    form= EmployeesForm()

    data= {
       'form': form,
        'error':error
    }
    return render(request, 'main/create4.html',data)

def create5(request):
    error=''
    if request.method == 'POST':
        form = DislocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dislocation')
        else:
            error="Форма была не верной"
    form = DislocationForm()
    data= {
       'form': form,
        'error':error
    }
    return render(request, 'main/create5.html',data)