import pygame


class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        # картинка вместо залитого фона
        self.bg_color = pygame.image.load('images/space.png')
        # self.bg_color = (230, 230, 230) # цвет вместо картинки
        # Настройки корабля
        self.ship_speed = 10
        self.ship_limit = 3

        # параметры снаряда
        self.bullet_speed = 20
        self.bullet_width = 10
        self.bullet_heigth = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # настройки пришельцев
        self.fleet_drop_speed = 10

        # темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.alien_speed_factor = 3.0
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.fleet_direction = 1
        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
