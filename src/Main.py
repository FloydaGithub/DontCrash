from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
#

import pyglet
from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.scenes.transitions import *
from cocos.actions import *

from macros import *
import Sound


# menu items effect
def rotate_effect():
    angle = 360
    duration = 0.5
    return Accelerate(RotateBy(angle, duration), 0.15)


def rotate_effect_back():
    return RotateTo(0, 0.01)
#


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("Don't Crash")
        self.select_sound = Sound.load('move.mp3')

        # add the items
        items = [
            (MenuItem('Play Game', self.on_play_game)),
            (MenuItem('Setting', self.on_setting)),
            (MenuItem('Quit', self.on_quit)),
        ]

        # set title params
        self.font_title['font_size'] = 78
        self.font_title['color'] = (250, 0, 0, 255)
        self.font_title['bold'] = True
        self.font_title['italic'] = True
        self.font_item['color'] = (255, 255, 255, 144)

        item_margin = 60
        cx = Display.cx
        cy = Display.cy
        self.create_menu(items,
                         selected_effect=rotate_effect(),
                         unselected_effect=rotate_effect_back(),
                         layout_strategy=fixedPositionMenuLayout([
                             (cx, cy + item_margin),
                             (cx, cy),
                             (cx, cy - item_margin),
                         ]))

    def on_play_game(self):
        import GameScene
        director.replace(ShuffleTransition(GameScene.get_scene(), 0.5))

    def on_setting(self):
        print("Setting")

    def on_quit(self):
        pyglet.app.exit()

def main():
    pyglet.resource.path.append('res')
    pyglet.resource.reindex()
    director.init(width=Display.width, height=Display.height)
    director.set_show_FPS(Config.debug)
    director.run(Scene(MainMenu()))

def test_main():
    main()

if __name__ == '__main__':
    main()