import pygame, random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
WIN_SIZE = 503
WIDTH = 20
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 100
BUTTON_COLOR = (170, 183, 184)

running = True
generations = 0

def randomize_board():
    states = [0] * 400
    states = [random.randint(0, 1) for j in range(WIDTH * WIDTH)]
    return states

cur_states = randomize_board()
next_states = []

pygame.init()
pygame.display.list_modes()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE + BUTTON_HEIGHT + 10)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Setup buttons
font = pygame.font.Font("freesansbold.ttf", 16)

# # Rect( left, top, width, height )
# pause_resume_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(15, WIN_SIZE + 5, 3 * BUTTON_SIZE, BUTTON_SIZE))
# restart_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(15 + BUTTON_SIZE, WIN_SIZE + 5, 3 * BUTTON_SIZE, BUTTON_SIZE))


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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            # Use coordinates to see if a button has been clicked:
            if pause_resume_button.collidepoint(click_pos):
                running = not running
            if restart_button.collidepoint(click_pos):
                cur_states = randomize_board()
                next_states = []
                generations = 0
 
    # --- Game logic should go here
    if running:
        generations += 1
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

    # Update the title
    pygame.display.set_caption(f"Conway's Game of Life - Generation: {generations}")

    # pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height) )
    pause_resume_button = pygame.draw.rect(screen, BUTTON_COLOR, pygame.Rect((WIN_SIZE//2 - BUTTON_WIDTH - 10), WIN_SIZE + 5, BUTTON_WIDTH, BUTTON_HEIGHT))
    pr_button_text = "Stop" if running is True else "Resume"
    text = font.render(pr_button_text, True, (14, 28, 54) )
    textRect = text.get_rect()  
    textRect.center = (pause_resume_button.center[0], pause_resume_button.center[1]) 
    screen.blit(text, textRect) 

    restart_button = pygame.draw.rect(screen, BUTTON_COLOR, pygame.Rect((WIN_SIZE//2 + 10), WIN_SIZE + 5, BUTTON_WIDTH, BUTTON_HEIGHT))
    text = font.render('Restart', True, (14, 28, 54) )
    textRect = text.get_rect()  
    textRect.center = (restart_button.center[0], restart_button.center[1]) 
    screen.blit(text, textRect)     

    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
