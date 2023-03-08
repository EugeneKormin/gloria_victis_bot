# импортирование сторонних библиотек
import mss                                      # библиотека для получения фрейсов для дальнейшего анализа
from win32gui import GetWindowRect              # библиотека для получения положения изображения для анализа
from ctypes import windll                       # библиотека для нахождения окна по его имена
import numpy as np
import cv2
import hashlib
import datetime


# объявление класса Screen
class Screen(object):
    '''
    Все методы, связанные с обработкой изображений
    '''
    def __init__(self, WINDOW_NAME: str) -> None:
        '''
        Объявление переменных класса
        :param WINDOW_NAME: str: имя окна с игрой
        '''
        self.__array: np.ndarray
        # имя окна с игрой
        self.__WINDOW_NAME = WINDOW_NAME

    @staticmethod
    def __save_screen(Array: np.ndarray):
        now: str = str(datetime.datetime.now())
        HASH_NAME: str = hashlib.md5(now.encode()).hexdigest()
        np.save(f"./images/{HASH_NAME}", Array)

    @staticmethod
    def __grab(X: int, Y: int, W: int, H: int) -> np.ndarray:
        '''
        Получение фрейма для дальнейшего анализа
        :param X: int: координата верхней границы окна WINDOW_NAME
        :param Y: int: координата левой границы окна WINDOW_NAME
        :param W: int: ширина окна WINDOW_NAME
        :param H: int: высота окна WINDOW_NAME
        :return: ndarray: массив ndarray, отображающей фрейм для анализа
        '''
        # получение изображения в формате RGBA. Не особо понимаю, чего внутри библиотеки mss происходит ;-(
        with mss.mss() as sct:
            monitor: dict = {"top": Y, "left": X, "width": W, "height": H}
            # получаем массив np.ndarray в формате RGBA
            img_array: np.array = np.array(sct.grab(monitor))
            # конвертируем BGRA в BGR
            rgb_image_array: np.ndarray = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
            # возвращение значений
            return rgb_image_array

    def __getWindowRect(self, WINDOW_NAME: str) -> np.ndarray:
        '''
        Метод для получения местонахождения окна с именем WINDOW_NAME
        :param WINDOW_NAME: str: название окна для получения его местонахождения
        :return: None
        '''
        # получение номера окна с игрой
        HWND: int = windll.user32.FindWindowW(0, WINDOW_NAME)

        # получение координат с игрой
        rect: tuple[int, int, int, int] = GetWindowRect(HWND)

        # парсинг данных
        RECT_X: int = rect[0]
        RECT_Y: int = rect[1]
        RECT_W: int = rect[2]
        RECT_H: int = rect[3]
        array: np.ndarray = self.__grab(X=RECT_X, Y=RECT_Y, W=RECT_W, H=RECT_H)
        return array

    def update_img(self) -> np.ndarray:
        '''
        :return: np.ndarray: возвращение необработанного фрейма для дальнейшей обработки и анализа
        '''
        # получение нормализованного от 0 до 1 np.ndarray массив в формате RGB
        self.__array: np.ndarray = self.__getWindowRect(WINDOW_NAME=self.__WINDOW_NAME)
        return self.__array