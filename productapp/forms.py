from  django import forms

class ProductForm(forms.Form):
    pid=forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product Id'
            }
        )
    )
    pname=forms.CharField(
        label="Enter Your Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    pcost=forms.IntegerField(
        label="Enter Your product cost ",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Pruduct Cost'
            }
        )
    )
    pcolor=forms.CharField(
        label="Enter Your Product color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product color'
            }
        )
    )
    pclass=forms.CharField(
        label='Enter Your Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    quantity=forms.IntegerField(
        label="Enter Product Quantity",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Quantity'
            }
        )
    )
class UpdateForm(forms.Form):
    pid=forms.IntegerField(
        label="Enter Your Product Id  ",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    pcost=forms.IntegerField(
        label="Enter product Updates Cost",
        widget=forms.NumberInput(
            attrs={
                "class":'form-control',
                'placeholder':'Product Update Cost'
            }
        )

    )
class DeleteForm(forms.Form):
    pid=forms.IntegerField(
        label="Enter Your Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )

