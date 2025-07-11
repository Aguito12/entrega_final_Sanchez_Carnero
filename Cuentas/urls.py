from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(next_page='Inicio'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/editar/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('signup_cliente/', views.signup_cliente_view, name='signup_cliente'),
]



