from django import forms
from .models import Mensagem, Blog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ["nome", "email", "telefone", "mensagem"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-md-6'),
                Column('telefone', css_class='col-md-6'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='col-md-12'),
                Column('mensagem', css_class='col-12'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-primary text-uppercase')
        )
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog.objects.first()
        fields = "__all__"