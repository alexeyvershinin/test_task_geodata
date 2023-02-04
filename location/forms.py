from django import forms
from location.models import PlotData


class CadastralNumberForm(forms.ModelForm):
    class Meta:
        model = PlotData
        fields = ['number', ]

        widgets = {
            'number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите номер участка'}),
        }

    def __init__(self, *args, **kwargs):
        super(CadastralNumberForm, self).__init__(*args, **kwargs)
        self.fields['number'].label = ''
