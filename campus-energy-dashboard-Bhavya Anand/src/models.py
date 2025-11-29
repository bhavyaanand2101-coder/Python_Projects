class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, meter_reading):
        self.meter_readings.append(meter_reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return f"Building: {self.name}, Total Consumption: {total} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, meter_reading):
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(meter_reading)

    def generate_all_reports(self):
        return [b.generate_report() for b in self.buildings.values()]
