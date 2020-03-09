#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.1.1"

"""Library for creating system tray applications
based on Moses Palmér's 'pystray' library
See README for insntructions"""

__all__ = ('TrayMenu',)

from typing import List, Callable
from pystray import MenuItem, Menu
from trayapp.items import RadioButtonGroup
from trayapp.items import SubMenu


class TrayMenu:
    __slots__ = ('items',)

    def __init__(self, *items: List[MenuItem]):
        # noinspection PyTypeChecker
        self.items: List[MenuItem] = list(items)

    def __enter__(self) -> 'TrayMenu': return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None: pass

    def __call__(self) -> Menu: return Menu(*self.items)

    def __bool__(self) -> bool: return bool(self.items)

    def __repr__(self) -> str: return str(self())

    __str__ = __repr__

    def add(self, *items) -> None: self.items.extend(items)

    def add_button(self, text: str, action: Callable, args=None,
                   default: bool = False, checked: bool = lambda icon: False) -> MenuItem:
        self.add(btn := MenuItem(text=text, action=lambda: action(*(args or ())), default=default, checked=checked))
        return btn

    def add_submenu(self, text: str) -> SubMenu:
        return SubMenu(self, text)

    def add_radiobuttongroup(self) -> RadioButtonGroup:
        return RadioButtonGroup(self)

    def add_separator(self) -> None:
        self.add(Menu.SEPARATOR)

    @staticmethod
    def create_menu(*items) -> 'TrayMenu': return TrayMenu(*items)


if __name__ == '__main__': pass
