from src.model_store import PolygonalModel, Scene, Camera, Flash


class IModelChangedObserver:
    def apply_update_model(self):
        pass


class IModelChanger:
    def notify_change(self, sender):
        pass


class ModelStore(IModelChanger):
    def __init__(self, change_observer: list[IModelChangedObserver]):
        self.models = [PolygonalModel(None)]
        self.scenes = [Scene(0, self.models, self.flashes, self.cameras)]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self._change_observers = change_observer

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id_ == id:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
