from Keys import Keys
import random
import time


class Keyboard(object):
    def __init__(self):
        self.__keys = Keys()

    def press_a_key(self, KEY):
        self.__keys.directKey(KEY, self.__keys.key_press)
        time.sleep(random.uniform(0.02, 0.04))
        self.__keys.directKey(KEY, self.__keys.key_release)
        time.sleep(random.uniform(0.2, 0.9))

    def press_key_sequence(self, key_sequence):
        [self.press_a_key(KEY=KEY) for KEY in key_sequence]
