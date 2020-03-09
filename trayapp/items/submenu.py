#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.1.1"

"""Library for creating system tray applications
based on Moses Palmér's 'pystray' library
See README for insntructions"""

__all__ = ('SubMenu',)

from pystray import MenuItem


class SubMenu:
    __slots__ = ('text', 'parent', 'menu')

    def __init__(self, parent: 'TrayMenu', text: str):
        self.text: str = text
        self.parent: 'TrayMenu' = parent
        self.menu: 'TrayMenu' = parent.__class__()  # oof, this looks rather awful

    def __enter__(self) -> 'TrayMenu': return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if not exc_type:
            self.parent.add(MenuItem(text=self.text, action=self.menu()))


if __name__ == '__main__': pass
