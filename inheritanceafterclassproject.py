class vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
class bus(vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def fare(self):
        total_fare = super().fare()
        maintanance_charge = total_fare * 0.1
        return total_fare + maintanance_charge

school_bus = bus(50)
print("Total Bus fare is:", school_bus.fare())