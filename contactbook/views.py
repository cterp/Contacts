from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView # generic Django view to edit contacts
from django.views.generic import DeleteView
from django.views.generic import DetailView
from contactbook.models import Contact
from django.core.urlresolvers import reverse


class ListContact(ListView):
    model = Contact
    template_name = 'contacts_list.html'


class CreateContact(CreateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContact, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context


class UpdateContact(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContact, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class DeleteContact(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')