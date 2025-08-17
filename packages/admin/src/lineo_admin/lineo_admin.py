app_name = 'lineo-admin'


class Access:

    @classmethod
    def create_user(cls, user, obj):
        return user.is_superuser

    @classmethod
    def delete_user(cls, user, obj):
        if user.is_superuser:
            return user.id != obj.id

        return False

    @classmethod
    def update_user(cls, user, obj):
        return user.is_superuser

    @classmethod
    def update_profile(cls, user, obj):
        return user.id == obj.id


def register(registry):
    registry.access.register(app_name, Access)
    registry.sidebar.register('users', icon='user', label='Users', viewname='lineo-admin:user-list')
