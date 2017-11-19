# Used for creating, running and analyzing applescript and bash scripts.
import sys

from pokemonterminal.adapter import identify
from .wallpaper import get_current_adapters


def clear_terminal():
    adapter = identify()
    adapter.clear()


def change_terminal(image_file_path):
    if not isinstance(image_file_path, str):
        print("A image path must be passed to the change terminal function.")
        return
    adapter = identify()
    if adapter is None:
        print("Terminal not supported")
    adapter.set_image_file_path(image_file_path)


def change_wallpaper(image_file_path):
    if not isinstance(image_file_path, str):
        print("A image path must be passed to the change wallpapper function.")
        return
    providers = get_current_adapters()
    if len(providers) > 1:
        # All this if is really not supposed to happen at all whatsoever
        # really what kind of person has 2 simultaneous D.E???
        print("Multiple providers found select the appropriate one:")
        [print(str(x)) for x in providers]
        print("If some of these make no sense or are irrelevant please file" +
              "an issue in https://github.com/LazoCoder/Pokemon-Terminal")
        print("=> ", end='')
        inp = None
        while inp is None:
            try:
                inp = int(input())
                if inp >= len(providers):
                    raise ValueError()
            except ValueError as _:
                print("Invalid number, try again!")
        target = providers[inp]
    elif len(providers) <= 0:
        print("Your desktop environment isn't supported at this time.")
        sys.exit()
    else:
        target = providers[0]
    target.change_wallpaper(image_file_path)
