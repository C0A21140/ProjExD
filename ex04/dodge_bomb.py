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
    
    #tori_rect = tori_img.get_rect()
    #tori_rect.center = 700, 400
    #screen.blit(tori_img, tori_rect)

    while(True):
        screen. blit(bg_img, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()