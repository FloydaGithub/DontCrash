from cocos.scene import Scene

import pyglet
from pyglet.window import key

import cocos
from cocos import tiles, actions, layer
from cocos.director import director

from Map import *
from Model import *


class DriveCar(actions.Driver):
    def __init__(self, model):
        self.model = model
        self.inertia = 0
        super(DriveCar, self).__init__()

    def step(self, dt):
        # handle input and move the car
        self.target.rotation += (
            keyboard[key.RIGHT] - keyboard[key.LEFT]) * 150 * dt
        self.target.acceleration = (
            keyboard[key.UP] - keyboard[key.DOWN]) * 400

        if self.target.acceleration == 0:
            if self.inertia != 0:
                self.target.acceleration = -self.inertia
                if self.inertia > 0:
                    self.inertia -= 1
                else:
                    self.inertia += 1
                if abs(self.inertia) < 1:
                    self.inertia = 0
        else:
            # self.inertia = 0
            pass

        if keyboard[key.SPACE]:
            self.target.speed = 0
            self.inertia = 0
        super(DriveCar, self).step(dt)

        if not hasattr(self, "target"): return
        if self.model.is_out(self.target) or self.model.inters_mark(self.target):
            self.target.x, self.target.y = self.target.x_old, self.target.y_old
            self.target.speed = -self.target.speed
            self.inertia = self.target.speed
        else:
            self.target.x_old, self.target.y_old = self.target.x, self.target.y
        scroller.set_focus(self.target.x, self.target.y)


def get_scene():
    global keyboard, scroller
    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    model = Model()

    world_layer = WorldMap(2000, 2000, model)
    scroller = cocos.layer.ScrollingManager()
    scroller.add(world_layer)

    car_layer = layer.ScrollableLayer()
    car = cocos.sprite.Sprite('car.png')
    car_layer.add(car)
    car.position = (200, 100)
    # car.max_forward_speed = 200
    # car.max_reverse_speed = -100
    car.max_forward_speed = 400
    car.max_reverse_speed = -200
    car.do(DriveCar(model))
    scroller.add(car_layer)

    scene = Scene()
    scene.add(scroller)

    return scene
