#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.1.2"

"""Library for creating system tray applications
based on Moses Palmér's 'pystray' library
See README for insntructions"""

__all__ = ('TrayApp',)

from typing import Union, Tuple
from pystray import Icon
from PIL import Image
from pathlib import Path
from trayapp.tray_menu import TrayMenu


class TrayApp:
    __slots__ = ('app', 'menu',)

    app: Icon
    menu: TrayMenu

    def __init__(self, name: str, icon_or_path: Union[str, Path, type(Image)], icon_size: Tuple[int, int]):
        self.app = Icon(name=name, title=name)
        self.set_icon(icon_or_path, icon_size)
        self.menu = TrayMenu()

    def __repr__(self) -> str: return str(self.app.menu or self.menu())

    __str__ = __repr__

    def __enter__(self) -> TrayMenu: return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if not exc_type:
            self.app.menu = self.menu()
            self.app.update_menu()
            self.run()

    def __bool__(self): return self.app.visible

    def set_icon(self, icon_or_path: Union[str, Path, type(Image)], icon_size: Tuple[int, int]):
        if not isinstance(icon_or_path, (Path, str)):
            (image := icon_or_path).thumbnail(icon_size)
        elif not (icon_or_path := Path(icon_or_path)).exists():
            raise FileNotFoundError(f'Could not find image: "{icon_or_path}"')
        else:
            (image := Image.open(icon_or_path)).thumbnail(icon_size)
        self.app.icon = image
        self.app.icon.visible = True

    # lambda to ensure that the icon is visible on every platform
    def run(self) -> None: self.app.run(lambda icon: setattr(icon, 'visible', True))

    def stop(self) -> None: self.app.stop()


if __name__ == '__main__':
    with TrayApp(name='Test',  # the little tooltip, seen when hovering over the icon
                 icon_or_path=Path(r'C:\Users\robin\Pictures\Wallpaper\cyberpunk_bttf.jpg'),  # anything that can be transformed into a PIL.Image
                 icon_size=(256, 256,)  # size to create the thumbnail
                 ) as app:
        # create the menu shown when icon gets right-clicked here

        app.add_button(text='hello world',
                       action=print,  # method to call when clicked
                       args=('hello world',),  # arguments, optional, in a tuple
                       # determines wheter the function gets called when the icon is left-clicked
                       # optional, default to False, can be obviously only used once per app
                       default=True
                       )

        app.add_separator()  # well...

        with app.add_submenu(text='SubMenu') as submenu:  # submenues can be created by using a context manager within

            with submenu.add_submenu(text='first subsub') as first_sub_sub:  # and recursivly as well
                first_sub_sub.add_button(text='1.1', action=print, args=('1.1',))
                first_sub_sub.add_button(text='1.2', action=print, args=('1.2',))

            with submenu.add_submenu(text='second susub') as second_sub_sub:
                second_sub_sub.add_button(text='2.1', action=print, args=('2.1',))
                second_sub_sub.add_button(text='2.2', action=print, args=('2.2',))

            # any add_button(), add_separator(), add_submenu(), add_radiobuttongroup() can be used here
            # just remember to add them to the right submenu

        app.add_separator()

        # a RadioButtonGroup is a group of buttons which can be used to select something
        # trying it out might be the best way to understand it
        with app.add_radiobuttongroup() as rbg:  # used with a contextmanager as well
            rbg.add(text='hello')
            rbg.add(text='world', selected=True)  # selected determines the item which is selected on creation
