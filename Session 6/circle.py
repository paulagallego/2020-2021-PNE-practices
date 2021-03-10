class Circle:
    """Circle class"""
    all_circles = []
    pi = 3.14159

    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the circle"""
        return self.__class__.pi * self.radius * self.radius

    @staticmethod
    def total_area():
        """static method to total the areas of all circles"""
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total