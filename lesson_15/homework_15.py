class Rhombus:
    def __init__(self, side_a, angle_a, angle_b):
        self.side_a = side_a
        if angle_a + angle_b != 180:
            raise ValueError("The sum of angles angle_a and angle_b should be 180°.")
        self.angle_a = angle_a
        self.angle_b = angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError('The length of the side should be > 0.')
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError('Angle should be in range between 0° and 180°.')
            super().__setattr__(key, value)
        elif key == 'angle_b':
            if not (0 < value < 180):
                raise ValueError('Angle should be in range between 0° and 180°.')
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)


# Checking
try:
    rhombus = Rhombus(5, 60, 120)
    print(f'Current rhombus parameters are: side - {rhombus.side_a}, angle_a - {rhombus.angle_a}, angle_b - {rhombus.angle_b}')
    print('-' * 50)

    # check length
    rhombus.side_a = -2
except ValueError as e:
    print(e)
    print('-' * 50)

try:
    # check angle
    rhombus.angle_a = 200
except ValueError as e:
    print(e)
    print('-' * 50)