import pygame as pg
import sys
import maze_maker


class Screen:
    def __init__(self, title, wh):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)        # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.x = wh[0]//100
        self.y = wh[1]//100
        #self.m_sfc = pg.Surface((1500,900))
        #self.m_rct = self.m_sfc.get_rect()
        self.maze = maze_maker.make_maze(self.x, self.y)
        self.block = list() 
        self.block_sfc = pg.Surface((100,100))
        self.block_rct = self.block_sfc.get_rect()
    def map(self):
        for y in range(len(self.maze)):
            for x in range(15):
                if self.maze[y][x] == 0:
                    self.block_rct.centerx = x*100+50
                    self.block_rct.centery = y*100+50
                    pg.draw.rect(self.block_sfc, (255, 255, 255), (10, 10, x*100+100, y*100+100))
                    self.block.append(self.block_sfc)
                    self.blit()
                elif self.maze[y][x] == 1:
                    self.block_rct.centerx = x*100+50
                    self.block_rct.centery = y*100+50
                    pg.draw.rect(self.block_sfc, (200, 200, 200), (10, 10, x*100+100, y*100+100))
                    self.block.append(self.block_sfc)
                    self.blit()
    

    def blit(self):
        self.sfc.blit(self.block_sfc, self.block_rct)

    def blit2(self):
        for i in self.block:
            self.sfc.blit(i, self.block_rct)


    

        

class Bird():
    def __init__(self, image: str, expansion: float, spawnpoint):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, expansion)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = spawnpoint
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_UP] :
            self.rct.move_ip(0, -1)
        if key_states[pg.K_DOWN]  :
            self.rct.move_ip(0, +1)
        if key_states[pg.K_LEFT]  :
            self.rct.move_ip(-1, 0)
        if key_states[pg.K_RIGHT] :
            self.rct.move_ip(+1, 0)
        self.blit(scr)


def main():
    clock = pg.time.Clock()
    scr = Screen("負けるな！こうかとん", (1500, 900))
    scr.map()
    tori = Bird("fig/6.png", 2.0, (150, 150))
    while True:
        scr.map()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        tori.update(scr)

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()