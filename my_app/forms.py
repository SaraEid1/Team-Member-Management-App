from django import forms


NUMS = [
    (0, "Regular - Can't delete members"),
    (1, "Admin - Can delete members"),
    ]
class CHOICES(forms.Form):
    NUMS  = forms.CharField(widget=forms.RadioSelect(choices=NUMS))