import app as app
import sys
import os
import time
import math

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

WAIT = 10

def getT():
    return time.time_ns() / (1e9 * WAIT)

intensity = 1
colour = SCOUTS_PURPLE
last_colour = SCOUTS_PURPLE
last_change = getT()

if sys.implementation.name == "micropython":
    apps = os.listdir("/apps")
    path = ""
    for a in apps:
        # This is important for apps deployed to the appstore
        # The Snake app from naomi stored at
        # https://github.com/npentrel/tildagon-snake/
        # has all its files in the folder
        # npentrel_tildagon_snake
        if a == "archey347_tildagon_app_scouts" or a == "scouts":
            path = "/apps/" + a
    ASSET_PATH = path + "/assets/"

def set_colour(c):
    global colour
    global last_change
    global last_colour

    if c == colour:
        return

    last_change = getT()
    last_colour = colour
    colour = c

def set_leds(t):
    global colour
    global last_change
    global last_colour
    global intensity

    unit = 2 * 3.14159 / LEDS

    this_colour = colour

    # Smooth fade between colour changes
    transition = (getT() - last_change) * 10
    if transition < 1:
        transition_new = 1 - transition
        
        this_colour = (
            int(last_colour[0] * transition_new + colour[0] * transition),
            int(last_colour[1] * transition_new + colour[1] * transition),
            int(last_colour[2] * transition_new + colour[2] * transition)
        )

    for i in range(LEDS):
        rad = i * unit

        rad_t = t * 2 * 3.14159

        base_intensity = math.cos(rad + rad_t) ** 8

        base_intensity = base_intensity * intensity

        actual_colour = (int(this_colour[0] * base_intensity),
                         int(this_colour[1] * base_intensity),
                         int(this_colour[2] * base_intensity)
        )


        tildagonos.leds[i + 1] = actual_colour

    tildagonos.leds.write()

def up_intensity():
    global intensity

    if intensity == 0:
        intensity = 0.05

    intensity = min(1, intensity * 1.25)

def down_intensity():
    global intensity

    intensity = max(0.05, intensity / 1.25)

class Slide:
    def draw(self, ctx, t):
        raise "Not implemented"

class Fleur(Slide):
    def draw(self, ctx, t):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "fleur.jpg", -100, -91, 200, 182)

        set_colour(SCOUTS_PURPLE)
        set_leds(t)

class SE(Slide):
    def draw(self, ctx, t):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "se.jpg", -99, -100, 198, 200)

        set_colour(SE_DARK_GREEN)
        set_leds(t)
        
class Cake(Slide):
    def draw(self, ctx, t):
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.image(ASSET_PATH + "cake.jpg", -80, -80, 160, 160)

        set_colour(SCOUTS_ORANGE)
        set_leds(t)

class SlideApp(app.App):
    def __init__(self):
        eventbus.emit(PatternDisable())
        self.slides = [Fleur(), SE(), Cake()]
        self.last_change = time.time()
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.minimise()
            eventbus.emit(PatternEnable())
            self.button_states.clear()
        
        if self.button_states.get(BUTTON_TYPES["DOWN"]):
            down_intensity()
            self.button_states.clear()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            up_intensity()
            self.button_states.clear()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.save()

        t = getT()

        slide_index = int(t) % len(self.slides)
        self.slides[slide_index].draw(ctx, t)

        ctx.restore()

__app_export__ = SlideApp
