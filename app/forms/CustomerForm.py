from django import forms
from app.models import Customer

class CustomerForm(forms.ModelForm):
    cust_username = forms.CharField(max_length=10)
    cust_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    cust_email = forms.EmailField()
    cust_fb_id = forms.CharField(max_length=255, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Customer
        fields = ('cust_username', 'cust_password', 'cust_email')