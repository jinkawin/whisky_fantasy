from django import forms

from app.tables.Whisky import Whisky


class ProductForm(forms.ModelForm):
    class Meta:
        model = Whisky
        fields = ('whisky_name', 'whisky_price', 'whisky_quantity', 'whisky_description', 'location', 'whisky_img',
                  'whisky_img_link', 'whisky_status','merchant')
