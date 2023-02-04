from Core.Scene import Scene
from Core.Game import Game
from UIObjects.Button import Button
from Difficulties import Difficulty
from GameModes import GameMode
from Scenes.ChooseTeamMenu import ChooseTeamMenu


class GameModeMenu(Scene):
    def __init__(self, game: Game = None, difficulty: Difficulty = None):
        self.difficulty = difficulty
        super().__init__(game)
        self.game_mode = None

    def init_UI(self):
        center = self._game.width // 2, self._game.height // 2

        size = width, height = 200, 100
        position = center[0] - width // 2, center[1] - height // 2
        self.word_mode_button = Button(position, size, (200, 200, 200), self, "Словами")

    def connect_buttons(self):
        self.word_mode_button.on_click = self.word_mode_button_on_click

    def word_mode_button_on_click(self):
        self.game_mode = GameMode.WORDS
        choose_team_menu = ChooseTeamMenu(self.game, self.difficulty, self.game_mode)
        self.game.set_scene_active(choose_team_menu)
