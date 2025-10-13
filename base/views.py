from django.views.generic import TemplateView

from .forms import ContactForm, ReservationForm


def generate_time_choices():
    return [f"{hour:02d}:{minute:02d}" for hour in range(7, 18) for minute in [0, 15, 30, 45]]


class IndexView(TemplateView):
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        context["contact_form"] = ContactForm()
        context["time_choices"] = generate_time_choices()
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        contact_form = ContactForm(request.POST)
        context = self.get_context_data()

        if "name" in request.POST and "message" in request.POST:
            if contact_form.is_valid():
                contact_form.save()
                context["contact_form"] = ContactForm()
                context["contact_success"] = True
            else:
                context["contact_form"] = contact_form
                context["contact_error"] = True
        else:
            if reservation_form.is_valid():
                reservation_form.save()
                context["form"] = ReservationForm()
                context["success"] = True
            else:
                context["form"] = reservation_form
                context["error"] = True

        return self.render_to_response(context)


class MenuView(TemplateView):
    template_name = "base/menu.html"
