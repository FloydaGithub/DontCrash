from cocos.rect import *


class Config:
    debug = True


class Direction:
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    none = "none"


class Display:
    grid_num_x = 12
    grid_num_y = 8
    grid_size = 75
    window_margin = 50
    # width  = 960
    width = grid_num_x * grid_size + 2 * window_margin
    # height = 640
    height = grid_num_y * grid_size + 2 * window_margin
    cx = width / 2
    cy = height / 2


class Color:
    red = (255, 0, 0, 255)
    gray = (255, 255, 255, 44)


class Player:
    max_speed = 10


class MapConfig():
    width = 2000
    height = 2000
    margin = int(width * 0.01)
    crash_rect = Rect(margin * 2, margin * 2, width - margin * 4,
                      height - margin * 4)
    map_rect = Rect(margin, margin, width - margin * 2, height - margin * 2)
    world_rect = Rect(0, 0, width, height)
