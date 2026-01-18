
from Lesson9.workshop.Engine.Engine import Engine


class ElectricEngine(Engine):
    def __init__(self, power, battery_capacity):
        super().__init__(power)
        self.battery_capacity = battery_capacity

    def start(self):
        print(
            f"Starting electric engine"
            f"power: {self.power} HP"
            f"capacity: {self.battery_capacity}"
        )
