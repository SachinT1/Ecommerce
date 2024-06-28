from django import forms
from .models import *
from django.core.exceptions import ValidationError

INPUT_CLASSES='w-1/2 py-4 px-6 rounded-xl border'

class NewCatForm(forms.ModelForm):
    """class Meta:
        model=Category
        fields = ('name',)
        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
        }"""
    class Meta:
        model = Category
        fields=('name',)
        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
        }

    name = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data= super(NewCatForm,self).clean()
        catname = cleaned_data.get('name')
        if validate_text(catname):
            self.add_error("name","This Category already exists")  
        return cleaned_data



class NewItemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields=('cat','name','description','price','image')
        widgets={
            'cat':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),

            
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields=('name','description','price','image','is_sold')
        widgets={
            
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),

            
        }
