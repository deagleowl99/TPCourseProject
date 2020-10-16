from django.urls import path, include
from TP import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
	path('registration', views.create_user, name = 'create_user'),
    path('login', views.login_user, name = 'login_user'),
]