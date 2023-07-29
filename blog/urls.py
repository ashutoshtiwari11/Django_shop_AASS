from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.shop ,name='blog'),
    path('signup/',views.signup,name="signup"),
    #  path('shop/', views.shop_view, name='shop'),
    path('about/',views.about),
    path('signin/',views.handlesignin,name="signin"),
    path('login/',views.user_login, name="login"),
    path("logout/",views.user_logout, name='logout'),
    path('contact/',views.contact,name="contact"),
    path('mycart/',views.mycart,name="mycart"),
    path('checkout/',views.checkout, name = "checkout"),
    path('product/<int:myid>',views.productpage,name="product"),
    path('tracker/', views.tracker,name="tracker"),
    path('search/',views.search,name="search")
    
]