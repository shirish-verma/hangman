from datetime import datetime, date

class Cyclinder:
    def __init__(self, height, radius = 1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
    
    def get_surface_area(self):
        surface_area = round((2 * 22/7 * self.radius * self.height) + (2 * 22/7 * (self.radius ** 2)), 2)
        return surface_area

    def get_volume(self):
        volume = round((22/7 * (self.radius ** 2) * self.height), 2)
        return volume

    def __repr__(self):
        return f'This is a cylinder object with height of {self.height} and radius of {self.radius}.'

cylinder_1 = Cyclinder(5, 2)
print(cylinder_1)
print(f'The surface area for this cylinder is: {cylinder_1.surface_area}')
print(f'The volume for this cylinder is: {cylinder_1.volume}')


class Person: 
    def __init__(self, name, date_of_birth, friends):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.friends = friends
        self.age = self.age_func()
    
    def __str__(self):
        return f'{self.name} was born on {self.date_of_birth.strftime("%Y-%m-%d")} and has {len(self.friends)} friend(s).'
    
    def __repr__(self):
        return f'{self.name} was born on {self.date_of_birth} and is friends with {self.friends}'

    def age_func(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def __gt__(self, other):
        return self.age > other.age

    def add_friend(self, other):
        self.friends += other.friends
        other.friends = self.friends


person_1 = Person('Johnny Dogooder', '2000-01-01', ['Janet Dowondrous', 'Jack Dolittle'])
person_2 = Person('Jack Dolittle', '2020-01-01', ['Janet Dowondrous', 'Johnny Dogooder'])
person_new = Person('Tom', '2010-01-01', ['Dick', 'Harry'])
print(person_1)
print(person_2)
print(person_new)
print(person_1 > person_2)
print(person_2 > person_new)
print('')
print(person_1.friends)
print(person_new.friends)
person_1.add_friend(person_new)
print(person_1.friends)
print(person_new.friends)


class Shape:
    def __init__(self, num_sides, tesselates = None):
        self.num_sides = num_sides
        self.tesselates = tesselates
        self.valid_num = self.sides_check()

    def sides_check(self):
        if self.num_sides == 0:
            raise AttributeError ('Number of sides cannot be zero.')
        else:
            return True

    def get_info(self):
        raise NotImplementedError ("Please implement this method")

    def __str__(self):
        return self.get_info()

    def __add__(self, other):
        new_shape = self.num_sides + other.num_sides
        return Shape(new_shape)

    def __repr__(self):
        return f'sides = {self.num_sides}, tesselate = {self.tesselates}'

class Circle(Shape):
    def __init__(self):
        super().__init__(None, False)

    def get_info(self):
        return f'Circle | Total Sides: Circle has no sides, Tesselates = {bool(self.tesselates)}'

class Triangle(Shape):
    def __init__(self):
        super().__init__(3, True)
    def get_info(self):
        return f'Triange | Total Sides: {self.num_sides}, Tesselates = {bool(self.tesselates)}'

class Square(Shape):
    def __init__(self):
        super().__init__(4, True)
    def get_info(self):
        return f'Square | Total Sides: {self.num_sides}, Tesselates = {bool(self.tesselates)}'

class Pentagon(Shape):
    def __init__(self):
        super().__init__(5, False)
    def get_info(self):
        return f'Pentagon | Total Sides: {self.num_sides}, Tesselates = {bool(self.tesselates)}'

class Hexagon(Shape):
    def __init__(self):
        super().__init__(6, True)
    def get_info(self):
        return f'Hexagon | Total Sides: {self.num_sides}, Tesselates = {bool(self.tesselates)}'

shp_1 = Shape(10)
cir_1 = Circle()
tri_1 = Triangle()
sqr_1 = Square()
pen_1 = Pentagon()
hex_1 = Hexagon()

print(cir_1.get_info())
print(tri_1.get_info())
print(sqr_1.get_info())
print(pen_1.get_info())
print(hex_1.get_info())
print(cir_1)

poly_1 = tri_1 + sqr_1
poly_2 = tri_1 + hex_1
print(repr(poly_1))
print(type(poly_1))
print(repr(poly_2))
print(type(poly_2))