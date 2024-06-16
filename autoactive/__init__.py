from .wayland_patch import patch_wayland
patch_wayland()

from .autoactive import main_loop
from .version import __version__


__all__ = ["__version__", "main_loop"]
