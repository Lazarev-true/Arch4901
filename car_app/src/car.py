from abc import ABC, abstractmethod
from src.color import Color
from src.type_car import TypeCar
from src.type_fuel import TypeFuel
from src.type_gear_box import TypeGearBox


class Car(ABC):
    __name = ''
    __model = ''
    __color = Color(1)
    __body_type = TypeCar(1)
    __number_wheels = 0
    __fuel = TypeFuel(1)
    __gear_box = TypeGearBox(2)
    __engine_cap = 1.0

    def __init__(self, name, model, color, body_type, number_wheels, fuel, gear_box, engine_cap):
        super().__init__()
        self.__name = name
        self.__model = model
        self.__color = color
        self.__body_type = body_type
        self.__number_wheels = number_wheels
        self.__fuel = fuel
        self.__gear_box = gear_box
        self.__engine_cap = engine_cap

    def movement(self):
        pass

    def maintenance(self):
        pass

    @abstractmethod
    def gear_shift(self, int_arg):
        pass

    def turn_lights(self, int_arg):
        return True

    def turn_wgrs(self):
        return True

