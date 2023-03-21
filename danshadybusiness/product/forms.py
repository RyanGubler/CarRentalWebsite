from django import forms


class ServiceForm(forms.Form):
    tick1 = forms.BooleanField(required=False, label="Ticket 1")
    tick2 = forms.BooleanField(required=False, label="Ticket 2")
    tick3 = forms.BooleanField(required=False, label="Ticket 3")
