from Core.Game import Game
from Core.Scene import Scene
from Scenes.PlayScene import PlayScene

from UIObjects.Button import Button

from Difficulties import Difficulty
from GameModes import GameMode


class ChooseTeamMenu(Scene):
    def __init__(self, game: Game = None, difficulty: Difficulty = None, game_mode: GameMode = None):
        self.difficulty = difficulty
        self.game_mode = game_mode
        super().__init__(game)

        self.teams = []

    def init_UI(self):
        center = self._game.width // 2, self._game.height // 2

        size = width, height = 200, 100
        position = x, y = center[0] - width // 2, center[1] - height // 2

        self.white_team_button = Button(position, size, (200, 200, 200), self, "Белые")
        self.black_team_button = Button((x, y + height + 10), size, (55, 55, 55), self, "Чёрные", font_color=(255, 255, 255))

    def connect_buttons(self):
        self.white_team_button.on_click = self.white_team_button_on_click
        self.black_team_button.on_click = self.black_team_button_on_click

    def white_team_button_on_click(self):
        self.teams.append('white')
        self.teams.append('black')
        play_scene = PlayScene(self.difficulty, self.game_mode, self.teams, self.game)
        self.game.set_scene_active(play_scene)

    def black_team_button_on_click(self):
        self.teams.append('black')
        self.teams.append('white')
        play_scene = PlayScene(self.difficulty, self.game_mode, self.teams, self.game)
        self.game.set_scene_active(play_scene)
