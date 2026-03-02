class vihicle:
    def __init__(self, vehicletype):
        print("vehicles is a ", vehicletype)

class car(vihicle):
    def __init__(self):
        vihicle.__init__(self, "car")

print(issubclass(car, vihicle))
print(isinstance(car , list))
print(isinstance(car , car))
print(isinstance(car,(car , vihicle)))