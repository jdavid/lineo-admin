from django.contrib.auth import mixins
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
