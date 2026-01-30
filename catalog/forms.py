from django.forms import ModelForm

from catalog.models import Product, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)

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
        cleaned_date = super().clean()
        name = cleaned_date.get("name")
        description = cleaned_date.get("description")

        if any(word in name.lower() for word in ban_words):
            self.add_error("name", "Использованы запрещённые слова")

        if any(word in description.lower() for word in ban_words):
            self.add_error("description", "Использованы запрещённые слова")

    def clean_purchase_price(self):
        cleaned_data = super().clean()
        purchase_price = cleaned_data.get('purchase_price')
        if purchase_price < 0:
            self.add_error('purchase_price', 'Неправильная цена')

