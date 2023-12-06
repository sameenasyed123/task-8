#take a class with a name of circle 

class Circle:
    # along with the constructor(radius)
    def __init__(self, radii_list):
        self.radii = radii_list

# list that given in qs
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Accessing the radii list
print(circle_instance.radii)
