from typing import TYPE_CHECKING

from Difficulties import Difficulty
from GameModes import GameMode
from Words import WORDS

from Core.Scene import Scene
from UIObjects.Button import Button
from UIObjects.Text import Text

if TYPE_CHECKING:
    from Core.Game import Game


class PlayScene(Scene):
    def __init__(self, difficulty: Difficulty, game_mode: GameMode, teams: list[str], game: 'Game' = None):
        self.difficulty = difficulty
        self.game_mode = game_mode
        self.teams = teams
        super().__init__(game)

        # self.teams: list[str] = []
        self.not_used_words = WORDS.copy()

    def init_UI(self):
        center = self._game.width // 2, self._game.height // 2

        size = width, height = 200, 100
        position = x, y = center[0] - width // 2, center[1] - height // 2

        self.ready_button = Button(position, size, (200, 200, 200), self, "Готовы?")

        self.skip_button = Button((20, self.game.height - height - 20), size, (200, 200, 200), self, "Пропустить")
        self.skip_button.is_active = False

        self.ok_button = Button((self.game.width - width - 20, self.game.height - height - 20), size, (200, 200, 200), self, "Ок")
        self.ok_button.is_active = False

        self.label = Text((0, 20), (self.game.width, 75), self, "{} минут осталось", font_size=75)

    def pick_word(self):
        pass

    def connect_buttons(self):
        self.ready_button.on_click = self.ready_button_on_click
        self.skip_button.on_click = self.skip_button_on_click
        self.ok_button.on_click = self.ok_button_on_click

    def ready_button_on_click(self):
        self.ready_button.is_active = False
        self.skip_button.is_active = True
        self.ok_button.is_active = True

    def skip_button_on_click(self):
        print("SKIP")

    def ok_button_on_click(self):
        print("OK")
