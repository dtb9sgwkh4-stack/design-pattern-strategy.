class Transport:
    def go_to_airport(self):
        pass


class Car(Transport):
    def go_to_airport(self):
        print("Едем в аэропорт на машине")


class Taxi(Transport):
    def go_to_airport(self):
        print("Едем в аэропорт на такси")


class Bus(Transport):
    def go_to_airport(self):
        print("Едем в аэропорт на автобусе")


class Traveler:
    def __init__(self, transport):
        self.transport = transport

    def go_to_airport(self):
        self.transport.go_to_airport()


car = Car()
traveler = Traveler(car)
traveler.go_to_airport()

taxi = Taxi()
traveler = Traveler(taxi)
traveler.go_to_airport()

bus = Bus()
traveler = Traveler(bus)
traveler.go_to_airport()
