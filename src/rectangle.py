
class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class UUIDRectangle(Rectangle):
    def __init__(self, x, y, width, height, uuid):
        super().__init__(x, y, width, height)
        self.assigned_to_set = False
        self.uuid = uuid
