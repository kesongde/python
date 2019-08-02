class Settings():
    #存储《外星人入侵》的所有设置的类

    def __init__(self):
        #初始化游戏的设置
        #屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船的速度
        self.ship_speed_factor = 5

        #子弹设置
        self.bullet_speed_factor = 7
        self.bullet_width = 2
        self.bullet_height = 5
        self.bullet_color = 60,60,60

        self.bullets_allowed = 3000

        #外星人设置
        self.alien_speed_factor = 1

        self.fleet_drop_speed = 10
        #fleet_direction为1表示右移,为-1表示左移
        self.fleet_direction = 1
