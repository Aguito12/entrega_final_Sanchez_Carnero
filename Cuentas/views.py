from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import SignUpForm, UserEditForm
from AppCoder.models import Cliente


# Login basado en clase
class LoginView(LoginView):
    template_name = 'Cuentas/login.html'


# Logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Inicio')


# Registro general de usuarios
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()   # acá se crea también el UserProfile automáticamente
            login(request, user)

            # Crear Cliente automáticamente
            Cliente.objects.create(
                nombre=user.first_name,
                email=user.email,
                telefono=form.cleaned_data.get('telefono', '')
            )

            return redirect('Inicio')
    else:
        form = SignUpForm()
    return render(request, 'Cuentas/signup.html', {'form': form})


# Registro de clientes
def signup_cliente_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()   # acá se crea también el UserProfile automáticamente
            login(request, user)

            # Crear Cliente automáticamente
            Cliente.objects.create(
                nombre=user.first_name,
                email=user.email,
                telefono=form.cleaned_data.get('telefono', '')
            )

            return redirect('Inicio')
    else:
        form = SignUpForm()

    return render(request, 'Cuentas/signup_cliente.html', {'form': form})


@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'Cuentas/profile.html', {'profile': profile})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'Cuentas/edit_profile.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self, queryset=None):
        return self.request.user

    def get_initial(self):
        initial = super().get_initial()
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        initial['bio'] = profile.bio
        initial['avatar'] = profile.avatar
        initial['telefono'] = profile.telefono
        initial['birth_date'] = profile.birth_date
        return initial


    def form_valid(self, form):
        response = super().form_valid(form)
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        profile.bio = form.cleaned_data.get('bio', '')
        avatar = form.cleaned_data.get('avatar')
        if avatar:
            profile.avatar = avatar
        profile.telefono = form.cleaned_data.get('telefono', '')
        profile.birth_date = form.cleaned_data.get('birth_date')
        profile.save()
        return response











