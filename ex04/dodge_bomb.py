import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    #画面のあれこれ
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600,900)) #Surface
    screen_rect = screen.get_rect() #rect
    #背景の描画
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_img.get_rect()
    screen. blit(bg_img, bg_rect)
    #こうかとんの設定
    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    #爆弾の設定
    #bomb_img = pg.Surface((20, 20))
    bomb_img = pg.image.load("fig/bakudan.png")
    #bomb_img.set_colorkey((0, 0, 0))
    #pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_rect = bomb_img.get_rect()
    bomb_rect.centerx = random.randint(0, screen_rect.width)
    bomb_rect.centery = random.randint(0, screen_rect.height)
    vx, vy = +1, +1
    #爆発の設定
    bakuhatu = pg.image.load("fig/bakuhatu2.png")
    bakuhatu_rect = bakuhatu.get_rect()
    bakuhatu_rect.center = 800, 450


    while(True):
        screen. blit(bg_img, bg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        #こうかとんの移動と描画
        key = pg.key.get_pressed()
        if key [pg.K_UP]:
            tori_rect.move_ip(0, -1)
        if key [pg.K_DOWN]:
            tori_rect.move_ip(0, 1)
        if key [pg.K_LEFT]:
            tori_rect.move_ip(-1, 0)
        if key [pg.K_RIGHT]:
            tori_rect.move_ip(1, 0)
        #こうかとんがはみ出ないようにする処理
        if check_bound(tori_rect, screen_rect) != (1, 1):
            if key [pg.K_UP]:
                tori_rect.move_ip(0, 1)
            if key [pg.K_DOWN]:
                tori_rect.move_ip(0, -1)
            if key [pg.K_LEFT]:
                tori_rect.move_ip(1, 0)
            if key [pg.K_RIGHT]:
                tori_rect.move_ip(-1, 0)
        screen.blit(tori_img, tori_rect)
        #爆弾の移動と描画
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb_img, bomb_rect)
        (yoko, tate) = check_bound(bomb_rect, screen_rect)
        vx *= yoko
        vy *= tate 
        
        if key [pg.K_1]:#キーボードの１を押すとミサイルになる
            if vx == -1:#１を押し続けていると進行方向によってミサイルの向きが変わる
                bomb_img = pg.image.load("fig/bomb.png")
            else:
                    bomb_img = pg.image.load("fig/bomb2.png")
        elif key [pg.K_0]:#キーボードの０を押すと元に戻る
            bomb_img = pg.image.load("fig/bakudan.png")


        if tori_rect.colliderect(bomb_rect):#ぶつかったら爆発した画像を１秒間表示
            screen.blit(bakuhatu, bakuhatu_rect)
            pg.display.update()
            clock.tick(0.5)
            return 

        pg.display.update()
        clock.tick(1000)

#画面外にでないようにするのに利用する関数
def check_bound(rct, s_rct):  #rctはこうかとんか爆弾のrect  s_rctは画面のrect
    yoko, tate = +1, +1
    if rct.left < s_rct.left  or  s_rct.right < rct.right:
        yoko = -1
    if rct.top < s_rct.top  or  s_rct.bottom < rct.bottom:
        tate = -1
    return (yoko, tate)




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()