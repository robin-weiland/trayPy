#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.0.0"

__all__ = ('TrayApp',)

from typing import Union, Tuple
from pystray import Icon
from PIL import Image
from pathlib import Path
from src.tray_menu import TrayMenu


class TrayApp:
    __slots__ = ('app', 'menu',)

    app: Icon
    menu: TrayMenu

    def __init__(self, name: str, icon_path: Union[str, Path], icon_size: Tuple[int, int]):
        if not (icon_path := Path(icon_path)).exists(): raise FileNotFoundError(f'Could not find image: "{icon_path}"')
        (image := Image.open(icon_path)).thumbnail(icon_size)
        self.app = Icon(name=name, title=name, icon=image)
        self.menu = TrayMenu()

    def __repr__(self) -> str: return str(self.app.menu or self.menu())

    __str__ = __repr__

    def __enter__(self) -> TrayMenu: return self.menu

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if not exc_type:
            self.app.menu = self.menu()
            self.app.update_menu()
            self.run()

    # lambda to ensure that the icon is visible on every platform
    def run(self) -> None: self.app.run(lambda icon: setattr(icon, 'visible', True))

    def stop(self) -> None: self.app.stop()


if __name__ == '__main__':
    tray_app = TrayApp(name='Test',
                       icon_path=Path(r'C:\Users\robin\Documents\Private\Python\trayPy\data\test.png'),
                       icon_size=(256, 256,))

    with tray_app as app:

        app.add_button(text='hello world', action=print, args=('hello world',), default=True)

        app.add_separator()

        with app.add_submenu(text='SubMenu') as submenu:

            with submenu.add_submenu(text='first subsub') as first_sub_sub:
                first_sub_sub.add_button(text='1.1', action=print, args=('1.1',))
                first_sub_sub.add_button(text='1.2', action=print, args=('1.2',))

            with submenu.add_submenu(text='second susub') as second_sub_sub:
                second_sub_sub.add_button(text='2.1', action=print, args=('2.1',))
                second_sub_sub.add_button(text='2.2', action=print, args=('2.2',))

        app.add_separator()

        with app.add_radiobuttongroup() as rbg:
            rbg.add(text='hello')
            rbg.add(text='world', selected=True)

        #

        # RadioButtonGroup example #

        # items = (
        #     'hello',
        #     'world',
        #     'this',
        #     'is',
        #     'just',
        #     'an',
        #     'example',
        # )
        #
        #
        # # you NEED to provide the group itself since just state would be by value
        # def print_selected(rbg):
        #     print(items[rbg.state])
        #
        #
        # selected_item = 3  # saved outside and updated when the app is closed
        #
        # with TrayApp(name='Test',
        #              icon_path=Path(r'C:\Users\robin\Documents\Private\Python\trayPy\data\test.png'),
        #              icon_size=(256, 256,)) as app:
        #
        #     with app.add_radiobuttongroup() as rbg:
        #         for index, item in enumerate(items):
        #             rbg.add(text=item, selected=index == selected_item)
        #
        #     # to check if it works
        #     app.add_button(text='print the selected', action=print_selected, args=(rbg,), default=False)
