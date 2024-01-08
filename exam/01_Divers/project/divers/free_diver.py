from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=120)

    def miss(self, time_to_catch: int):
        # Calculate the reduction based on 60% of time_to_catch
        reduction = int(0.6 * time_to_catch)
        reduction = max(reduction, 0)

        # Decrease oxygen level, ensuring it does not go below 0
        self.oxygen_level -= reduction

        if self.oxygen_level < 0:
            self.oxygen_level = 0  # Prevent oxygen level from going negative

        self.update_health_status()

    def renew_oxy(self):
        # Restore oxygen level to the initial value for FreeDiver
        self.oxygen_level = 120
