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

sidebar = Sidebar()
