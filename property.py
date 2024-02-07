class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be greater than 0.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be greater than 0.")

    @property
    def area(self):
        return self._width * self._height

def main():

    my_rectangle = Rectangle(width=4, height=6)

    print(f"Width: {my_rectangle.width}")
    print(f"Height: {my_rectangle.height}")
    print(f"Area: {my_rectangle.area}")

if __name__ == "__main__":
    main()
