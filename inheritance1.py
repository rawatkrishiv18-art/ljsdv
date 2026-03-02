class vehicle:

    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

class bus(vehicle):
    pass

school_bus = bus("school volvo",180,12)
print("Vehicle Name:",school_bus.name,"Speed:",school_bus.max_speed,"Milage:",school_bus.milage)
