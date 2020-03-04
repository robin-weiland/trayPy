#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-02"
__version__ = "0.1.0"

"""Library for creating system tray applications
Based on Moses Palmér's 'pystray' library
See README for insntructions"""

__all__ = ('TrayApp',)

from typing import Union, Tuple
from pystray import Icon
from PIL import Image
from pathlib import Path
from trayPy.tray_menu import TrayMenu


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


if __name__ == '__main__': pass
