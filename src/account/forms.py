from django import forms
from account.models import Account
from userprofile.models import Profile
from django.contrib.auth import authenticate


class UserRegisterForm(forms.Form):
    #fields corresponding to User Model
    email           = forms.EmailField(required=True ) 
    name            = forms.CharField(max_length = 30)
    contact         = forms.CharField(max_length = 30)
    image           = forms.ImageField(required=False)
    date_of_birth   = forms.DateField(required = True)
    password1       = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password2       = forms.CharField(max_length=30, widget=forms.PasswordInput)

    #fields corresponding to UserProfile Model
    class Meta:
        fields = ["email", "name" , "contact" , "image" , "date_of_birth" , "password1", "password2"]

    def save(self):
        data = self.cleaned_data
        print(data)
        # What to do next over here?
        if data['password1']==data['password2']:
            if not data['image']:
                print('if wala')
                user = Account.objects.create_user(email=data['email'] , password=data['password1'])
                
                Profile.objects.create(name=data['name'] , contact=data['contact'] ,
                    date_of_birth=data['date_of_birth'] , user=user)
            else:
                print('else wala')
                user = Account.objects.create_user(email=data['email'] , password=data['password1'])
                
                Profile.objects.create(name=data['name'] , contact=data['contact'] ,
                    image=data['image'] ,date_of_birth=data['date_of_birth'] , user=user)



class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label = 'Password ' , widget= forms.PasswordInput)

    class Meta:
        model       = Account
        fields      = ['email' , 'password'] 

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email = email , password = password):
                raise forms.ValidationError("Invalid Login")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["name" ,"contact" , "date_of_birth" , "image"]


    def save(self,commit= True ):
        userProfile                 = self.instance
        userProfile.name            = self.cleaned_data['name']
        userProfile.contact         = self.cleaned_data['contact']
        userProfile.date_of_birth   = self.cleaned_data['date_of_birth']

        
        if self.cleaned_data['image']:
            userProfile.image = self.cleaned_data['image']
        if commit:
            userProfile.save()

        return userProfile

