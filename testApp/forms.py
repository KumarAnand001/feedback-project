from typing import Any
from django import forms
from django.core import validators

def start_with_d(value):

    if value[0].lower() != 'd':

        raise forms.ValidationError('Name should be start with d or D')
    

def gmailVerification(value):

    if value[len(value) - 9 : ] != 'gmail.com':

        raise forms.ValidationError('Must be gmail')

class FeedbackForm(forms.Form):

    name = forms.CharField(validators=[start_with_d])
    rollNo = forms.IntegerField()
    email = forms.EmailField(validators=[gmailVerification])
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)
    

    # def clean_name(self):

    #     inputName = self.cleaned_data['name']
    #     if len(inputName) < 4:

    #         raise forms.ValidationError('The length of name field should >=4')
        
    def clean(self):
        print('form submited')
        cleaned_data = super().clean()
        inputName = cleaned_data['name']
        if len(inputName) < 10:

            raise forms.ValidationError('Name should compulsory contains minimum 10 character')
        
        inputRollNo = cleaned_data['rollNo']
        if len(str(inputRollNo)) != 3:

            raise forms.ValidationError('RollNo should compulsory contains exactly 3 digit')
        
        inputpwd = cleaned_data['password']
        inputrpwd = cleaned_data['rpassword']

        if inputpwd != inputrpwd :

            raise forms.ValidationError('Password not matched')
        
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0 :

            raise forms.ValidationError('Thanks Bot!!!')