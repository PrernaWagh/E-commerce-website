from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='shop/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='shop/logout.html'),name='logout'),
]