import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600,900)) #Surface
    screen_rect = screen.get_rect() #rect

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_img.get_rect()
    screen. blit(bg_img, bg_rect)

    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    



    while(True):
        screen. blit(bg_img, bg_rect)
        #screen.blit(tori_img, tori_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key = pg.key.get_pressed()
        if key [pg.K_UP] == True:
            tori_rect.centery -= 1
        if key [pg.K_DOWN] == True:
            tori_rect.centery += 1
        if key [pg.K_LEFT] == True:
            tori_rect.centerx -= 1
        if key [pg.K_RIGHT] == True:
            tori_rect.centerx += 1
        screen.blit(tori_img, tori_rect)
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()