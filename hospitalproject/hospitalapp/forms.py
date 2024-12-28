from django import forms
from .models import Booking, Doctors

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['doctor', 'date', 'time']

    doctor = forms.ModelChoiceField(
        queryset=Doctors.objects.all(),
        empty_label="Select a Doctor",
        label="Doctor",
        widget=forms.Select  # Optional, but helps to clarify the field type
    )
