from .constants import *
import objc
import AppKit
import CoreText


class Alert:

    def __str__(self):
        return f'<{Alert.__name__} object at 0x10cc92910>'

    def list_available_fonts(self):
        """Return all available fonts on current machine"""
        font_descriptors = CoreText.CTFontManagerCopyAvailableFontFamilyNames()
        list_fonts = []
        for font in font_descriptors:
            list_fonts.append(font)
        return list_fonts

    @objc._objc.python_method
    def create_alert(self, title, message, width, height, icon, buttons: [tuple, list, str]):
        """Create Alert instance."""
        self.buttons = buttons
        self.alert = AppKit.NSAlert.alloc().init()
        self.alert.setShowsSuppressionButton_(icon)
        icn = AppKit.NSImage.alloc().initWithContentsOfFile_(icon)
        self.alert.setInformativeText_(message)
        self.alert.setAccessoryView_(AppKit.NSView.alloc().initWithFrame_(AppKit.NSMakeRect(0, 0, width, height)))

        self.alert.setMessageText_(title)

        self.dict_btn = {}
        if isinstance(buttons, str):
            i = buttons
            self.alert.addButtonWithTitle_(i)
        else:
            for i in buttons:
                self.alert.addButtonWithTitle_(i)
                for j in range(len(buttons)):
                    self.dict_btn = buttons

        try:
            if icon in styles.keys():
                self.alert.setIcon_(styles[icon])
            else:
                self.alert.setIcon_(icn)
        except KeyError:  # If ``icon`` custom image.
            self.alert.setIcon_(icn)

    def add_entry(self, width, height,
                  border, font, font_size,
                  color, text_color):
        """Add entry widget to alert."""

        self.text_field = AppKit.NSTextField.alloc().initWithFrame_(((0, 0), (width, height)))
        if border is not None:
            self.text_field.setCornerRadius_(border)
        if text_color is not None:
            text_color = eval('AppKit.NSColor.%sColor()' % text_color.lower())
            self.text_field.setTextColor_(text_color)
        if font is not None and font_size is not None:
            if font in self.list_available_fonts():
                self.text_field.setFont_(AppKit.NSFont.fontWithName_size_(font, font_size))
            raise NameError('Font not supported on device or not found')
        if color is not None:
            color = eval('AppKit.NSColor.%sColor()' % color.lower())  # Strange name function in
            self.text_field.setBackgroundColor_(color)
        self.alert.setAccessoryView_(self.text_field)  # display widget on alert.

    def add_slider(self, color, width,
                   height,
                   tracker_color,
                   slider_default_value=0,
                   slider_max_value=None, slider_min_value=None,
                   ):
        """Add slider widget to alert."""

        self.popup_button = AppKit.NSSlider.alloc().initWithFrame_(((0, 0), (width, height)))
        if color is not None:
            bg = eval('AppKit.NSColor.%sColor()' % color.lower())
            self.popup_button.setBackgroundColor_(bg)
        if slider_min_value is not None:
            self.popup_button.setMinValue_(slider_min_value)
        if slider_max_value is not None:
            self.popup_button.setMaxValue_(slider_max_value)
        if slider_default_value is not None:
            self.popup_button.setValue_(slider_default_value)
        if tracker_color is not None:
            color_trk = eval('AppKit.NSColor.%sColor()' % tracker_color.lower())

            self.popup_button.setTrackFillColor_(color_trk)

        self.alert.setAccessoryView_(self.popup_button)

    def add_popup_button(self, options: [str, list, tuple],
                         width, height,
                         color, controller_size: int,
                         border, opacity: bool):
        """Add popup button to alert."""
        self.popup_button_options = options
        self.pop_button = AppKit.NSPopUpButton.alloc().initWithFrame_(((0, 0),
                                                                       (width,
                                                                        height)))

        if isinstance(options, str):
            self.pop_button.addItemWithTitle_(options)
        else:
            for params in options:
                self.pop_button.addItemWithTitle_(params)
        if color is not None:
            text_color = eval('AppKit.NSColor.%sColor()' % color.lower())
            self.pop_button.setBackgroundColor_(text_color)
        if border is not None:
            self.pop_button.setCornerRadius_(border)
        if controller_size is not None:
            self.pop_button.setFlipped_(0)
            self.pop_button.setControlSize_(controller_size)
        if opacity is not None:
            self.pop_button.setTransparent_(int(opacity))
        self.alert.setAccessoryView_(self.pop_button)

    def add_radio_button(self, options, width, height,
                         color, border,
                         font,  font_size, title,
                         button_state: [0, 1]):

        self.radio = AppKit.NSButton.alloc().initWithFrame_(((0, 0), (width, height)))
        self.radio.setButtonType_(AppKit.NSSwitchButton)

        if isinstance(options, str):
            self.radio.setAccessibilityColumnTitles_(options)
        else:
            for params in options:
                self.radio.setAccessibilityColumnTitles_(params)
        if button_state is not None:
            self.radio.setState_(button_state)
        if color is not None:
            bg = eval('AppKit.NSColor.%sColor()' % color.lower())
            self.radio.setBackgroundColor_(bg)
        if title is not None:
            self.radio.setTitle_(title)
        if border is not None:
            self.radio.setCornerRadius_(border)
        if font is not None and font_size is not None:
            if font in self.list_available_fonts():
                self.text_field.setFont_(AppKit.NSFont.fontWithName_size_(font, font_size))
            raise NameError('Font not supported on device or not found')

        self.alert.setAccessoryView_(self.radio)

    @property
    def entry_text(self):
        try:
            return self.text_field.stringValue(),
        except AttributeError:  # if entry widget has been not added
            raise AttributeError(f'Make object instance {self.add_entry.__name__} for get entry text.')

    @property
    def popup_button_option(self):
        try:
            value = self.pop_button.indexOfSelectedItem()
            if isinstance(self.popup_button_options, str):
                return self.popup_button_options
            return self.popup_button_options[value]
        except AttributeError:
            raise AttributeError(f'Make object instance {self.add_popup_button.__name__} for get button-choice state.')

    @property
    def slider_value(self):
        try:
            return self.popup_button.stringValue()
        except AttributeError:
            raise AttributeError(f'Make object instance {self.add_slider.__name__} for get slider value state.')
        except TypeError:
            return 0  # if slider not moved to determine number, different of zero.

    @property
    def radio_button_pressed(self):
        try:
            return self.radio.stringValue()
        except AttributeError:
            raise AttributeError(f'Make object instance {self.add_radio_button.__name__} for get button state.')


    @property
    def pressed_button(self):
        try:
            return self.dict_btn[self.runner - 1000],  # return button name instead index of pressed button
        except KeyError:  # If in alert only one button
            return self.buttons

    def send(self):
        self.runner = self.alert.runModal()


