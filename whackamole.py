import pygame
import random

BOARD_ROWS = 16
BOARD_COLS = 20

def draw_lines(screen):
    # horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            (0,0,0),
            (0, i*32),
            (640,i*32),
        )
    # vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            (0,0,0),
            (i*32,0),
            (i*32,512)
        )

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if(x >= mole_x and x <= mole_x + 32):
                        if(y >= mole_y and y <= mole_y+32):
                            mole_x = random.randint(0,BOARD_COLS-1)*32
                            mole_y = random.randint(0,BOARD_ROWS-1)*32

            screen.fill("light green")
            draw_lines(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
