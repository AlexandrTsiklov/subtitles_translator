import pytesseract
import numpy as np
import cv2

from configurer import *
from validator  import *


def prepare_image(image):
    gray_image = get_grayscale(image)                 # Преобразование в оттенки серого
    denoised_image = remove_noise(gray_image)         # Удаление шумов
    thresholded_image = thresholding(denoised_image)  # Применение порогового значения
    dilated_image = dilate(thresholded_image)         # Дилатация
    eroded_image = erode(dilated_image)               # Эрозия
    return eroded_image


def recognize(image):
    prepared_image = prepare_image(image)
    dirty_text = pytesseract.image_to_string(prepared_image, config=r'--oem 3 --psm 6')
    clean_text = validate(dirty_text)
    return clean_text.strip()


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)