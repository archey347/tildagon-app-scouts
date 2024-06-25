import app
from . import fleur as fleur
from tildagonos import tildagonos

from events.input import Buttons, BUTTON_TYPES

class ScoutsApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays
            # open. Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        ctx.save()
        tildagonos.tft.bitmap(fleur, 50, 50)
        ctx.restore()

__app_export__ = ScoutsApp