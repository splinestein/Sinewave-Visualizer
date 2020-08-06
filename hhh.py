import pygame as pg
from pygame.math import Vector2
import math
import time
from sys import exit

class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        #magenta, dodgerblue, etc. use html color codes.
        pg.draw.circle(self.image, pg.Color('magenta'), (25, 25), 20)
        self.rect = self.image.get_rect(center=pos) #center=pos
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

def main():
    pg.init()
    screen = pg.display.set_mode((1200, 1200))
    # Blit objects with trails onto this surface instead of the screen.
    alpha_surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    player = Player((300, 300), all_sprites)

    #while True:
    st = time.time()
    xpx = 0

    xpy = 0
    while True:
        xpx += 1 #Acts as our time
    #for xpx in range(400):
        dt = st - time.time()
        # Reduce the alpha of all pixels on this surface each frame.
        # Control the fade speed with the alpha value.
        alpha_surf.fill((255, 255, 255, 255), special_flags=pg.BLEND_RGBA_MULT)
        #time.sleep(.2)
        all_sprites.update()
        screen.fill((20, 50, 80))  # Clear the screen.
        all_sprites.draw(alpha_surf)  # Draw the objects onto the alpha_surf.
        '''
        player.vel.x = 10 * math.sin(xpx / 10)
        player.vel.y = 10 * math.cos(xpx / 10)
        xr = 40 * math.cos(xpx / 50)
        yr = 40 * math.sin(xpx / 50)
     
        player.vel.x += xr * math.sin(xpx / 5)
        player.vel.y += yr * math.sin(xpx / 10)
        '''
        '''
        #cool thing 
        xr = 2 * math.cos(xpx / 30)
        yr = 2 * math.sin(xpx / 50)
        player.vel.x += xr * math.sin(xpx / 5)
        player.vel.y += yr * math.sin(xpx / 7)
        '''
        events = pg.event.get()



        #Moves player left,right,up,down if arrow keys are held down.
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            pass
            #player.pos[1] -= 4
        if keys[pg.K_DOWN]:
            pass
            #player.pos[1] += 4
        if keys[pg.K_LEFT]:
            #player.pos[0] -= 4
            xpy -= 1
            player.vel.y = (10) * math.sin((xpy / 10))
            player.vel.x = (10) * math.cos((xpy / 10))
        if keys[pg.K_RIGHT]:
            #player.pos[0] += 4
            xpy += 1
            player.vel.y = (10) * math.sin((xpy / 10))
            player.vel.x = (10) * math.cos((xpy / 10))

        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_x:
                    pg.quit()

        #Keep within screen.
        if player.pos[0] >= 1200:
            player.pos[0] = 0
        if player.pos[0] < 0:
            player.pos[0] = 1200
        if player.pos[1] >= 1200:
            player.pos[1] = 0
        if player.pos[1] < 0:
            player.pos[1] = 1200


        #player.vel.y = math.sin((xpx / 10)*100) / math.cos((xpx / 1000)*10) # / 10 to control wave accuracy and * 10 for range size
        #player.vel.y = math.sin((xpx / 10)*100) / math.cos((xpx / 500)*10)
        #player.vel.y = (10) * math.sin((xpx / 10))
        #player.vel.x = (math.sin(xpx / 10)*10) * math.cos((xpx / 10))
        #player.vel.y = (10) * math.sin((xpx / 10))
        #player.vel.x = (10) * math.cos((xpx / 10))

        screen.blit(alpha_surf, (0, 0))  # Blit the alpha_surf onto the screen.
        pg.display.update()
        #pg.display.flip() #removed in v3 due to constant crashing
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()