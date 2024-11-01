import tkinter as tk
from tkinter import messagebox
from base import Sphere, Diamond

class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Shape Generator")

        self.shape_label = tk.Label(root, text="Select Shape:")
        self.shape_label.pack()
        self.shape_var = tk.StringVar(value="sphere")
        self.shape_menu = tk.OptionMenu(root, self.shape_var, "sphere", "diamond")
        self.shape_menu.pack()

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

        self.colour_label = tk.Label(root, text="Colour:")
        self.colour_label.pack()
        self.colour_entry = tk.Entry(root)
        self.colour_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Shape", command=self.generate_shape)
        self.generate_button.pack()

    def generate_shape(self):
        try:
            shape_type = self.shape_var.get()
            colour = self.colour_entry.get() or 'blue'  # Default to 'blue' if empty

            if shape_type == "sphere":
                radius = float(self.radius_entry.get())
                shape = Sphere(radius, colour)
            elif shape_type == "diamond":
                base_length = float(self.base_length_entry.get())
                height = float(self.height_entry.get())
                shape = Diamond(base_length, height, colour)
            else:
                raise ValueError("Unsupported shape type")

            volume = shape.volume()
            surface_area = shape.surface_area()
            messagebox.showinfo("Shape Info", f"Volume: {volume:.2f}\nSurface Area: {surface_area:.2f}")
            shape.draw()

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
