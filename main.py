import tkinter as tk
from tkinter import messagebox

from networkx import diamond_graph


import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Base Class
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

    def set_type(self, shape_type):
        self.__type = shape_type

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        self.__colour = colour

# Derived Class: Sphere
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

# Derived Class: Diamond (Two pyramids joined at the base)
class Diamond(Shape3D):
    def __init__(self, base_length, height, colour):
        super().__init__("diamond", colour)
        self.__base_length = base_length
        self.__height = height

    def volume(self):
        # Volume of two joined pyramids: (1/3) * Base_Area * Height * 2
        base_area = self.__base_length**2
        return (1/3) * base_area * self.__height * 2

    def surface_area(self):
        # Surface area approximation for diamond: 8 triangular faces
        slant_height = math.sqrt((self.__base_length / 2) ** 2 + self.__height ** 2)
        return 2 * self.__base_length * slant_height + self.__base_length ** 2

    def draw(self):
        # Drawing a 3D diamond as two pyramids joined at their base
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Define vertices for the two pyramids
        v = np.array([[0, 0, self.__height],         # Top vertex of first pyramid
                      [-self.__base_length/2, -self.__base_length/2, 0],  # Base vertices
                      [self.__base_length/2, -self.__base_length/2, 0],
                      [self.__base_length/2, self.__base_length/2, 0],
                      [-self.__base_length/2, self.__base_length/2, 0],
                      [0, 0, -self.__height]])       # Bottom vertex of second pyramid

        # Define the 8 triangular faces of the diamond
        faces = [[v[0], v[1], v[2]],
                 [v[0], v[2], v[3]],
                 [v[0], v[3], v[4]],
                 [v[0], v[4], v[1]],
                 [v[5], v[1], v[2]],
                 [v[5], v[2], v[3]],
                 [v[5], v[3], v[4]],
                 [v[5], v[4], v[1]]]

        # Plot the diamond
        ax.add_collection3d(Poly3DCollection(faces, facecolors=self.get_colour(), linewidths=1, edgecolors='r', alpha=.25))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()


class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Shape Generator")

        # Shape type label and dropdown
        self.shape_label = tk.Label(root, text="Select Shape:")
        self.shape_label.pack()
        self.shape_var = tk.StringVar(value="sphere")
        self.shape_menu = tk.OptionMenu(root, self.shape_var, "sphere", "diamond")
        self.shape_menu.pack()

        # Dimension inputs
        self.radius_label = tk.Label(root, text="Radius (for Sphere):")
        self.radius_label.pack()
        self.radius_entry = tk.Entry(root)
        self.radius_entry.pack()

        self.base_length_label = tk.Label(root, text="Base Length (for Diamond):")
        self.base_length_label.pack()
        self.base_length_entry = tk.Entry(root)
        self.base_length_entry.pack()

        self.height_label = tk.Label(root, text="Height (for Diamond):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        # Colour input
        self.colour_label = tk.Label(root, text="Colour:")
        self.colour_label.pack()
        self.colour_entry = tk.Entry(root)
        self.colour_entry.pack()

        # Generate button
        self.generate_button = tk.Button(root, text="Generate Shape", command=self.generate_shape)
        self.generate_button.pack()

    def generate_shape(self):
        try:
            shape_type = self.shape_var.get()
            colour = self.colour_entry.get()

            if shape_type == "sphere":
                radius = float(self.radius_entry.get())
                shape = Sphere(radius, colour)
            elif shape_type == "diamond":
                base_length = float(self.base_length_entry.get())
                height = float(self.height_entry.get())
                shape = diamond_graph(base_length, height, colour)
            else:
                raise ValueError("Unsupported shape type")

            volume = shape.volume()
            surface_area = shape.surface_area()
            messagebox.showinfo("Shape Info", f"Volume: {volume}\nSurface Area: {surface_area}")

            shape.draw()

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

# Run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
