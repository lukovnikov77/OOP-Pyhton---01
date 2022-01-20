class Rectangle:
    def __init__(self):
        self.length = 1
        self.width = 1
    #  Setters
    def set_width(self, width):
        self.width = width
    def set_length(self, length):
        self.length = length
    #  Getters
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    # find area and perimetr
    def find_area(self):
        return self.length * self.width
    def find_perimetr (self):
        return 2 * (self.width + self.length)

    # show String of values
    def __str__(self):
        return 'length = {}, width = {}'.format(self.length, self.width)

rectangle1 = Rectangle()
# set width and length of rectangle1 object
rectangle1.set_width(5)
rectangle1.set_length(6)
# call find_area and find_perimetr methods
ar = rectangle1.find_area();
pr = rectangle1.find_perimetr();
print(rectangle1)
# show results
print("Area = ",ar)
print ("Perimetr = " , pr)