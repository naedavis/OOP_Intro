# class Cats:
#     def __init__(self, type, name, gender, colour, age):
#         self.type = type
#         self.name = name
#         self.gender = gender
#         self.colour = colour
#         self.age = age
#     def move(self):
#         print("I am a :" + self.type + "\n"+
#               "my name is :" + self.name + "\n"+
#               "My gener is :" + self.gender + "\n"+
#               "My colour is :" + self.colour + "\n"
#               "My age is : " + self.age)
# objCats=Cats("Lion", "White Lion", "female", "White", "5 years")
# objCats.name = "Mountain Lion"
# objCats.move()


#Exercise2
#class Shapes

#parent class that will be called in evey other class
#superclass
#"Shapes" = cLass name
class Shapes:
    #have to call the init constructor
    #self comes ther automatically
    #other properties/attributes are the ones you plan on using in this specific class later
    #init is a place where everything you're assigning stuff tois stored in 'memory"
    #type, name, size, side are all Attributes of class Shapes, every shape has these attributes
    def __init__(self, type, name, size, side):
        #you have to assign the attributes named to variables python will recognise
        #note how its always preceded by self
        self.type = type
        self.name = name
        self.size = size
        self.side = side
    ##this is the method you're going to use when you display the attributes you're gonna get
    #area is the method that is going to be used/ the Behaviour of the class shpes
    def area(self):
        #"\n" skips a line when the code/program is executed
        print("I am a " + self.type + "\n"+
            "Name is "+ self.name + "\n" +
            "size is " + self.size + "\n" +
            "number of sides " + self.side)
#object name can be anything, preferably start with "obj" so you know its an object
#call the class name you're going to use, the methods you wanna use.
#inside the brackets are the values given by a user to input into the able method
objShapes=Shapes("Quadrilateral", "square", "20cm", "5")
#object named will use the method area in the above class called area
objShapes.area()


#Subclass
class Circle(Shapes):
    #Shapes attributes will be inheritted therefore it'll show when this SubClass is called
    #radius is an extra attribute that was not inherited
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        #answer is declared to have the followinfg calculation
        answer = 3.14*int(self.radius)**2
        #same as above print, calls the previously declared calculation
        #must be converted to string bc calculation is in integer
        print("The area of circle is : "+ str(answer))
#object name declared
# is equal to the name of the Subclass Circle
#6 is the "input" from the user
objCircle = Circle(6)
objCircle.area()

class Triangle(Shapes):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        answer = (self.height*self.base)/2
        print("Area of triangle is "+ str(answer))
objTriangle = Triangle(5,8)
objTriangle.area()

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.width*self.length
        print("Area of Rectangle is " + str(area))
objRectangle = Rectangle(10, 7)
objRectangle.area()
class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        area = self.side**2
        print("Area of Square is :" + str(area))
objSquare = Square(5)
objSquare.area()
# class Circle(Shapes):
#     def __init__(self, radius):
#         self.radius = radius
#     def perimeter(self):
#         result = 2*3.14*self.radius
#         print( "Perimeter is " + str(result))
# objCoin = Circle(10)
# objCoin.perimeter()
#
# class Triangle(Shapes):
#     def __init__(self, side1, base, side):
#         self.side1 = side1
#         self.base = base
#         self.side = side
#     def perimeter(self):
#         answer = self.base + self.side + self.side1
#         print("Perimeter of " + str(answer))
# objPizza = Triangle(5,2,2)
# objPizza.perimeter()
#
# class Rectangle(Shapes):
#     def __init__(self, length, width):
















# Exercise1
# class bus
# class Bus:
#     def __init__(self, seats, colour, drivername):
#         self.seats = seats
#         self.colour = colour
#         self.drivername = drivername
#     def colourred(self):
#
#         # print("seats:" + self.seats + "\n"+
#         #   "colour:" + self.colour + "\n"+
#         #   "name:" + self.drivername)
#     def colourblue(self):
#         # print("seats:" + self.seats + "\n" +
#         #   "colour:" + self.colour + "\n" +
#         #   "name:" + self.drivername)
#
# objBus=Bus("9 seats", "black", "Robert")
# objBus.colour = "red"
