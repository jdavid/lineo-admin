
app_name = 'lineo-pages'

class Access:

    @classmethod
    def create_page(cls, user, obj):
        return user.is_superuser

    @classmethod
    def delete_page(cls, user, obj):
        return user.is_superuser

    @classmethod
    def update_page(cls, user, obj):
        return user.is_superuser


def register(registry):
    registry.access.register(app_name, Access)
    registry.sidebar.register('pages', icon='file-lines', label='Pages', viewname='lineo-pages:page-list')
