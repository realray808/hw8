import json

import Park
import Customer


f = open("file1.json")
data = json.loads(f.read())
customer = data["Customer"]
station = data["Station"]


def simulate(customers, max_station):
    customers_instance = []
    for i, c in enumerate(customers):
        customers_instance.append(Customer.Customer(c[0], c[1], i + 1))

    iteration = 1
    while iteration < 3:
        park = Park.Park(max_station, customer_instance=customers_instance)
        print(park)
        print("End of Iteration %d" % iteration)
        for i in park.park_customer:
            if i.cur_station == park.tram.cur_station:
                i.on_tram = True
                i.cur_station += 1
        park.tram.move()
        iteration += 1


if __name__ == '__main__':
    simulate(customer, station)