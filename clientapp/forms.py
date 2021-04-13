from .models import Call, CustomUser
from django.forms import ModelForm, forms
from django import forms


class CallForm(ModelForm):
    class Meta:
        model = Call
        fields = ['title', 'category', 'message', 'file']


class LoginForm(ModelForm):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)

    def __init__(self, *args, **kwagrs):
        super().__init__(*args, **kwagrs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self, *args, **kwagrs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден в системе.')
        user = CustomUser.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
