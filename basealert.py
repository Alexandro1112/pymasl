from .constants import *
import objc
import AppKit


class Alert:

    def __str__(self):
        return f'<{Alert.__name__} object at 0x10cc92910>'

    @objc._objc.python_method
    def create_alert(self, title, message, width, height, icon: [INFO_ICON, WARNING_ICON, TRASH_ICON, SYS_ICON,
                                                                 STOP_ICON, SECURITY_ICON, ADVANCE_ICON, CAMERA_ICON,
                                                                 COLOR_ICON, CRAYONS_ICON, DOCUMENT_ICON, FOLDER_ICON,
                                                                 HOME_ICON, NETWORK_ICON, TOOLBAR_ICON, USER_ICON,
                                                                 COMPUTER_ICON, CHECK_MARK_ICON],
                                                                 buttons: [tuple, list, str]):
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
            styles = {
                'warning': AppKit.NSImage.imageNamed_('NSCaution'),
                'check_mark': AppKit.NSImage.imageNamed_('NSMenuOnStateTemplate'),
                'security': AppKit.NSImage.imageNamed_('NSSecurity'),
                'document': AppKit.NSImage.imageNamed_('NSMultipleDocuments'),
                'user': AppKit.NSImage.imageNamed_('NSUser'),
                'crayons': AppKit.NSImage.imageNamed_('NSColorPickerCrayon'),
                'toolbar': AppKit.NSImage.imageNamed_('NSToolbarCustomizeToolbarItemImage'),
                'info': AppKit.NSImage.imageNamed_('NSInfo'),
                'camera': AppKit.NSImage.imageNamed_('NSTouchBarCommunicationVideoTemplate'),
                'home': AppKit.NSImage.imageNamed_('NSHomeTemplate'),
                'trash': AppKit.NSImage.imageNamed_('NSTrashFull'),
                'network': AppKit.NSImage.imageNamed_('NSNetwork'),
                'color': AppKit.NSImage.imageNamed_('NSColumnViewTemplate'),
                'stop': AppKit.NSImage.imageNamed_('NSStopProgressTemplate'),
                'folder': AppKit.NSImage.imageNamed_('NSFolder'),
                'sys': AppKit.NSImage.imageNamed_('NSPreferencesGeneral'),
                'computer':  AppKit.NSImage.imageNamed_('NSComputer'),
                'advance': AppKit.NSImage.imageNamed_('NSAdvanced'),
                'glass': AppKit.NSImage.imageNamed_('NSSmallMagnifyingGlass'),
            }
            if icon in styles.keys():
                self.alert.setIcon_(styles[icon])
            else:
                self.alert.setIcon_(icn)
        except KeyError:  # If ``icon`` custom image.
            self.alert.setIcon_(icn)
        finally:
            return self

    def add_entry(self, entry_width, entry_height,
                  entry_border, entry_font, entry_font_size,
                  entry_color, entry_text_color):
        """Add entry widget to alert."""

        self.text_field = AppKit.NSTextField.alloc().initWithFrame_(((0, 0), (entry_width, entry_height)))
        if entry_border is not None:
            self.text_field.setCornerRadius_(entry_border)
        if entry_text_color is not None:
            text_color = eval('AppKit.NSColor.%sColor()' % entry_text_color)
            self.text_field.setTextColor_(text_color)
        if entry_font is not None and entry_font_size is not None:
            self.text_field.setFont_(AppKit.NSFont.fontWithName_size_(entry_font, entry_font_size))
        if entry_color is not None:
            color = eval('AppKit.NSColor.%sColor()' % entry_color)  # Strange name function in
            self.text_field.setBackgroundColor_(color)
        self.alert.setAccessoryView_(self.text_field)  # display widget on alert.

    def add_slider(self, slider_color, slider_width,
                   slider_height,
                   slider_tracker_color,
                   slider_default_value=0,
                   slider_max_value=None, slider_min_value=None,
                   ):
        """Add slider widget to alert."""

        self.popup_button = AppKit.NSSlider.alloc().initWithFrame_(((0, 0), (slider_width, slider_height)))
        if slider_color is not None:
            bg = eval('AppKit.NSColor.%sColor()' % slider_color)
            self.popup_button.setBackgroundColor_(bg)
        if slider_min_value is not None:
            self.popup_button.setMinValue_(slider_min_value)
        if slider_max_value is not None:
            self.popup_button.setMaxValue_(slider_max_value)
        if slider_default_value is not None:
            self.popup_button.setValue_(slider_default_value)
        if slider_tracker_color is not None:
            color_trk = eval('AppKit.NSColor.%sColor()' % slider_tracker_color)

            self.popup_button.setTrackFillColor_(color_trk)

        self.alert.setAccessoryView_(self.popup_button)

    def add_popup_button(self, popup_button_options: [str, list, tuple],
                         popup_button_width, popup_button_height,
                         popup_button_color, popup_button_controller_size: int,
                         popup_button_border, popup_button_opacity: bool):
        """Add popup button to alert."""
        self.popup_button_options = popup_button_options
        self.pop_button = AppKit.NSPopUpButton.alloc().initWithFrame_(((0, 0),
                                                                       (popup_button_width,
                                                                        popup_button_height)))

        if isinstance(popup_button_options, str):
            self.pop_button.addItemWithTitle_(popup_button_options)
        else:
            for params in popup_button_options:
                self.pop_button.addItemWithTitle_(params)
        if popup_button_color is not None:
            text_color = eval('AppKit.NSColor.%sColor()' % popup_button_color)
            self.pop_button.setBackgroundColor_(text_color)
        if popup_button_border is not None:
            self.pop_button.setCornerRadius_(popup_button_border)
        if popup_button_controller_size is not None:
            self.pop_button.setFlipped_(0)
            self.pop_button.setControlSize_(popup_button_controller_size)
            self.pop_button.setOpaque_(90)
        if popup_button_opacity is not None:
            self.pop_button.setTransparent_(int(popup_button_opacity))
        self.alert.setAccessoryView_(self.pop_button)

    def add_radio_button(self, radio_button_width, radio_button_height,
                         radio_button_color, radio_button_border,
                         radio_button_font,  radio_button_font_size, radio_button_title,
                         radio_button_state: [0, 1], radio_button_text_rotation: int):
        self.radio = AppKit.NSButton.alloc().initWithFrame_(((0, 0), (radio_button_width, radio_button_height)))
        self.radio.setButtonType_(AppKit.NSSwitchButton)
        if radio_button_text_rotation is not None:
            self.radio.setBoundsRotation_(radio_button_text_rotation)
        if radio_button_state is not None:
            self.radio.setState_(radio_button_state)
        if radio_button_color is not None:
            bg = eval('AppKit.NSColor.%sColor()' % radio_button_color)
            self.radio.setBackgroundColor_(bg)
        if radio_button_title is not None:
            self.radio.setTitle_(radio_button_title)
        if radio_button_border is not None:
            self.radio.setCornerRadius_(radio_button_border)
        if radio_button_font is not None and radio_button_font_size is not None:
            self.radio.setFont_(AppKit.NSFont.fontWithName_size_(radio_button_font, radio_button_font_size))

        self.alert.setAccessoryView_(self.radio)  #

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
            return bool(int(self.radio.stringValue()))
        except AttributeError:
            raise AttributeError(f'Make object instance {self.add_radio_button.__name__} for get button state.')

    def send(self):
        """Necessary to call."""
        self.runner = self.alert.runModal()
        return self 

    @property
    def pressed_button(self):
        try:
            return self.dict_btn[self.runner - 1000],  # return button name instead index of pressed button
        except KeyError:  # If in alert only one button
            return self.buttons







