#Classes defines new types (points) to model real concepts
#We instead capitalise the first letter of every word

#Class --> Defines the blueprint of creating an object

#Object --> Represents a set of instances based on that blueprint

#Instances --> Specific representation of an object/class:

#For example, a program may have a class/object named Animal
#but there could be many instances of "Animal", such as lion, cat, and dog

class Sale:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Sale()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Sale()
point2.x = 1
print(point2.x)

#Classes --> Definew New types --> Types have methods to define body of the class
# + Attributes you can set anywhere