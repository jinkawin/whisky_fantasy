from django import forms

from app.tables import Delivery


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = Delivery
        fields = ('name','addressOne','addressTwo','town_city','postcode','phone')
