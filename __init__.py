import platform
import sys

platform = platform.platform()
if 'Darwin' in platform or 'macOS' in platform:
    from .basealert import Alert  # success.
    from .constants import *

elif sys.implementation.version.major > 4:
    raise Exception(f'No has library pymas for python {sys.implementation.version.major} version.')
else:
    raise NotImplementedError(f'No implement pymac for platform {platform}.')
