
from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', views.user_login, name="login"),
    path('signup/', views.register, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('', views.home),
    path('store/', views.store, name='store'),
    path('form/', views.form, name='form'),
    path('collection/', views.collection, name='collection'),
    path('calls/', views.calls, name='calls'),
    path('profile/', views.profile, name='profile'),

]
