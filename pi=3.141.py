class Circle:
    # Private class variable
    pi = 3.141

    def __init__(self, radii_list):
        self.radii = radii_list
        self.areas = self.calculate_areas()

    def calculate_areas(self):
        # Calculate areas based on radii
        areas = [self.pi * r**2 for r in self.radii]
        return areas

# Example usage
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Accessing the radii list and calculated areas
print("Radii List:", circle_instance.radii)
print("Calculated Areas:", circle_instance.areas)
