import abc


class GameItemInterface(abc.ABC):
    @abc.abstractmethod
    def opening(self):
        pass


class ItemCreationInterface(abc.ABC):
    @abc.abstractmethod
    def item_creation(self):
        pass
