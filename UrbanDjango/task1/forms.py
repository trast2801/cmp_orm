from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label = 'Введите логин')
    pass_ = forms.CharField(min_length=8, label = 'Введите пароль')
    pass_ret = forms.CharField(min_length=8,label='повторите пароль')
    age = forms.CharField(max_length=3,label='Введите ваш возраст')