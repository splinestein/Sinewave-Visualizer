import pygame as pg
from pygame.math import Vector2
import math
import time

class Player(pg.sprite.Sprite):

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((50, 50), pg.SRCALPHA)
        #magenta, dodgerblue, etc. use html color codes.
        pg.draw.circle(self.image, pg.Color('magenta'), (25, 25), 25)
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    # Blit objects with trails onto this surface instead of the screen.
    alpha_surf = pg.Surface(screen.get_size(), pg.SRCALPHA)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    player = Player((150, 150), all_sprites)

    #while True:
    for xpx in range(200):
        # Reduce the alpha of all pixels on this surface each frame.
        # Control the fade speed with the alpha value.
        alpha_surf.fill((255, 255, 255, 255), special_flags=pg.BLEND_RGBA_MULT)
        #time.sleep(.2)
        all_sprites.update()
        screen.fill((20, 50, 80))  # Clear the screen.
        all_sprites.draw(alpha_surf)  # Draw the objects onto the alpha_surf.
        player.vel.x = 2
        player.vel.y = math.sin(xpx / 10)*10 # / 10 to control wave accuracy and * 10 for range size
        screen.blit(alpha_surf, (0, 0))  # Blit the alpha_surf onto the screen.
        pg.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
    pg.quit()