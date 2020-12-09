class Customer:
    def __init__(self, start_station, final_station, identifier):
        self.start_station = start_station
        self.fin_station = final_station
        self.id = identifier
        self.cur_station = start_station
        self.on_tram = False

    def __str__(self):
        status = "Customer %d is at station %d and has destination %d" % \
                 (self.id, self.start_station, self.fin_station)
        return status


if __name__ == '__main__':
    C = Customer(7, 2, 1)
    print(C)
