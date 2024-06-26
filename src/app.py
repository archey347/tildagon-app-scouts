import app as app
import sys
import os
import time

from app_components import clear_background
from events.input import Buttons, BUTTON_TYPES
from tildagonos import tildagonos
from system.eventbus import eventbus
from system.patterndisplay.events import *

LEDS = 12

SCOUTS_PURPLE = (116, 20, 220)
SCOUTS_TEAL = (6, 132, 134)
SCOUTS_RED = (237, 64, 36)
SCOUTS_GREEN = (38, 183, 86)
SCOUTS_NAVY = (0, 58, 130)
SCOUTS_BLUE = (0, 110, 224)
SCOUTS_PINK = (255, 180, 229)
SCOUTS_YELLOW = (255, 230, 39)
SCOUTS_ORANGE = (255, 145, 42)
SCOUTS_FOREST_GREEN = (32, 91, 65)

SE_DARK_GREEN = (120, 146, 75)
SE_LIGHT_GREEN = (183, 213, 67)

if sys.implementation.name == "micropython":
    apps = os.listdir("/apps")
    path = ""
    for a in apps:
        # This is important for apps deployed to the appstore
        # The Snake app from naomi stored at
        # https://github.com/npentrel/tildagon-snake/
        # has all its files in the folder
        # npentrel_tildagon_snake
        if a == "scouts":
            path = "/apps/" + a
    ASSET_PATH = path + "/"
else:
    # while testing, put your files in the folder you are developing in,
    # for example: example/streak.jpg
    ASSET_PATH = "apps/example/"


class Slide:
    def draw(self, ctx):
        raise "Not implemented"

class Fleur(Slide):
    def draw(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "fleur.jpg", -90, -80, 180, 164)

        for i in range(LEDS):
            tildagonos.leds[i + 1] = SCOUTS_PURPLE
        
        tildagonos.leds.write()


class SE(Slide):
    def draw(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "se.jpg", -99, -100, 198, 200)

        for i in range(LEDS):
            tildagonos.leds[i + 1] = SE_DARK_GREEN
        
        tildagonos.leds.write()
        
class Cake(Slide):
    def draw(self, ctx):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "cake.jpg", -80, -80, 160, 160)

        for i in range(LEDS):
            tildagonos.leds[i + 1] = SCOUTS_ORANGE
        
        tildagonos.leds.write()



class SlideApp(app.App):
    def __init__(self):
        eventbus.emit(PatternDisable())
        self.slides = [Fleur(), SE(), Cake()]
        self.image_index = 0
        self.wait = 4
        self.last_change = time.time()
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()

        if self.last_change + self.wait < time.time():
            self.image_index = (self.image_index + 1) % len(self.slides)
            self.last_change = time.time()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.save()
        self.slides[self.image_index].draw(ctx)
        ctx.restore()

__app_export__ = SlideApp
