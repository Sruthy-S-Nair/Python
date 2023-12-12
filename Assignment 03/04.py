class Rectangle:
    def __init__(self, length, width):
        self.length = int(input("Enter the length of the rectangle: "))
        self.width = int(input("Enter the width of the rectangle: "))

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.Perimeter()}")
        print(f"Area: {self.Area()}")

# Create a rectangle object
rect = Rectangle(4, 5)

# Display the attributes and calculations
rect.display()
