from service import FlightService
from flight import Flight

service = FlightService("flights.db")

service.create_flight(Flight(0,137,"137"))
service.create_flight(Flight(0,371,"227"))
service.create_flight(Flight(0,731,"227"))
service.create_flight(Flight(0,111,"137"))
service.create_flight(Flight(0,333,"227"))

print(service.get_all())

service.delete_flight(1)

print(service.get_by_id(4))

for i in range(0, 90):
    service.delete_flight(i)

print(service.get_all())



