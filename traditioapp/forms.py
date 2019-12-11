from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile,Songs, Traditonsongs,Post,LatestContact


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'age', 'contact', 'address', 'county']


class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['name', 'description', 'location', 'owner']

class TraditionForm(forms.ModelForm):
    class Meta:
        model = Traditonsongs
        fields = ['name', 'location', 'image']


class LatestForm(forms.ModelForm):
    class Meta:
        model = LatestContact
        fields = ['name', 'contact', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('name', 'county')
