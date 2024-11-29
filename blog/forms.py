from django import forms

class MensagemForm(forms.Form):
    nome = forms.CharField(
        max_length=100
    )
    email = forms.EmailField(
        max_length=254
    )
    telefone = forms.CharField(
        max_length=12
    )
    mensagem = forms.CharField(
        max_length=1000,
        widget = forms.Textarea()
    )