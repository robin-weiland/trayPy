#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.0.0"

__all__ = ('TrayApp',)

from typing import Union, Tuple
from pystray import Icon, MenuItem
from PIL import Image
from pathlib import Path
from src.traymenu import TrayMenu
# from atexit import register


class TrayApp:
    app: Icon
    menu: TrayMenu

    def __init__(self, name: str, icon_path: Union[str, Path], icon_size: Tuple[int, int]):
        # register(self.stop)
        icon_path = Path(icon_path)
        if not icon_path.exists(): raise FileNotFoundError(f'Could not find image at "{icon_path}"')
        image = Image.open(icon_path)
        image.thumbnail(icon_size)
        self.app = Icon(name=name, title=name,
                        icon=image
                        )
        self.menu = TrayMenu()

    def __enter__(self): return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.app.menu = self.menu.get
            self.app.update_menu()
            self.run()

    def run(self): self.app.run()

    def stop(self): self.app.stop()


def test(rbg: 'RadioButtonGroup'):
    if rbg.state == 0: print('hello')
    elif rbg.state == 1: print('world')


if __name__ == '__main__':
    with TrayApp('Test', Path(r'C:\Users\robin\Documents\Private\Python\trayPy\data\test.png'), (256, 256,)) as app:
        # app.add_separator()
        app.add_button('hello world', print, ('hello world',), True)
        app.add_button('u dumb', print, ('u dumb',))
        app.add_button('print', print, ('test',))
        app.add_separator()
        with app.create_menu() as submenu:
            submenu.add_button('first', print, ('frist',))
            submenu.add_button('second', print, ('second',))
        app.add_submenu('submenu', submenu)
        app.add_separator()
        with app.add_radiobuttongroup() as rbg:
            rbg.add('hello')
            rbg.add('world')
        app.add_separator()
        app.add_button('Radiobutton Test', test, (rbg,))


