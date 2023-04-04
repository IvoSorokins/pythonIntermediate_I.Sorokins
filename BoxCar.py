import Carriage


class BoxCar(Carriage):

    valid_cargo_types = ["cattle", "paper", "food"]

    def __init__(self, tare, length, volume, bc, cargo_type="cattle"):
        super().__init__(tare, length, volume)
        self.BC = f"BC-{bc}"
        self.cargo_type = cargo_type
        self.cargo_weight = 0

    def set_cargo_type(self, cargo_type):
        if self.cargo_type in BoxCar.valid_cargo_types:
            self.cargo_type = cargo_type
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - cattle!")

    def add_cargo(self, cargo_type, cargo_weight):
        if cargo_type in BoxCar.valid_cargo_types:
            self.cargo_type = cargo_type
            self.cargo_weight = cargo_weight
        else:
            print("\nInvalid cargo type! \nUsing default cargo type - cattle!")

    # Method that returns string that represents object
    def __repr__(self):
        return f"[Box Car] ID:{self.bc} Cargo type: {self.cargo_type} Volume:{self.volume}"