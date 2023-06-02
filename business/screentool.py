import numpy as np
import pyautogui

from recognizer import *
from translator import *


class TextUtils:
    
    @staticmethod
    def get_textsize(text: str):
        textsize, _ = cv2.getTextSize(text, FONT, FONT_SCALE, FONT_THICKNESS)
        return textsize[0], textsize[1]  # width, height

    @staticmethod
    def separate_lines(text: str):
        textlines, string = [], ''
        for i, char in enumerate(text):
            if (char == ' ' and len(string) >= MAX_CHARACTERS_PER_LINE) or (i == len(text) - 1):
                textlines.append(string)
                string = ''
            else:
                string += char
        return textlines

    @staticmethod
    def adjust_data(text: str, y_src: int):
        w, h = TextUtils.get_textsize(text)
        textlines = [text] if len(text) <= MAX_CHARACTERS_PER_LINE else TextUtils.separate_lines(text)
        return textlines, int(y_src * LINE_HEIGHT_ADJUST_COEFFICIENT) - h * len(textlines)



class ImageTool:
    def __init__(self, bareimage):
        self.bareimage = bareimage
        self.cladimage = bareimage.copy()
    
    @staticmethod
    def obtain_screenshot():
        return cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)

    @staticmethod
    def recognize_translate(image):
        nativetext = recognize(image)
        targettext = translate(nativetext, Language.English, Language.Russian)
        return targettext

    def overlay_text(self, text: str, y_src: int):               # y_src - y of top left corner of user's rectangle
        textlines, y_dst = TextUtils.adjust_data(text, y_src)    # list of strings, y_dst - y where the first string starts
        self.clear_cladimage()
        for textline in textlines:
            w, h = TextUtils.get_textsize(textline)              # width and height of the current text line                   # calculate x_src for center alighnment
            cv2.putText(self.cladimage, textline, ((SCREEN_WIDTH - w) // 2  , y_dst), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, LINE_THICKNESS)
            y_dst += (h * 2)

    def show_bareimage(self):
        cv2.imshow("Image", self.bareimage)

    def show_cladimage(self):
        cv2.imshow("Image", self.cladimage)

    def show_translation(self, area=(X1_DEFAULT, Y1_DEFAULT, X2_DEFAULT, Y2_DEFAULT)):
        x1, y1, x2, y2 = area
        cropped_image = self.bareimage[y1:y1 + abs(y2 - y1), x1:x1 + abs(x2 - x1)]
        self.overlay_text(ImageTool.recognize_translate(cropped_image), min(y1, y2))
        self.show_cladimage()

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int):
        cv2.rectangle(self.cladimage, (x1, y1), (x2, y2), FONT_COLOR, 3)

    def update(self):
        self.bareimage = ImageTool.obtain_screenshot()
        return self

    def clear_cladimage(self):
        self.cladimage = self.bareimage.copy()

    def close_image(self):
        cv2.destroyAllWindows()