from Core.Scene import Scene
from Core.Game import Game
from UIObjects.Button import Button
from Difficulties import Difficulty
from Scenes.GameModeMenu import GameModeMenu


class DifficultyMenu(Scene):
    def __init__(self, game: Game = None):
        super().__init__(game)
        self.chosen_difficulty = None

    def init_UI(self):
        center = self._game.width // 2, self._game.height // 2

        size = width, height = 200, 100
        position = x, y = center[0] - width // 2, center[1] - height // 2

        self.easy_button = Button((x, y - height - 10), size, (200, 200, 200), self, "Легкий",
                                  font_size=40)

        self.normal_button = Button(position, size, (200, 200, 200), self, "Средний",
                                    font_size=40)

        self.hard_button = Button((x, y + height + 10), size, (200, 200, 200), self, "ТЯЖЕЛЫЙ",
                                  font_color=(225, 30, 30), font_size=40)

    def connect_buttons(self):
        self.easy_button.on_click = self.easy_button_on_click
        self.normal_button.on_click = self.normal_button_on_click
        self.hard_button.on_click = self.hard_button_on_click

    def easy_button_on_click(self):
        self.game.set_scene_active(GameModeMenu(self.game, Difficulty.EASY))
        self.chosen_difficulty = Difficulty.EASY

    def normal_button_on_click(self):
        self.game.set_scene_active(GameModeMenu(self.game, Difficulty.NORMAL))
        self.chosen_difficulty = Difficulty.NORMAL

    def hard_button_on_click(self):
        self.game.set_scene_active(GameModeMenu(self.game, Difficulty.HARD))
        self.chosen_difficulty = Difficulty.HARD
