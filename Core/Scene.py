import pygame
from typing import TYPE_CHECKING

from Core.GameObject import GameObject
from UIObjects.Button import Button

if TYPE_CHECKING:
    from Game import Game
    from UIObject import UIObject


class Scene(GameObject):
    def __init__(self, game: 'Game' = None):
        self._is_active = False
        self.children: list['UIObject'] = []

        if game:
            game.add_scene(self)
        self._game = game

    @property
    def game(self) -> 'Game':
        return self._game

    @game.setter
    def game(self, value: 'Game'):
        self._game = value
        self.init_UI()
        self.connect_buttons()

    def init_UI(self):
        pass

    def connect_buttons(self):
        pass

    def add_child(self, child: 'UIObject'):
        self.children.append(child)

    def render(self, surface: pygame.Surface):
        for child in self.children:
            child.render(surface)

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        if isinstance(value, bool):
            self._is_active = value
        else:
            raise ValueError("Scene.is_active принимает только boolean значения")

    def handle_event(self, event: pygame.event.Event):
        for child in self.children:
            child.handle_event(event)

        if event.type == pygame.MOUSEMOTION:
            if any(i.hovered for i in self.children if isinstance(i, Button)):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # def connect_buttons_by_name(self):
    #     for i in self.children:
    #         if type(i).__name__ == "Button":
    #             method_name = f"{i.__name__}_on_click"
    #             print(method_name)
    #             if hasattr(self, method_name):
    #                 i.on_click = eval(method_name)
