from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Diver name cannot be null or empty!")
        self._name = value

    @property
    def oxygen_level(self):
        return self._oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self._oxygen_level = value

    def miss(self, time_to_catch: int):
        # Decrease oxygen level based on the time_to_catch
        self.oxygen_level -= time_to_catch
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    @abstractmethod
    def renew_oxy(self):
        # To be implemented in derived classes
        pass

    def hit(self, fish: BaseFish):
        # Decrease oxygen level and add fish to catch list if oxygen is sufficient
        self.miss(fish.time_to_catch)
        if self.oxygen_level >= 0:
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)

    def update_health_status(self):
        # Toggle health status
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: "
                f"{len(self.catch)}, Points earned: {self.competition_points}]")
