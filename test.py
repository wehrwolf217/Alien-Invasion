#! /usr/bin/env python3
import sys

import pygame


class Test1:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("test")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                """выводите значение атрибута event.key при обнаружении 
                события pygame.KEYDOWN"""
                print(event.key)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        # Отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    test = Test1()
    test.run_game()