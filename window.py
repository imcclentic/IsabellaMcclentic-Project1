import arcade

class comp151Window(arcade.window):
    def __init__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.player = None
        self.targets = []
        self.score = 0

    def setup(self):
        pass

    def on_update(self):
        pass

    def on_draw(self):
        arcade.start_render()
        #Draw Here
        arcade.finish_render()