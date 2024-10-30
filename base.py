
class Shape3D:
    def __init__(self, shape_type, colour):
        self.__type = shape_type  
        self.__colour = colour  

    # Function placeholders for surface and volume 
    def volume(self):
        return None

    def surface_area(self):
        return None

    # Getter for type
    def get_type(self):
        return self.__type

    # Setter for type
    def set_type(self, shape_type):
        self.__type = shape_type

    # Getter for colour
    def get_colour(self):
        return self.__colour

    # Setter for colour
    def set_colour(self, colour):
        self.__colour = colour
