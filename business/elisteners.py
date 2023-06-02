import keyboard

from screentool import ImageTool
from notiontool import *
from configurer import *



class MouseListener:

    def __init__(self, imagetool):
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        self.imagetool: ImageTool = imagetool
        self.drawing = False
        self.enabled = False

    def check_events(self):
        key = cv2.waitKey(10)  
        if key == ord('q'):
            NotionConnector.send_to_list(NotionUrls.newC1_url)
        if key == ord(' ') or key == ord('q'):
            self.disable()

    def on_mouse_event(self, event, x: int, y: int, flags, param):
        if event == cv2.EVENT_RBUTTONDOWN:
            self.drawing = True
            self.imagetool.show_bareimage()
            self.x1, self.y1 = x, y

        elif event == cv2.EVENT_RBUTTONUP and self.drawing:
            self.drawing = False
            self.imagetool.show_translation(area=(self.x1, self.y1, self.x2, self.y2))

        elif event == cv2.EVENT_MOUSEMOVE:
            self.x2, self.y2 = x, y
            if not self.drawing:
                self.x1, self.y1 = x, y

    def enable(self):
        cv2.setMouseCallback("Image", self.on_mouse_event)
        self.enabled = True

        while self.enabled:
            self.check_events()
            if self.drawing:
                self.imagetool.clear_cladimage()
                self.imagetool.draw_rectangle(self.x1, self.y1, self.x2, self.y2)
                self.imagetool.show_cladimage()

    def disable(self):
        self.imagetool.close_image()
        self.drawing = False
        self.enabled = False


class KeyboardListener:
    def __init__(self, connector):
        self.connector = connector

    def on_translation_hotkey(self):
        self.connector.on_translation_hotkey()

    def enable(self):
        keyboard.add_hotkey('Ctrl + Z + X', self.on_translation_hotkey, suppress=False)
        keyboard.wait()