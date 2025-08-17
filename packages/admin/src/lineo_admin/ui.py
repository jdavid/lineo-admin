from dataclasses import dataclass


@dataclass
class Action:
    icon: str
    title: str
    viewname: str
    drawer: bool = True
