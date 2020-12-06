import json

import Customer
import Tram
# import Park


f = open("file1.json")
data = json.loads(f.read())
customer = data["Customer"]
station = data["Station"]

customer_init = []
customer_in_tram = []
for k, C in enumerate(customer):
    customer_init.append(Customer.Customer(C[0], C[1], k))
print(customer_init)

def simulate(customer, station):

