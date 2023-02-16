from Core.Scene import Scene
from Core.Game import Game
from UIObjects.Button import Button
from Scenes.PlayScene import PlayScene

from GameMode import GameMode, Difficulty


class GameModeMenu(Scene):
    def __init__(self, game: Game = None):
        super().__init__(game)
        self.game_mode = None

    def init_UI(self):
        size = width, height = 200, 100
        position = x, y = self.center[0] - width // 2, self.center[1] - height // 2

        self.easy_mode_button = Button((x, y - height - 10), size, (200, 200, 200), self, "Junior")
        self.normal_mode_button = Button(position, size, (200, 200, 200), self, "Middle")
        self.hard_mode_button = Button((x, y + height + 10), size, (200, 200, 200), self, "Senior")
        self.verbal_mode_button = Button((x, y + height * 2 + 80), size, (200, 200, 200), self, "Жестами")

    def connect_buttons(self):
        self.verbal_mode_button.on_click = self.verbal_mode_button_on_click
        self.easy_mode_button.on_click = self.easy_mode_button_on_click
        self.normal_mode_button.on_click = self.normal_mode_button_on_click
        self.hard_mode_button.on_click = self.hard_mode_button_on_click

    def verbal_mode_button_on_click(self):
        play_scene = PlayScene(GameMode(Difficulty.VERBAL, 3, 20), {'Красные': 0, 'Синие': 0}, self.game)
        self.game.set_scene_active(play_scene)

    def easy_mode_button_on_click(self):
        play_scene = PlayScene(GameMode(Difficulty.JUNIOR, 3, 20), {'Красные': 0, 'Синие': 0}, self.game)
        self.game.set_scene_active(play_scene)

    def normal_mode_button_on_click(self):
        pass

    def hard_mode_button_on_click(self):
        pass
