import app
from . import fleur as fleur
import asyncio

from events.input import Buttons, BUTTON_TYPES
from system.patterndisplay.events import *
from system.eventbus import eventbus
from tildagonos import tildagonos


class ScoutsApp(app.App):
    screen_size = ((-120, -120), (240, 240))
    on_color = (220, 11, 141)
    color: tuple[int, int, int] = on_color
    on: bool = True
    party_task = None

    def __init__(self):
        self.button_states = Buttons(self)
        eventbus.emit(PatternDisable())
        tildagonos.init_display()
        self.draw_fleur()

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["RIGHT"]):
            self.toggle()
        if self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.draw_fleur()
        elif self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()

    def draw(self, ctx):
        ctx.save()
        # ctx.font_size = 20
        # ctx.text_align = ctx.CENTER
        # ctx.text_baseline = ctx.MIDDLE
        ctx.rgb(
            self.color[0],
            self.color[1],
            self.color[2],
        ).rectangle(
            self.screen_size[0][0],
            self.screen_size[0][1],
            self.screen_size[1][0],
            self.screen_size[1][1],
        ).fill()

        ctx.restore()

    def toggle(self):
        self.color = self.on_color if self.color == (0, 0, 0) else (0, 0, 0)
        self.on = not self.on

    def draw_fleur(self):
        tildagonos.tft.bitmap(se, 60, 70)

__app_export__ = ScoutsApp