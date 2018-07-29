from django import forms

class UserRegisterForm(forms.Form):
    '''
    Form definition for user registration
    '''
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )

    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 50
    )

    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 50,
        widget = forms.PasswordInput()
    )