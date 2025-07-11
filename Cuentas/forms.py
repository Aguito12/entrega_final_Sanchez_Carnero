from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    bio = forms.CharField(widget=forms.Textarea, required=False, label="Biografía")
    avatar = forms.ImageField(required=False, label="Foto de perfil")
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de nacimiento"
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'bio',
            'avatar',
            'birth_date',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

            # Crea o actualiza el perfil
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.bio = self.cleaned_data.get('bio', '')
            profile.avatar = self.cleaned_data.get('avatar') or profile.avatar
            profile.telefono = self.cleaned_data.get('telefono', '')
            profile.birth_date = self.cleaned_data.get('birth_date')
            profile.save()

        return user


class UserEditForm(forms.ModelForm):
    # Campos del perfil
    bio = forms.CharField(widget=forms.Textarea, required=False, label="Biografía")
    avatar = forms.ImageField(required=False, label="Avatar")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=commit)

        # Guardar UserProfile
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.bio = self.cleaned_data.get('bio', '')
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            profile.avatar = avatar
        profile.telefono = self.cleaned_data.get('telefono', '')
        profile.birth_date = self.cleaned_data.get('birth_date')
        profile.save()

        return user

