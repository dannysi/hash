class Street(object):
    def __init__(self, from_int, to_int, name, length):
        self.from_int = from_int
        self.to_int = to_int
        self.name = name
        self.length = length

    def String(self):
        print("street", self.name, self.from_int, self.to_int, self.length)


class StopLight(object):
    def __init__(self, s_intersection, s_street, s_cars):
        self.s_intersection = s_intersection
        self.s_street = s_street
        self.s_cars = s_cars
        self.schedule = []

    def add_car(self, car):
        self.s_cars.append(car)

    def String(self):
        print("intersection", self.s_intersection, "street", self.s_street, "cars", self.s_cars)

    def add_schedule(self, street, time):
        self.schedule.append((street, time))



class Car(object):
    def __init__(self,id , route):
        self.route = route

    def String(self):
        print("car", self.route)


class Intersection(object):
    def __init__(self, name):
        self.name = name
        self.to_street = []
        self.from_street = []
        self.stoplights = []

    def add_to(self, street):
        self.to_street.append(street)

    def add_from(self, street):
        self.from_street.append(street)

    def add_stoplight(self, stoplight):
        self.stoplights.append(stoplight)

    def String(self):
        print("intersection", self.name, "from:", self.from_street, "to", self.to_street)


def read_from_file(file):
    f = open(file, "r")
    time, intersection_len, streets_len, cars_len, score = f.readline().split()
    streets = []
    cars = []

    for _ in range(int(streets_len)):
        from_int, to_int, name, length = f.readline().split()
        streets.append(Street(int(from_int), int(to_int), name, int(length)))

    for i in range(int(cars_len)):
        _, route = f.readline().split(maxsplit=1)
        cars.append(Car(i, route.split()))
    intersections = []
    for i in range(int(intersection_len)):
        intersections.append(Intersection(i))
    for street in streets:
        intersections[street.from_int].add_from(street.name)
        intersections[street.to_int].add_to(street.name)

    stoplights = init_stoplights(streets, cars, intersections)

    return streets, cars, intersections, score, stoplights


def init_stoplights(i_streets, i_cars, i_intersections):
    t_streets = dict()
    stoplights = []
    for car in i_cars:
        for street_name in car.route:
            if street_name not in t_streets.keys():
                t_streets[street_name] = [car]
            else:
                t_streets[street_name].append(car)

    for inters in i_intersections:
        for from_street in inters.from_street:
            stoplight = StopLight(inters, from_street, t_streets[from_street])
            stoplights.append(stoplight)
            inters.add_stoplight(stoplight)
    return stoplights


streets, cars, intersections, score, stoplights = read_from_file("a.txt")

for street in streets:
    street.String()
for car in cars:
    car.String()
for intersection in intersections:
    intersection.String()

for stoplight in stoplights:
    stoplight.String()

