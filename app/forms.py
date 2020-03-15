from django import forms
from django.contrib.auth.models import User

from app.models import UserProfile


class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class MerchantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('role', 'picture',)


class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"Old Password",
        error_messages={'required': u'please input current password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"oldpassword",
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"New Password",
        error_messages={'required': u'please input new password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"Confirm Password",
        error_messages={'required': u'please input again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"password",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"All items are required")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"Two passwords are not identical")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
