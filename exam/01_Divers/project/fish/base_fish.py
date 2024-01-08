from abc import ABC, abstractmethod


class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Fish name should be determined!")
        self._name = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if not 1 <= value <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self._points = value

    @property
    def time_to_catch(self):
        return self._time_to_catch

    @time_to_catch.setter
    def time_to_catch(self, value):
        self._time_to_catch = value

    @abstractmethod
    def fish_details(self):
        pass
