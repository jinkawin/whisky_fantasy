import form

from app.tables import Delivery


class DeliveryForm(form.ModelForm):

    class Meta:
        model = Delivery
        fields = '__all__'
