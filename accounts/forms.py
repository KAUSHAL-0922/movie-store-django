from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([
            f'<div class="alert alert-danger mt-2" role="alert">{e}</div>' for e in self
        ]))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    
# class UserRegistrationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserRegistrationForm, self).__init__(*args,**kwargs)
        
#         for fieldname in ['username','email' ,'password1', 'password2']:
            
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update(
#               {'class': 'form-control'})
            
#     email = forms.EmailField(required=True)
#     user_type = forms.ChoiceField(choices=user_constants.USER_TYPE_CHOICES, required=True)
    
#     class Meta:
#         model = User
#         fields = ['username','email', 'user_type', 'password1', 'password2']
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.user_type = self.cleaned_data['user_type']
#         if commit:
#             user.save()
#         return user

