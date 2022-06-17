class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.name == other.name and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        if self.name < other.name:
            return True
        if self.name > other.name:
            return False
        if self.x < other.x:
            return True
        if self.x > other.x:
            return False
        if self.y < other.y:
            return True
        if self.y > other.y:
            return False
        return False

    def __gt__(self, other):
        if self != other:
            return not(self < other)
        return False

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def __ge__(self, other):
        if self == other:
            return True
        return self > other

    def __str__(self):
        return f'{self.name}{self.get_coords()}'

    def __repr__(self):
        return f'Point(\'{self.name}\', {self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


points = [Point('A', 101, 1), Point('B', -1, 0),
          Point('A', 11, 0), Point('A', 111, -11)]
points.sort()
print(', '.join(map(str, points)))