import time

from Screen import Screen
from Mouse import Mouse
from Keyboard import Keyboard

import pytesseract
import cv2


class FishingBot(object):
    def __init__(self):
        self.__screen = Screen(WINDOW_NAME="Gloria Victis")
        self.__mouse = Mouse()
        self.__keyboard = Keyboard()
        self.__IF_BOT_IS_SAFE = False
        self.__execute()

    def __detect_direction(self, screen):
        img_text = screen[615:630, 650:710]
        gray_img = cv2.cvtColor(img_text, cv2.COLOR_BGR2GRAY)
        _, text_image = cv2.threshold(gray_img, 175, 255, cv2.THRESH_BINARY)
        TEXT = pytesseract.image_to_string(text_image)
        return TEXT

    def __prepare_for_fishing(self):
        self.__keyboard.press_key_sequence(key_sequence=["6", "0", "e"])

    def __run_fishing_sequence(self):
        screen = self.__screen.update_img()
        DIRECTION = self.__detect_direction(screen=screen)
        self.__mouse.move(DISTANCE=14, DIRECTION=DIRECTION)

    def __check_if_bot_is_safe(self):
        return True

    def __execute(self):
        time.sleep(5)
        while True:
            PREV_STATUS = self.__IF_BOT_IS_SAFE
            self.__IF_BOT_IS_SAFE = self.__check_if_bot_is_safe()

            if PREV_STATUS is False and self.__IF_BOT_IS_SAFE:
                self.__prepare_for_fishing()

            while self.__IF_BOT_IS_SAFE:
                self.__run_fishing_sequence()
