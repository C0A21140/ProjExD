import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, wh, image ):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)        # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)       # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rect
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    def __init__(self, image: str, expansion: float, spawnpoint):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, expansion)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = spawnpoint
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_UP]    :
            self.rct.move_ip(0, -1)
        if key_states[pg.K_DOWN]  :
            self.rct.move_ip(0, +1)
        if key_states[pg.K_LEFT]  :
            self.rct.move_ip(-1, 0)
        if key_states[pg.K_RIGHT] :
            self.rct.move_ip(+1, 0)
    
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    :
                self.rct.move_ip(0, +1)
            if key_states[pg.K_DOWN]  :
                self.rct.move_ip(0, -1)
            if key_states[pg.K_LEFT]  :
                self.rct.move_ip(+1, 0)
            if key_states[pg.K_RIGHT] :
                self.rct.move_ip(-1, 0)
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, speed, scr):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = speed 


    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)
    

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Attack: #羽を飛ばすクラス
    def __init__(self, tori: Bird, speed):
        self.sfc = pg.image.load("fig/wing.png") #画像を取得
        self.sfc = pg.transform.rotozoom(self.sfc, 2.0, 2.0) #画像を拡大
        self.rct = self.sfc.get_rect() #レクト
        self.rct.centerx = tori.rct.centerx + 1  #羽をこうかとんの右側に描画
        self.rct.centery = tori.rct.centery
        self.vx, self.vy = speed, 0   #動くスピードを決定

    def blit(self, scr):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, 0)
        self.blit(scr)
                        


def main():
    clock = pg.time.Clock()
    a = 1   #カウント
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    scr.blit()

    tori = Bird("fig/6.png", 2.0, (900, 400))
    
    baku = Bomb((255, 0, 0), 10, (+1, +1), scr)

    wing = Attack(tori, +5)
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE: #スペースキーが押されたら
                a = 0
                wing = Attack(tori, +5)
        
        if a == 0:  #カウントが0なら
            wing.update(scr)  #羽を飛ばす
        tori.update(scr)

        baku.update(scr)

        if tori.rct.colliderect(baku.rct):
            return

        pg.display.update()
        clock.tick(1000)



def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()