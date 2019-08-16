import pygame, random
# Testing a push to github
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
WIN_SIZE = 503
WIDTH = 20

cur_states = [0] * 400
cur_states[0] = 1
cur_states[20] = 1
cur_states[40] = 1

next_states = []

pygame.init()
pygame.display.list_modes()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    if len(next_states) > 0:
        cur_states = next_states.copy()
        next_states = []

    i = 0
    while i < (WIDTH * WIDTH):
        # neighbors:
        #  i-21 | i-20 | i-19
        #  i -1 |      | i +1
        #  i+19 | i+20 | i+21
        neighbors = [ i - WIDTH + 1,    i - WIDTH,      i - WIDTH - 1,
                      i - 1,                            i + 1,
                      i + WIDTH - 1,    i + WIDTH,      i + WIDTH + 1 ]
        n = 0
        for pos in neighbors:
            try:
                if not (i % 10) and not (i % 20):
                    n += cur_states[pos]
            except:
                pass
 
        if cur_states[i] == 1:
            # live cell with < 2 live neighbors dies
            if n < 2:
                next_states.append(0)

            # live cell with 2-3 live neighbors lives
            elif n <= 3:
                next_states.append(1)

            # live cell with > 3 live neighbors dies
            else:
                next_states.append(0)

        else:
        # dead cell with = 3 live neighbors lives
            if n == 3:
                next_states.append(1)
            else:
                next_states.append(0)

        i += 1
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    # pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height) )

    i = 0
    y = 3
    while y < WIN_SIZE:
        x = 3

        while x < WIN_SIZE:
            if i < 400:
                COLOR = BLACK if cur_states[i] == 0 else WHITE
                pygame.draw.rect(screen, COLOR, pygame.Rect(x, y, 22, 22))

            i += 1
            x += 25
        y += 25


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
