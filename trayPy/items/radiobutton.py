#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.1.0"

"""Library for creating system tray applications
Based on Moses Palmér's 'pystray' library
See README for insntructions"""

__all__ = ('RadioButtonGroup',)

from typing import List
from pystray import MenuItem


class RadioButtonGroup:
    state: int = 0

    def __init__(self, menu, *items):
        self.menu: 'Menu' = menu
        self.items: List = list()
        not items or self.items.extend(*items)

    def __bool__(self): return bool(self.items)

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: self.menu.add(*self.items)

    @property
    def get(self):
        return self.items

    @staticmethod
    def get_state(index: int):  # not a prop since it needs to be a proper method further below
        def inner(item):
            return RadioButtonGroup.state == index
        return inner

    @staticmethod
    def set_state(index: int):  # same as above
        def inner(icon, item):
            RadioButtonGroup.state = index
        return inner

    def add(self, text: str, selected: bool = False):
        index: int = len(self.items)
        if selected: RadioButtonGroup.state = index
        btn: MenuItem = MenuItem(
            text=text,
            action=RadioButtonGroup.set_state(index),
            checked=RadioButtonGroup.get_state(index),
            radio=True
        )
        self.items.append(btn)
        return btn


if __name__ == '__main__': pass
