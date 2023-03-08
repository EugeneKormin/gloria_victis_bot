from Screen import Screen
from Mouse import Mouse
from Keys import Keys

import pytesseract
import time
import cv2


class FishingBot(object):
    def __init__(self):
        self.__screen = Screen(WINDOW_NAME="Gloria Victis")
        self.__mouse = Mouse()
        self.__keys = Keys()
        self.__execute()

    def __detect_direction(self, screen):
        img_text = screen[615:630, 650:710]
        gray_img = cv2.cvtColor(img_text, cv2.COLOR_BGR2GRAY)
        _, text_image = cv2.threshold(gray_img, 175, 255, cv2.THRESH_BINARY)
        TEXT = pytesseract.image_to_string(text_image)
        return TEXT

    def __start_fishing(self):
        self.__keys.directKey("6", self.__keys.key_press)
        time.sleep(0.04)
        self.__keys.directKey("6", self.__keys.key_release)

        time.sleep(1.5)

        self.__keys.directKey("0", self.__keys.key_press)
        time.sleep(0.04)
        self.__keys.directKey("0", self.__keys.key_release)

        time.sleep(1.5)

        self.__mouse.press_button()

    def __execute(self):
        self.__start_fishing()
        while True:
            screen = self.__screen.update_img()

            DIRECTION = self.__detect_direction(screen=screen)

            self.__mouse.move(DISTANCE=14, DIRECTION=DIRECTION)
