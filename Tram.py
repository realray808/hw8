class Tram:
    def __init__(self, max_stations):
        self.max_station = max_stations
        self.cur_station = 1

    def move(self):
        self.cur_station += 1

    def __str__(self):
        status = "The Tram is currently at station %d out of %d" % \
                 (self.cur_station, self.max_station)
        return status


if __name__ == '__main__':
    T = Tram(12)
    print(T)
    T.move()
    print(T)
