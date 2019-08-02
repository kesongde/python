import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并创建一个屏幕的对象
    #pygame.init()
    #screen = pygame.display.set_mode((1200,800))
    #初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("TU_UT")

    #创建一艘飞船
    #创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个外星人
    alien = Alien(ai_settings,screen)


    #设置背景色
    #bg_color = (230,230,230)
    
    
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标d
        #for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        sys.exit()
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()

        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        #gf.update_bullets(bullets)
        #gf.update_screen(ai_settings,screen,ship,alien,bullets)
        
        #gf.update_aliens(aliens)

        gf.update_aliens(ai_settings,aliens)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        
        #每次循环时都重绘屏幕
        #screen.fill(bg_color)
        
        screen.fill(ai_settings.bg_color)
        #ship.blitme()

        #让最近绘制的屏幕可见
        #pygame.display.flip()

run_game()