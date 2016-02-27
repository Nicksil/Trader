from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from finder.forms import SingleTypeLookupForm


class SingleTypeLookupView(FormView):

    form_class = SingleTypeLookupForm
    template_name = 'finder/single_type_lookup_form.html'
    success_url = reverse_lazy('finder:single_type_lookup_view')

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
