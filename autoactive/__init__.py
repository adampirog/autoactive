from autoactive.wayland_patch import patch_wayland


patch_wayland()

from autoactive.autoactive import main_loop
from autoactive.version import __version__


__all__ = ["__version__", "main_loop"]
