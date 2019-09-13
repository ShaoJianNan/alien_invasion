import sys

import pygame as pygame

import game_functions
from Settings.settings import Settings
from alien_invasion.ship import Ship


def ran_game():
    #初始化游戏并且创建一屏幕个对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #设置背景颜色
    bg_color=(ai_settings.bg_color)
    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        game_functions.check_events(ship)
        ship.update()
        #每次循环都重绘制屏幕
        game_functions.update_screen(ai_settings,screen,ship)

ran_game()

