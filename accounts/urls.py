from django.contrib import admin
from django.urls import path, include

# Import views directly from the app
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('analysis/', views.analysis_view, name='analysis'),
    path('personal/', views.personal_view, name='personal')

    # Use analysis_view
]
