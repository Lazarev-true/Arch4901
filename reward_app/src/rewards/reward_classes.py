from abstracts.abstract_classes import IGameItem


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class Weapon(IGameItem):
    def open(self):
        print('Weapon!')


class Armour(IGameItem):
    def open(self):
        print('Armour!')


class Potion(IGameItem):
    def open(self):
        print('Potion!')


class Exp(IGameItem):
    def open(self):
        print('Exp!')


class Jewerly(IGameItem):
    def open(self):
        print('Jewerly!')
