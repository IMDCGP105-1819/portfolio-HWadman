class Car(object):
    def __init__(self, color, manufacturer, model, doors):

        if type(color)!=str:
            raise Exception("color must be a string")
        if type(manufacturer)!=str:
            raise Exception("manufacturer must be a string")
        if type(model)!=str:
            raise Exception("model must be a string")
        if type(doors)!=int:
            raise Exception("doors must be a integer")

        self.color = color;
        self.manufacturer = manufacturer;
        self.model = model;
        self.doors = doors;

    def __str__(self):
        return str(f"The car is a {self.color} {self.manufacturer} {self.model}, and has {self.doors} doors.")

    def CarColor(self, color):
        self.color = color

    def CarManufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def CarModel(self, model):
        self.model = model

    def CarDoors(self, doors):
        self.doors = doors



myCar = Car("Blue","Volkswagen","Golf",200)
myCar.CarColor("Green")
myCar.CarManufacturer("BMW")
myCar.CarModel("i3")
myCar.CarDoors(8)
print(myCar)
