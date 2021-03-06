from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Required. Enter Your First Name.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Required. Enter Your Last Name.')
    email = forms.EmailField(max_length=150, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class ProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, help_text='Required. Enter Your First Name.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Required. Enter Your Last Name.')
    email = forms.EmailField(max_length=150, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


    def __str__(self):
        return self.user.username