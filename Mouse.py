from Keys import Keys
from time import sleep
import random


class Mouse(object):
    def __init__(self):
        self.__keys = Keys()

    def __move_left(self, DISTANCE):
        for i in range(DISTANCE):
            self.__keys.directMouse(-1 * i, 0)
            sleep(random.uniform(0.03, 0.05))

    def __move_right(self, DISTANCE):
        for i in range(DISTANCE):
            self.__keys.directMouse(1 * i, 0)
            sleep(random.uniform(0.03, 0.05))

    def __move_up(self, DISTANCE):
        for i in range(DISTANCE):
            self.__keys.directMouse(0, -1 * i)
            sleep(random.uniform(0.03, 0.05))

    def __move_down(self, DISTANCE):
        for i in range(DISTANCE):
            self.__keys.directMouse(0, 1 * i)
            sleep(random.uniform(0.03, 0.05))

    def __move_mouse(self, DISTANCE, DIRECTION):
        if "left" in DIRECTION:
            self.__move_left(DISTANCE=DISTANCE)
            self.press_left_button()
            self.__move_right(DISTANCE=DISTANCE)

        elif "right" in DIRECTION:
            self.__move_right(DISTANCE=DISTANCE)
            self.press_left_button()
            self.__move_left(DISTANCE=DISTANCE)

        elif "up" in DIRECTION:
            self.__move_up(DISTANCE=DISTANCE)
            self.press_left_button()
            self.__move_down(DISTANCE=DISTANCE)

        elif "down" in DIRECTION:
            self.__move_down(DISTANCE=DISTANCE)
            self.press_left_button()
            self.__move_up(DISTANCE=DISTANCE)

    def press_left_button(self):
        self.__keys.directMouse(buttons=self.__keys.mouse_lb_press)
        sleep(random.uniform(0.06, 0.09))
        self.__keys.directMouse(buttons=self.__keys.mouse_lb_release)

    def press_right_button(self):
        self.__keys.directMouse(buttons=self.__keys.mouse_rb_press)
        sleep(random.uniform(0.06, 0.09))
        self.__keys.directMouse(buttons=self.__keys.mouse_rb_release)

    def move(self, DISTANCE: int, DIRECTION: str):
        self.__move_mouse(
            DISTANCE=random.randint(DISTANCE - 2, DISTANCE + 2),
            DIRECTION=DIRECTION
        )
