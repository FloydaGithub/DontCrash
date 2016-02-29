import cocos
from cocos.rect import *

class WorldMap(cocos.layer.ScrollableLayer):
    is_event_handler = False

    def on_enter(self):
        super(WorldMap, self).on_enter()

    def __init__(self, world_width, world_height, model):
        self.world_width = world_width
        self.world_height = world_height
        self.model = model
        super(WorldMap, self).__init__()

        self.px_width = world_width
        self.px_height = world_height

        #dummy objects in the world: a big framed background and squares
        bg = cocos.layer.ColorLayer(170,
                                    170,
                                    0,
                                    255,
                                    width=world_width,
                                    height=world_height)
        self.add(bg, z=0)
        margin = int(world_width * 0.01)
        #print 'margin',margin
        self.margin = margin
        bg = cocos.layer.ColorLayer(0,
                                    170,
                                    170,
                                    255,
                                    width=world_width - 2 * margin,
                                    height=world_height - 2 * margin)
        bg.position = (margin, margin)
        self.add(bg, z=1)

        mod = (world_width - 2.0 * margin) / 10.0
        #print mod
        y = margin + mod
        # self.marks_positions = []
        while y < world_height - mod:
            x = margin + mod
            while x < world_width - mod:
                red = 55 + int(200.0 * x / world_width)
                blue = 55 + int(200.0 * y / world_height)
                actor = cocos.layer.ColorLayer(red,
                                               0,
                                               blue,
                                               255,
                                               width=2 * int(mod),
                                               height=2 * int(mod))
                actor.position = x, y
                self.model.push_marks(Rect(x, y, 2 * int(mod), 2 * int(mod)))
                self.add(actor, z=3)
                x += 3 * mod
            y += 3 * mod
