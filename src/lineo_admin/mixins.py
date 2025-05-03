from django.contrib import auth


class AccessMixin(auth.mixins.AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.test_func(request.user, self.object):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    @classmethod
    def test_func(self, user, obj=None):
        return True
