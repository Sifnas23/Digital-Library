from django.shortcuts import render, redirect
from Backendapp.models import Categorydb, Productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def indexfun(request):
    return render(request, "index.html")


def addcategory(request):
    return render(request, "AddCategory.html")


def Categorydbsave(request):
    if request.method == "POST":
        na = request.POST.get('category')
        de = request.POST.get('description')
        obj = Categorydb(Name=na, Desc=de)
        obj.save()
        return redirect(addcategory)


def displaycategorydata(request):
    data = Categorydb.objects.all()
    return render(request, "displaycategory.html", {"data": data})


def editcategory(request, dataid):
    data = Categorydb.objects.get(id=dataid)
    print(data)
    return render(request, "Editcategory.html", {"data": data})


def updatecategory(request, dataid):
    if request.method == "POST":
        na = request.POST.get('category')
        de = request.POST.get('description')

        Categorydb.objects.filter(id=dataid).update(Name=na, Desc=de)
        return redirect(displaycategorydata)


def delcategory(request, dataid):
    data = Categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategorydata)


def addproduct(request):
    data = Categorydb.objects.all()
    return render(request, "AddProduct.html", {"data": data})


def Productdbsave(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        pro = request.POST.get('product')
        pri = request.POST.get('price')
        de = request.POST.get('description')
        im = request.FILES['image']
        obj = Productdb(Category=cat, Product=pro, Price=pri, Description=de, Image=im)
        obj.save()
        return redirect(addproduct)


def displayproductdata(request):
    data = Productdb.objects.all()
    return render(request, "displayproduct.html", {"data": data})


def editproduct(request, dataid):
    data = Productdb.objects.get(id=dataid)
    da = Categorydb.objects.all()
    print(data)
    return render(request, "Editproduct.html", {"data": data, "da": da})


def updateproduct(request, dataid):
    if request.method == "POST":
        cat = request.POST.get('category')
        pro = request.POST.get('product')
        pri = request.POST.get('price')
        de = request.POST.get('description')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
        Productdb.objects.filter(id=dataid).update(Category=cat, Product=pro, Price=pri, Description=de, Image=file)
        return redirect(displayproductdata)


def delproduct(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproductdata)


def loginpage(request):
    return render(request, "LoginPage.html")


def adminloginfun(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexfun)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def adminlogoutfun(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
