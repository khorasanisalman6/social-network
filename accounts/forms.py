from django import forms

from accounts.models import User, Profile


class UserRegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Enter Confirm Password'}), label="Confirm Password")
    class Meta:
        model = User
        fields = ('username', 'email' , 'first_name', 'last_name' , 'password','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter Last Name'}),
            'password': forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Enter Password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) , label="Username Or Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}) ,
            'email': forms.EmailInput(attrs={'class':'form-control'}) ,
            'first_name': forms.TextInput(attrs={'class':'form-control'}) ,
            'last_name': forms.TextInput(attrs={'class':'form-control'})
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio', 'age', 'address')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}) ,
            'bio': forms.TextInput(attrs={'class':'form-control'}) ,
            'age': forms.TextInput(attrs={'class':'form-control'}) ,
            'address': forms.TextInput(attrs={'class':'form-control'}) ,
        }