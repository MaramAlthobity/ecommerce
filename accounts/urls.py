from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name='account-create'),
    path('login/', views.LoginView.as_view(), name='login'),
]