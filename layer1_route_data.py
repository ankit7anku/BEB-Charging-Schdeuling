# Layer I Route Information and Timetable Data Structure

class Layer1RouteData:
    def __init__(self):
        self.bus_routes = []  # List to hold all bus routes
        self.trip_schedules = []  # List to hold all trip schedules
        self.energy_consumption = {}  # Dictionary to hold energy consumption per trip
        self.depot_information = {}  # Dictionary to hold depot information

    def add_bus_route(self, route_id, route_details):
        self.bus_routes.append({'route_id': route_id, 'details': route_details})

    def add_trip_schedule(self, trip_id, schedule):
        self.trip_schedules.append({'trip_id': trip_id, 'schedule': schedule})

    def set_energy_consumption(self, trip_id, consumption):
        self.energy_consumption[trip_id] = consumption

    def set_depot_information(self, depot_id, info):
        self.depot_information[depot_id] = info

# Example usage:
# layer_data = Layer1RouteData()