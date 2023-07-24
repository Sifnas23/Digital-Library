from django.urls import path
from Frontendapp import views

urlpatterns = [
    path('', views.homefun, name="homefun"),
    path('category/', views.category, name="category"),
    path('product/<item>', views.product, name="product"),
    path('singlepro/<int:dataid>', views.singlepro, name="singlepro"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('signUpsave/', views.signUpsave, name="signUpsave"),
    path('logindata/', views.logindata, name="logindata"),
    path('logout/', views.logout, name="logout"),
    path('cartfun/', views.cartfun, name="cartfun"),
    path('cartdbsave/', views.cartdbsave, name="cartdbsave")
]
