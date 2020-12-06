import Customer
import Tram


class Park:
    def __init__(self, max_station, customers):
        self.max_station = max_station
        self.tram = Tram.Tram(max_station)
        self.park_customer = customers

    def __str__(self):
        status = "\n" + "\n" + \
            "------------------------------------------------------------\n" + \
            " Station                  Customer                   Tram   \n" + \
            "------------------------------------------------------------\n"
        for i in range(self.max_station, 0, -1):
            for c in self.park_customer:
                if