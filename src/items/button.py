#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.0.0"

__all__ = ('Button',)

from typing import Callable
from pystray import MenuItem


class Button:
    text: str
    action: Callable
    default: bool
    enabled_: bool

    def get(self): return MenuItem(text=self.text, action=self.action, default=self.default, enabled=self.enabled)

    @property
    def enabled(self): return self.enabled


if __name__ == '__main__': pass
