import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Shape3D:
    def __init__(self, shape_type, colour):
        self.__type = shape_type  
        self.__colour = colour  

    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        pass

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

class Sphere(Shape3D):
    def __init__(self, radius, colour):
        super().__init__("sphere", colour)
        self.__radius = radius

    def volume(self):
        return (4/3) * math.pi * self.__radius**3

    def surface_area(self):
        return 4 * math.pi * self.__radius**2

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.__radius * np.outer(np.cos(u), np.sin(v))
        y = self.__radius * np.outer(np.sin(u), np.sin(v))
        z = self.__radius * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, color=self.get_colour())
        plt.show()

class Diamond(Shape3D):
    def __init__(self, base_length, height, colour):
        super().__init__("diamond", colour)
        self.__base_length = base_length
        self.__height = height

    def volume(self):
        base_area = self.__base_length**2
        return (1/3) * base_area * self.__height * 2

    def surface_area(self):
        slant_height = math.sqrt((self.__base_length / 2) ** 2 + self.__height ** 2)
        return 2 * self.__base_length * slant_height + self.__base_length ** 2

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        v = np.array([[0, 0, self.__height],        
                      [-self.__base_length/2, -self.__base_length/2, 0], 
                      [self.__base_length/2, -self.__base_length/2, 0],
                      [self.__base_length/2, self.__base_length/2, 0],
                      [-self.__base_length/2, self.__base_length/2, 0],
                      [0, 0, -self.__height]])       

        faces = [[v[0], v[1], v[2]],
                 [v[0], v[2], v[3]],
                 [v[0], v[3], v[4]],
                 [v[0], v[4], v[1]],
                 [v[5], v[1], v[2]],
                 [v[5], v[2], v[3]],
                 [v[5], v[3], v[4]],
                 [v[5], v[4], v[1]]]

        ax.add_collection3d(Poly3DCollection(faces, facecolors=self.get_colour(), linewidths=1, edgecolors='r', alpha=.25))
        plt.show()
