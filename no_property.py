class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be greater than 0.")

    def get_height(self):
        return self._height

    def set_height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be greater than 0.")

    def calculate_area(self):
        return self._width * self._height

def main():

    my_rectangle = Rectangle(width=4, height=6)

    print(f"Width: {my_rectangle.get_width()}")
    print(f"Height: {my_rectangle.get_height()}")
    print(f"Area: {my_rectangle.calculate_area()}")

if __name__ == "__main__":
    main()
