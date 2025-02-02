import platform

from threading import Thread
from .basealert import Alert
from .basenotify import Notify
__all__ = [Alert, Notify]

platform = platform.platform()

if 'Darwin' in platform or 'macOS' in platform:
    pass
else:
    raise NotImplementedError(f'No implement pymasl for platform {platform}.')


def send_together(function, function_2):
    if hasattr(function, 'send') and hasattr(function_2, 'send'):
        try:
            f1, f2 = Thread(target=function.send()), Thread(target=function_2.send())
            f1.run(), f2.run()
            return
        except Exception:
            return None

