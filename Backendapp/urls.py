from django.urls import path
from Backendapp import views

urlpatterns = [
    path('', views.indexfun, name="indexfun"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('Categorydbsave/', views.Categorydbsave, name="Categorydbsave"),
    path('Productdbsave/', views.Productdbsave, name="Productdbsave"),
    path('displaycategorydata/', views.displaycategorydata, name="displaycategorydata"),
    path('displayproductdata/', views.displayproductdata, name="displayproductdata"),
    path('editcategory/<int:dataid>', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('delcategory/<int:dataid>', views.delcategory, name="delcategory"),
    path('editproduct/<int:dataid>', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>', views.updateproduct, name="updateproduct"),
    path('delproduct/<int:dataid>', views.delproduct, name="delproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminloginfun/', views.adminloginfun, name="adminloginfun"),
    path('adminlogoutfun/', views.adminlogoutfun, name="adminlogoutfun")
]
