from macros import *
from cocos.rect import *


class Model(MapConfig):
    def __init__(self):
        self.marks = []

    def push_marks(self, mark_rect):
        self.marks.append(mark_rect)

    def is_out(self, car):
        rect = Rect(car.x, car.y, 1, 1)
        return not self.crash_rect.intersects(rect)

    def inters_mark(self, car):
        car_rect = Rect(car.x - car.width / 2, car.y - car.height / 2, car.width, car.height)
        for mark_rect in self.marks:
            if mark_rect.intersects(car_rect):
                return True

        return False
