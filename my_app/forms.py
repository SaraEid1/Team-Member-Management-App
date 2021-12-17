from django.forms import ModelForm
from django import forms
from .models import TeamMember

ROLE_CHOICES = [
    (' ', "Regular - Can't delete members"),
    ('(admin)', "Admin - Can delete members")
]

class AddPageForm (forms.ModelForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = TeamMember
        fields = ('__all__')
        widget = {
            'firstname':forms.TextInput (),
            'lastname':forms.TextInput (),
            'email':forms.EmailInput (),
            'phonenumber':forms.TextInput ()
        }
    def __init__(self, *args, **kwargs):
        super(AddPageForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs\
            .update({
                'placeholder': 'Charlene',
                'class': 'form-control',
            })
        self.fields['lastname'].widget.attrs\
            .update({
                'placeholder': 'Pham',
                'class': 'form-control'
            })
        
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'charlene@instawork.com',
                'class': 'form-control'
            })
        self.fields['phonenumber'].widget.attrs\
            .update({
                'placeholder': '415-310-1619',
                'class': 'form-control'
            })
        self.fields['firstname'].label = ''
        self.fields['lastname'].label = ''
        self.fields['email'].label = ''
        self.fields['phonenumber'].label = ''
        self.fields['role'].label = ''