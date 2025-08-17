from dataclasses import dataclass


@dataclass
class SidebarItem:
    icon: str
    label: str
    viewname: str


class Sidebar:

    def __init__(self):
        self.items = {}

    def register(self, name, icon, label, viewname):
        self.items[name] = SidebarItem(icon, label, viewname)

    def get_items(self):
        return sorted(self.items.values(), key=lambda x: x.label)


class Access:

    def __init__(self):
        self.items = {}

    def register(self, name, access):
        self.items[name] = access

    def is_allowed(self, user, verb, obj):
        app_name, name = verb.split(':')
        access = self.items[app_name]
        f = getattr(access, name, None)
        if f is None:
            raise ValueError(f'Unknown access verb "{verb}"')

        return f(user, obj)


access = Access()
sidebar = Sidebar()
