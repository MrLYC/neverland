
try:
    from .settings_default import *
except ImportError:
    pass

try:
    from .settings_extend import *
except ImportError:
    pass
