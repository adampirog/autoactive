import subprocess

from Xlib.error import DisplayConnectionError


def patch_wayland():
    """
    Checks if the os runs the Wayland window manager and grants
    the program necessary permissions.
    """
    try:
        import pyautogui
    except DisplayConnectionError as exc:
        if "Authorization required" in str(exc):
            print("Detected Wayland problem.")
            grant_display_permissions()
        else:
            raise exc


def grant_display_permissions():
    print("Granting necessary permissions.")

    subprocess.run(["xhost", "+"], check=True)
