from typing import TYPE_CHECKING
import pygame
from Core.UIObject import UIObject

if TYPE_CHECKING:
    from Core.Scene import Scene


class Text(UIObject):
    def __init__(self, position, size, scene: 'Scene', text: str, color=pygame.Color("black"), font=None, font_size=None):
        super().__init__(position, size, color, scene)
        self.text = text
        self.font = font
        self.font_size = font_size

    def set_text(self, text: str, font=None, font_color=pygame.Color("black")):
        self.text = text
        self.font = font
        self.font_color = font_color

    # def render(self, surface: pygame.Surface):
    #     if not self._is_active:
    #         return
    #
    #     font_size = self.font_size
    #     if not font_size:
    #         font_size = int(self.width // len(self.text) * 1.3281472327365)
    #
    #     font = pygame.font.Font(self.font, font_size)
    #     text_surface = font.render(self.text, True, self.color)
    #     text_x = self.center_position[0] - text_surface.get_width() // 2
    #     text_y = self.center_position[1] - text_surface.get_height() // 2
    #     # self.scene.game.screen.blit(text_surface, (text_x, text_y))

    def render(self, surface: pygame.Surface):
        if not self._is_active:
            return

        text_surface = self.get_surface()
        text_x = self.center_position[0] - text_surface.get_width() // 2
        text_y = self.center_position[1] - text_surface.get_height() // 2
        self.scene.game.screen.blit(text_surface, (text_x, text_y))

    def get_surface(self) -> pygame.Surface:
        font_size = self.font_size
        if not font_size:
            font_size = int(self.width // len(self.text) * 1.3281472327365)

        font = pygame.font.Font(self.font, font_size)
        text_surface = font.render(self.text, True, self.color)

        return text_surface
