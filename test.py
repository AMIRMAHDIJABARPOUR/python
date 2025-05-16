class Box:
    def __init__(self):
        self.width = 0  # ✅ Initialize width

    @property
    def get_width(self):
        return self.width  # ✅ Getter method

    @get_width.setter
    def get_width(self, value):  # ✅ Fix: Correct setter syntax
        if value <= 0:  # ✅ Validate input
            raise ValueError("Width must be greater than 0")
        self.width = value  # ✅ Assign new value


# Usage:
box1 = Box()
box1.get_width = int(input("Enter the width: "))  # ✅ Correct setter usage
print(box1.get_width)  # ✅ Retrieve the width
