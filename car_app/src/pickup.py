import zope.interface
from src.car import Car
from src.fueling import Fueling


@zope.interface.implementer(Fueling)
class PickUp(Car):
    __load_capacity = 0

    def __init__(self, name, model, color, body_type, number_wheels, fuel, gear_box, engine_cap, load_capacity):
        super().__init__(name, model, color, body_type, number_wheels, fuel, gear_box, engine_cap)
        self.__load_capacity = load_capacity

    def gear_shift(self, int_arg):
        return -int_arg

    def fuel(self):
        pass

    def wip_windshield(self):
        pass

    def wip_headlight(self):
        pass

    def wip_mirrors(self):
        pass
