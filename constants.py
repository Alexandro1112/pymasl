import AppKit
"""Collection of icons."""

WARNING_ICON = 'warning'
CHECK_MARK_ICON = 'check_mark'
SECURITY_ICON = 'security'
DOCUMENT_ICON = 'document'
USER_ICON = 'user'
CRAYONS_ICON = 'crayons'
TOOLBAR_ICON = 'toolbar'
INFO_ICON = 'info'
COMPUTER_ICON = 'computer'
CAMERA_ICON = 'camera'
HOME_ICON = 'home'
TRASH_ICON = 'trash'
NETWORK_ICON = 'network'
COLOR_ICON = 'color'
STOP_ICON = 'stop'
FOLDER_ICON = 'folder'
SYS_ICON = 'sys'
ADVANCE_ICON = 'advance'
GLASS_ICON = 'glass'

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
