from django.shortcuts import render,redirect,HttpResponseRedirect
from . import forms,models
from .forms import SignupForm ,LoginForm
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib import messages
import os
from django.contrib.auth.models import auth, User
from django.db.models import Q


# Create your views here.
def index(request):
    search=request.GET.get('search','')
    if search:
        fm = models.Product.objects.filter(Q(Pname__icontains=search) | Q(location__icontains=search))
    else:
        fm=models.Product.objects.all()
    mydict={
        'data':fm,
    }
    return render(request,'index.html',mydict)

# customer signup
def csignup(request):
        fm=forms.SignupForm()
        fm2=forms.SignupForms()
        if request.method == 'POST':
            fm=forms.SignupForm(request.POST)
            fm2=forms.SignupForms(request.POST,request.FILES)
            if fm.is_valid() and fm2.is_valid():
                user=fm.save()
                user.save()
                print(user)
                emp=fm2.save(commit=False)
                emp.user=user
                emp=emp.save()
                messages.success(request, "Account Created Successfully.!!")
                fm=forms.SignupForm()
                fm2=forms.SignupForms()
        else:
            fm=forms.SignupForm()
            fm2=forms.SignupForms()
        mydict={'form':fm,'form2':fm2}
        return render(request, 'signup.html',mydict)

def clogin(request):
        if request.method == "POST":
            fm=forms.LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('Home')
        else:
            fm=forms.LoginForm()
        return render(request, 'Login.html', {'form': fm})

def clogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Home(request):
    if request.user.is_authenticated:
        search=request.GET.get('search','')
        if search:
            fm = models.Product.objects.filter(Q(Pname__icontains=search) | Q(location__icontains=search))
        else:
            fm=models.Product.objects.all()
        mydict={
            'emp':models.Signup.objects.get(user_id=request.user.id),
            'data':fm,
        }
        return render(request,'home.html',mydict)
    else:
        return redirect('login')

# product section start

def add_products(request):
    if request.user.is_authenticated:
        fm = forms.productForm()
       
        if request.method == 'POST':
            fm = forms.productForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Product Added Successfully...')
                fm = forms.productForm()
        else:
            fm = forms.productForm()
        return render(request, 'addproducts.html',{'fm':fm,'emp':models.Signup.objects.get(user_id=request.user.id),})
    else:
        return redirect('login')

def product_list(request):
    if request.user.is_authenticated:
        data = models.Product.objects.all()
        return render(request, 'productlist.html',{'data':data,'emp':models.Signup.objects.get(user_id=request.user.id),})
    else:
        return redirect('login')

def update_product(request,id):
    if request.user.is_authenticated:
        pi=models.Product.objects.get(pk=id)
        if request.method == "POST":
            fm=forms.productForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Product Update Successfully...!!!') 
                
        else:
            pi=models.Product.objects.get(pk=id)
            fm=forms.productForm(instance=pi)
        mydict={
            'fm':fm,
            'emp':models.Signup.objects.get(user_id=request.user.id),
            }
        return render(request, 'editproduct.html',mydict)
    else:
        return redirect('login')


def productDelete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=models.Product.objects.get(pk=id)
            pi.delete()
            return redirect(product_list)
    else:
        return HttpResponseRedirect('/login/')

# product section end

def users(request):
    if request.user.is_authenticated:
        data = models.Signup.objects.all()
        return render(request, 'userview.html',{'data':data,'emp':models.Signup.objects.get(user_id=request.user.id),})
    else:
        return redirect('login')



