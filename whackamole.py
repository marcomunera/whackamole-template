import pygame
import random

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x, mole_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32:
                        mole_x = random.randrange(0, 640, 32)
                        mole_y = random.randrange(0, 512, 32)

            screen.fill("light green")
            for i in range(0, 512 + 1, 32):
                pygame.draw.line(screen, "dark blue", (0, i), (640, i))
            for j in range(0, 640 + 1, 32):
                pygame.draw.line(screen, "dark blue", (j, 0), (j, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()