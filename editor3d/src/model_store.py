from src.service import Point3D, Angle3D, Color


class Texture:
    pass


class Polygon:
    Point3D = []


class PolygonalModel:
    def __init__(self, textures: list[Texture]):
        self.textures = textures
        self.polygons = []


class Flash:
    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:
    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    def __init__(self, id, models: list[PolygonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id_ = id

        if len(models) > 0:
            self.models = models
        else:
            raise ValueError('Должна быть одна модель')

        self.flashes = flashes

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise ValueError('Должна быть одна камера')

    @staticmethod
    def method1(flash):
        return flash

    @staticmethod
    def method2(model, flash):
        return model or flash
