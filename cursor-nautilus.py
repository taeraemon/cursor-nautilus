# Cursor Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to cursor
CURSOR = '/opt/cursor/cursor.AppImage'

# what name do you want to see in the context menu?
CURSORDNAME = 'Cursor'

# always create new window?
NEWWINDOW = False


class CursorExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_cursor(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of cursor
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(CURSOR + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='CursorOpen',
            label='Open in ' + CURSORDNAME,
            tip='Opens the selected files with Cursor'
        )
        item.connect('activate', self.launch_cursor, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='CursorOpenBackground',
            label='Open in ' + CURSORDNAME,
            tip='Opens the current directory in Cursor'
        )
        item.connect('activate', self.launch_cursor, [file_])

        return [item]
