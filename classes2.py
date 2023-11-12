class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y = self.y + 1
        print(self.x, self.y)

    def move_right(self):
        self.x += 1
        print(self.x, self.y)

    def move_down(self):
        self.y -= 1
        print(self.x, self.y)

    def move_left(self):
        self.x -= 1
        print(self.x, self.y)

    def current_position(self):
        print(self.x, self.y)

test = Rocket()

test.move_up()
test.move_right()
test.move_down()
test.move_left()
test.current_position()
