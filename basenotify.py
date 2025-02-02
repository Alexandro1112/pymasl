from .constants import styles
import NotificationCenter
import AppKit
from inspect import signature


class Notify:
    def __init__(self,
                 title,
                 subtitle,
                 image=None,
                 sound=NotificationCenter.NSUserNotificationDefaultSoundName):
        self.notify = NotificationCenter.NSUserNotification.alloc().init()
        if title is not None:
            self.notify.setTitle_(title)
        if subtitle is not None:
            self.notify.set_subtitle_(subtitle)

        img = styles[image]
        self.notify.setContentImage_(img)

        self.notify.set_lockscreenOnly_(True)
        self.notify.setSoundName_(sound)
        
    def custom_method(self, method, args):

        """
        The function allows you to add various attributes to NSAlert and assign arguments, then enable.
        Example: ``custom_method('setAlertStyle_', ['AppKit.NSCriticalAlertStyle'])``,
        it replaces:



        :param method: name of method of you require to add.
        :param args: arguments which method are accept. Assign None if function don't accept any arguments.
         Pass ``None`` if method do not accept any arguments.
        :return: status of executed function or value.
        """
        pool = AppKit.NSAutoreleasePool.alloc()
        pool.init()
        if args is None:
            args = []
        fragment = eval(f'self.notify.%s' % method)
        _signature = signature(fragment).parameters
        length = len(_signature) # return length of dict equals number of arguments

        if len(args) != length or method not in dir(self.notify):
            raise Exception(f'Wrong arguments. Need {length} arguments, got {len(args)}')

        _method = f'self.notify.%s('
        for i in range(len(args)):
            _method += '%s, '
        _method += ')'

        _out_ref = eval(_method % (method, *args))
        del pool
        return _out_ref

    def send(self, interval=0):
        self.notify.setDeliveryDate_(NotificationCenter.NSDate.dateWithTimeInterval_sinceDate_(
            interval, NotificationCenter.NSDate.date()
        ))

        NotificationCenter.NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(
            self.notify
        )



