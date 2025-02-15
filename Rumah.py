from ast import arg


class rumah:
    def __init__(self,color,room,floor,cost,large,location):
        self.color=color
        self.room=room
        self.floor=floor
        self.cost=cost
        self.large=large
        self.location=location
    def open(self):
        print("Buka Pintunya")

    def info(self):
        print("Color: ", self.color)
        print("Room: ", self.room)
        print("Floor: ", self.floor)
        print("Cost: ", self.cost, "USD")
        print("Large: ", self.large, "Meter")
        print("Location: ", self.location)

    def close(self):
        print("Tutup Pintunya")
    
rumahA1=rumah("brown","6 Rooms","2 Floors",1000,100,"Ocean Resident")
rumahA1.info()
rumahA1.open()
        