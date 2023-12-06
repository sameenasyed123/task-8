class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radii_list):
        self.radii = radii_list

    def calculate_area(self, radius):
        # Calculate and return the area of a circle
        return self.__pi * radius**2

    def calculate_perimeter(self, radius):
        # Calculate and return the perimeter (circumference) of a circle
        return 2 * self.__pi * radius

# Example usage
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Accessing the radii list and calculating area and perimeter
for radius in circle_instance.radii:
    area = circle_instance.calculate_area(radius)
    perimeter = circle_instance.calculate_perimeter(radius)
    print(f"For radius {radius}: Area = {area:.2f}, Perimeter = {perimeter:.2f}")
