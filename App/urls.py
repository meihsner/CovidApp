from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from covid.views import user_registration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', user_registration, name='register'),
    path('covid/', include('covid.urls'))
]
