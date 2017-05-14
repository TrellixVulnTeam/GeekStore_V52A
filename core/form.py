#coding=utf-8

from django import forms

class ContactForm(forms.Form):

	name = forms.CharField(label='Nome', required='True')
	email = forms.EmailField(label='Email')
	mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['mensagem'].widget.attrs['class'] = 'form-control'