#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.0.0"

__all__ = ('SubMenu',)

from pystray import MenuItem


class SubMenu:
    def __init__(self, parent: 'TrayMenu', text: str):
        self.menu: MenuItem = MenuItem(text=text)
        self.parent: 'TrayMenu' = parent

    def __enter__(self): return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None: self.parent.items.append(self.menu)

    def __getattribute__(self, item):
        try: super().__getattribute__(item)
        except AttributeError: getattr(self.menu, item)


if __name__ == '__main__': pass
