from django import forms
from django.forms import ModelForm

from catalog.models import Product, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter', 'status')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })

        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })

    def clean(self):
        ban_words = ["казино", "биржа", "обман", "криптовалюта", "дешево",
                     "полиция", "крипта", "бесплатно", "радар"]
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if any(word in name.lower() for word in ban_words):
            self.add_error("name", "Использованы запрещённые слова")

        if any(word in description.lower() for word in ban_words):
            self.add_error("description", "Использованы запрещённые слова")

        return cleaned_data

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price is not None and purchase_price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return purchase_price

