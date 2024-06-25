import app as app
import sys
import os

from app_components import clear_background
from events.input import Buttons, BUTTON_TYPES

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


class ExampleApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()

    def draw(self, ctx):
        clear_background(ctx)
        ctx.save()
        ctx.image(ASSET_PATH + "fleur.jpg", -80, -80, 180, 164)
        ctx.restore()


__app_export__ = ExampleApp
