import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"Area of the circle: {circle.compute_area():.2f}")
    print(f"Perimeter of the circle: {circle.compute_perimeter():.2f}")