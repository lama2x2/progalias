from Core.Game import Game
from Core.Scene import Scene
from UIObjects.Button import Button
from Scenes.DifficultyMenu import DifficultyMenu


class Menu(Scene):
    def __init__(self, game: Game = None):
        super().__init__(game)

    def init_UI(self):
        center = self._game.width // 2, self._game.height // 2

        size = width, height = 200, 100
        position = center[0] - width // 2, center[1] - height // 2
        self.play_button = Button(position, size, (200, 200, 200), self, "ok, let`s go", font_size=45)

    def connect_buttons(self):
        self.play_button.on_click = self.play_button_on_click

    def play_button_on_click(self):
        difficulty_menu = DifficultyMenu(self.game)
        self.game.set_scene_active(difficulty_menu)
