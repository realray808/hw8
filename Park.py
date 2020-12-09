import Customer
import Tram


class Park:
    def __init__(self, max_station, customers=None, customer_instance=None):
        self.max_station = max_station
        self.tram = Tram.Tram(max_station)
        if customer_instance is None and customers:
            self.park_customer = []
            for i, c in enumerate(customers):
                self.park_customer.append(Customer.Customer(c[0], c[1], i+1))
        else:
            self.park_customer = customer_instance

    def __str__(self):
        status = "\n" + "\n" + \
            "------------------------------------------------------------\n" + \
            " Station                  Customer                   Tram   \n" + \
            "------------------------------------------------------------\n"
        for i in range(self.max_station, 0, -1):
            waiting = []
            tram_stop = ""
            for customer in self.park_customer:
                if customer.cur_station == i:
                    waiting.append(str(customer.id))
            if self.tram.cur_station == i:
                tram_stop = "*T*"
            waiting_customer = " ".join(waiting)
            status += "    %d                        %s                       %s   \n" % (i, waiting_customer, tram_stop)
            if i != 1:
                status += "------------------------------------------------------------\n"
            else:
                status += "------------------------------------------------------------"
        return status


if __name__ == '__main__':
    park = Park(3, [[1, 2], [3, 1]])
    print(park)