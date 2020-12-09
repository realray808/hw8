import json

import Park


f = open("file1.json")
data = json.loads(f.read())
customer = data["Customer"]
station = data["Station"]


def simulate(customers, max_station):
    iteration = 1
    park = Park.Park(max_station, customers)
    print(park)
    print("End of Iteration %d" % iteration)
    park.tram.move()
    iteration += 1


if __name__ == '__main__':
    simulate(customer, station)