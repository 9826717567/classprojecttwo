from django import forms

from App_F.models import User, Post


class User_Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'contact', 'city')

class User_Login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password')

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_description', 'post_status', 'post_image')

