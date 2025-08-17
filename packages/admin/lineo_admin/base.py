# Django
from django.contrib.auth import mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from formset.views import FormViewMixin

from .registry import access


class AccessMixin(mixins.AccessMixin):

    access_verb = None

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.test_func(request.user, self.object):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    @classmethod
    def test_func(cls, user, obj=None):
        access_verb = cls.access_verb
        assert access_verb is not None
        return access.is_allowed(user, access_verb, obj)


class ListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lineo_admin/list.html'
    create_viewname = None

    def get_columns(self):
        fields = []

        model = self.model
        for column in self.columns:
            field = model._meta.get_field(column)
            fields.append(field)

        return fields


class CreateView(AccessMixin, FormViewMixin, generic.CreateView):
    template_name = 'lineo_admin/edit.html'

    def get_object(self):
        return None


class ReadView(AccessMixin, FormViewMixin, generic.DetailView):
    pass


class UpdateView(AccessMixin, FormViewMixin, generic.UpdateView):
    template_name = 'lineo_admin/edit.html'


class DeleteView(AccessMixin, FormViewMixin, generic.DeleteView):
    template_name = 'lineo_admin/delete.html'
