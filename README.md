
# TrayApp

**based on Moses Palmér's [_pystray_](https://pypi.org/project/pystray/) library!**

Simple library for creating system tray applications.

[![PyPI version](https://badge.fury.io/py/trayapp.svg)](https://badge.fury.io/py/trayapp)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)


### Usage

    with TrayApp(name='Test',  # the little tooltip, seen when hovering over the icon
                 icon_path=Path('../path/to/the/image.png'),  # anything that can be transformed into a PIL.Image
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
            
RadioButtonGroup example:

    items = (
            'hello',
            'world',
            'this',
            'is',
            'just',
            'an',
            'example',
        )
    
    # you NEED to provide the group itself since just state would be by value
    def print_selected(rbg): print(items[rbg.state])

    selected_item = 3  # saved outside and updated when the app is closed

    with TrayApp(name='Test',
                 icon_path=Path(r'C:\Users\robin\Documents\Private\Python\trayPy\data\test.png'),
                 icon_size=(256, 256,)) as app:

        with app.add_radiobuttongroup() as rbg:
            for index, item in enumerate(items):
                rbg.add(text=item, selected=index == selected_item)
        
        # to check if it works
        app.add_button(text='print the selected', action=print_selected, args=(rbg,), default=False)
        
        
### License

MIT, see the LICENSE file
