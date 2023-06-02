from elisteners import KeyboardListener, MouseListener
from screentool import ImageTool
from configurer import *


class Connector:
    def __init__(self):
        self.klistener = None
        self.mlistener = None
        self.imagetool = None

    def on_translation_hotkey(self):
        self.imagetool = ImageTool(ImageTool.obtain_screenshot()) if self.imagetool is None else self.imagetool.update()
        self.imagetool.show_translation()

        self.mlistener = MouseListener(self.imagetool)
        self.mlistener.enable()

    def runapp(self):
        self.klistener = KeyboardListener(self)
        self.klistener.enable()