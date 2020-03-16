from django import forms
from app.models import Customer

class CustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())
    cust_email = forms.EmailField()
    cust_fb_id = forms.CharField(max_length=255, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Customer
        fields = ('username', 'password', 'cust_email')