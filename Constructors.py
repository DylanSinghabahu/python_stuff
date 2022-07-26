class Fish:
    def __init__(self, x, y): #creates an object: init --> initialise
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("self")

point = Fish(10, 20)
point.x = 10
print(point.x)


