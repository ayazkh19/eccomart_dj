from django import forms


# these are django built in form classes
# provide convenience for creating and validation user data
# this form class is imported in views
# and then pass to relevant templates where they need to be displayed

# responsible registration form
class CustomerRegistrationForm(forms.Form):
    email_field = forms.EmailField(label='',
                                   max_length=100,
                                   required=False,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control mb-2',
                                       'placeholder': 'Email'}))
    password_field = forms.CharField(label='',
                                     max_length='20',
                                     widget=forms.PasswordInput(attrs={
                                         'class': 'form-control mb-2',
                                         'placeholder': 'Password'}),
                                     required=False)
    confirm_password_field = forms.CharField(label='',
                                             max_length='20',
                                             widget=forms.PasswordInput(attrs={
                                                 'class': 'form-control mb-2',
                                                 'placeholder': 'Confirm Password'}),
                                             required=False)

    # validation rules
    def clean(self):
        # supper is called on the parent class from which this form is inherited
        cleaned_data = super().clean()
        email = str(cleaned_data.get('email_field'))
        password = str(cleaned_data.get('password_field'))
        confirm_password = str(cleaned_data.get('confirm_password_field'))

        if len(email) < 1:
            raise forms.ValidationError('Email is required')
        if len(password) < 1:
            raise forms.ValidationError('password is required')
        if password != confirm_password:
            raise forms.ValidationError('password does not match')


# responsible for login form
class CustomerLoginForm(forms.Form):
    email_field = forms.EmailField(label='',
                                   max_length=100,
                                   required=False,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control mb-2',
                                       'placeholder': 'Email'}))
    password_field = forms.CharField(label='',
                                     max_length='20',
                                     widget=forms.PasswordInput(attrs={
                                         'class': 'form-control mb-2',
                                         'placeholder': 'Password'}),
                                     required=False)


