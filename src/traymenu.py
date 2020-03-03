#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.0.0"

__all__ = ('TrayMenu',)

from typing import List, Callable
from pystray import MenuItem, Menu
from src.items.radiobutton import RadioButtonGroup
from src.items.submenu import SubMenu


class TrayMenu:
    __slots__ = ('items',)

    def __init__(self, *items):
        self.items: List = list()
        self.items.extend(items)

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: pass

    def __call__(self): return Menu(*self.items)

    @property
    def get(self): return Menu(*self.items)

    def __bool__(self): return bool(self.items)

    def add_submenu(self, text: str, menu: 'Menu'):
        menu: MenuItem = MenuItem(text=text, action=menu.get)
        self.items.append(menu)
        return menu

    def add_button(self, text: str, action: Callable, args=None, default=False) -> MenuItem:
        btn: MenuItem = MenuItem(text=text, action=lambda: action(*(args or ())), default=default)
        self.items.append(btn)
        return btn

    def add_radiobuttongroup(self):
        return RadioButtonGroup(self)

    def add_separator(self) -> None:
        self.items.append(Menu.SEPARATOR)

    @staticmethod
    def create_menu(*items): return TrayMenu(*items)


if __name__ == '__main__': pass
