from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'special'})
        self.fields['password'].widget.attrs.update(size='40')    
        # widget= forms.TextInput(attrs=
        # {
        #     'class':'loginform',
        #     'id':'loginform',
        #     'placeholder':"Password"
        # })
    # )
    
    # widget= forms.PasswordInput(attrs={'placeholder':"Phone, email, or username"})

    # widget=forms.TextInput(attrs={'placeholder':'Phone, email, or username'})


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        # sale_date = forms.DateField(widget=forms.DateInput(format='%M%d%Y'),input_formats=['%M%d%Y'], label=('Date of birth:'))

        fields = ('date_of_birth', 'photo')


# class CouponApplyForm(forms.Form):
    # code = forms.CharField(label=_('Coupon'))
