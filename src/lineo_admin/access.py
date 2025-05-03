from django.contrib import auth


class Access:

    @classmethod
    def is_allowed(cls, user, verb, obj):
        name = f'can_{verb}'
        f = getattr(cls, name, None)
        if f is None:
            raise ValueError(f'Unknown access verb "{verb}')

        return f(user, obj)

    @classmethod
    def can_create_user(cls, user, obj):
        return user.is_superuser

    @classmethod
    def can_delete_user(cls, user, obj):
        if user.is_superuser:
            return user.id != obj.id

        return False

    @classmethod
    def can_update_user(cls, user, obj):
        return user.is_superuser


access = Access()


class AccessMixin(auth.mixins.AccessMixin):

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
