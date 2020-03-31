from django import forms

from app.tables.PaymentInfo import PaymentInfo


class PaymentForm(forms.ModelForm):

    class Meta:
        model = PaymentInfo
        fields = ('name_card','cardNo','expiryYear','expiryMonth','cvv')
