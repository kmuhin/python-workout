class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __repr__(self):
        return f'Vector({self.x_comp}, {self.y_comp})'


vector = Vector(3, 4)
repr(vector)


b = eval(repr(vector))
type(b), b.x_comp, b.y_comp


vector  # Looking at object; __repr__ used