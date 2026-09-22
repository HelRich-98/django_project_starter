from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "core/index.html"


class AboutView(generic.TemplateView):
    template_name = "core/about.html"


class ContactView(generic.TemplateView):
    template_name = "core/contact.html"
