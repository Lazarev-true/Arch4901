from src.car import *
from src.pickup import PickUp


class App:
    def main(self):
        pickup_1 = PickUp("nissan", "skyline", Color(1), TypeCar(1), 0, TypeFuel(1), TypeGearBox(1), 1.1, 1000)
        pickup_1.fuel()

if __name__ == '__main__':
    app_1 = App()
    app_1.main()
