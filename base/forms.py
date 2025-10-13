from datetime import datetime

from django import forms

from .models import ContactMessage, Reservation


class ReservationForm(forms.ModelForm):
    TIME_CHOICES = [
        (f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
        for hour in range(7, 19)
        for minute in [0, 15, 30, 45]
    ]

    time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Reservation
        fields = ["name", "email", "phone", "date", "time", "guests", "message"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:
            try:
                reservation_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                if reservation_datetime < datetime.now():
                    raise forms.ValidationError(
                        "Datum und Uhrzeit dürfen nicht in der Vergangenheit liegen."
                    )
            except ValueError:
                raise forms.ValidationError("Ungültiges Datum oder Uhrzeitformat.")


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Dein Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Deine E-Mail"}),
            "message": forms.Textarea(attrs={"placeholder": "Deine Nachricht"}),
        }
