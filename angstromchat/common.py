import angstromchat
import os

def get_base_dir():
    if os.environ.get("ANGSTROMCHAT_BASE_DIR"):
        angstromchat_dir = os.environ.get("ANGSTROMCHAT_BASE_DIR")
    else:
        home_dir = os.path.expanduser("~")
        cache_dir = os.path.join(home_dir, ".cache")
        angstromchat_dir = os.path.join(cache_dir, "angstromchat")
    os.makedirs(angstromchat_dir, exist_ok=True)
    return angstromchat_dir