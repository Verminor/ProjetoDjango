from django import forms
from django.core.mail.message import EmailMessage
from django2.settings import EMAIL_HOST_USER

from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=200)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email=EMAIL_HOST_USER,
            to=['Thrazejin@gmail.com', ],
            headers={'Reply-to': email}
        )
        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'inventory', 'image']
