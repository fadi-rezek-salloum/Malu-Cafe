from datetime import datetime

from django.contrib import admin
from django.utils.html import format_html

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    # Anzeige in der Listenansicht
    list_display = ("name", "email", "telefonnummer", "reservierungszeit", "guests", "status")
    list_display_links = ("name", "email")
    list_editable = ("guests",)
    list_filter = ("date", "guests")
    search_fields = ("name", "email", "phone")
    date_hierarchy = "date"
    ordering = ("-date", "time")

    # Gruppierung im Bearbeitungsformular
    fieldsets = (
        ("Kundendaten", {"fields": ("name", "email", "phone")}),
        ("Reservierungsdetails", {"fields": ("date", "time", "guests", "message")}),
    )

    # Nur-Anzeige-Felder
    readonly_fields = ("reservierungszeit",)

    # Benutzerfreundliche Anzeige der Telefonnummer
    def telefonnummer(self, obj):
        return obj.phone

    telefonnummer.short_description = "Telefon"

    # Kombinierte Anzeige von Datum und Uhrzeit
    def reservierungszeit(self, obj):
        return f"{obj.date.strftime('%d.%m.%Y')} – {obj.time.strftime('%H:%M')}"

    reservierungszeit.short_description = "Datum & Uhrzeit"

    # Statusanzeige mit Farbe
    def status(self, obj):
        now = datetime.now()
        res_datetime = datetime.combine(obj.date, obj.time)
        if res_datetime < now:
            color = "gray"
            label = "Vergangen"
        else:
            color = "green"
            label = "Zukünftig"
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>', color, label
        )

    status.short_description = "Status"
