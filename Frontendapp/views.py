from django.shortcuts import render, redirect
from Backendapp.models import Categorydb, Productdb
from Frontendapp.models import SignUp, Cartdb
from django.db.models import Sum


def homefun(request):
    return render(request, "Homepage.html")


def category(request):
    data = Categorydb.objects.all()
    return render(request, "Category.html", {'data': data})


def product(request, item):
    product = Productdb.objects.filter(Category=item)
    data = Categorydb.objects.all()
    return render(request, "Category.html", {"data": data, 'product': product})


def singlepro(request, dataid):
    data = Categorydb.objects.all()
    product = Productdb.objects.get(id=dataid)
    return render(request, "singleproduct.html", {"data": data, "product": product})


def userlogin(request):
    return render(request, "Login.html")


def signUpsave(request):
    if request.method == "POST":
        fna = request.POST.get("first")
        sna = request.POST.get("second")
        em = request.POST.get("email")
        nu = request.POST.get("number")
        pa = request.POST.get("password")
        obj = SignUp(FirstName=fna, LastName=sna, Email=em, MobileNumber=nu, Password=pa)
        obj.save()
        return redirect(userlogin)


def logindata(request):
    if request.method == "POST":
        username_d = request.POST.get("username")
        password_d = request.POST.get("password")
        if SignUp.objects.filter(Email=username_d, Password=password_d).exists():
            request.session['username'] = username_d
            request.session['password'] = password_d
            return redirect(homefun)
        else:
            return redirect(userlogin)
    else:
        return redirect(userlogin)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homefun)


def cartfun(request):
    data1 = Categorydb.objects.all()
    data = Cartdb.objects.all()
    # grandtotal = data.aggregate(Sum("Total_Price"))["Total_Price__sum"]
    return render(request, "addtocart.html", {"data": data, "data1": data1})


def cartdbsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('bookprice')
        qut = request.POST.get('quantity')
        obj = Cartdb(Name=na, Price=pr, Quantity=qut)
        obj.save()
        return redirect(cartfun)
