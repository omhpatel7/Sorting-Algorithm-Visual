import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Load sound effects
# swap_sound = pygame.mixer.Sound("C://Users//omhpa//OneDrive//Desktop//FunTimeCode//Swap_sound_2.mp3")  # Adjust file name accordingly
# swap_sound.set_volume(0.05)
# Screen dimensions
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 100, 100)
RED = (255, 0, 0)

# Font settings
font = pygame.font.SysFont(None, 24)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Bubble Sort algorithm
def bubble_sort(array):
    n = len(array)
    num_swaps = 0
    start_time = time.time()
    num_comparisons = 0  # Initialize number of comparisons
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1  # Increment number of comparisons
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                num_swaps += 1
                # Play swap sound
                # swap_sound.play()
                yield array.copy(), num_swaps, time.time() - start_time, num_comparisons

# Function to draw bars representing array elements
def draw_bars(array):
    screen.fill(BLACK)
    num_bars = len(array)
    bar_width = (SCREEN_WIDTH - 20) // num_bars  # Adjust bar width dynamically
    padding = (SCREEN_WIDTH - (bar_width * num_bars)) // 2  # Calculate padding dynamically
    border_width = 1  # Adjust border thickness
    for i, value in enumerate(array):
        bar_height = value * (SCREEN_HEIGHT // max(array))
        bar_rect = pygame.Rect(padding + i * bar_width, SCREEN_HEIGHT - bar_height, bar_width, bar_height)
        pygame.draw.rect(screen, WHITE, bar_rect)  # Draw border
        inner_rect = pygame.Rect(bar_rect.left + border_width, bar_rect.top + border_width, bar_rect.width - 2 * border_width, bar_rect.height - 2 * border_width)
        pygame.draw.rect(screen, CYAN, inner_rect)  # Fill inner part
    
    # Render text
    text = font.render("Bubble Sort", True, WHITE)
    screen.blit(text, (10, 10))

    text = font.render("Swaps: {}".format(num_swaps), True, WHITE)
    screen.blit(text, (10, 40))

    text = font.render("Time: {:.2f} s".format(time_taken), True, WHITE)
    screen.blit(text, (10, 70))

    text = font.render("Comparisons: {}".format(num_comparisons), True, WHITE)
    screen.blit(text, (10, 100))

    text = font.render("Delay: {:.4f} s".format(delay), True, WHITE)
    screen.blit(text, (10, 130))

    text = font.render("Visual Time: {:.2f} s".format(visual_time), True, WHITE)
    screen.blit(text, (10, 160))

    pygame.display.flip()

# Function to draw quit button
def draw_quit_button(is_hovered):
    quit_text = font.render("Quit", True, BLACK if is_hovered else WHITE)
    button_rect = pygame.Rect(SCREEN_WIDTH - 90, 10, 80, 30)
    pygame.draw.rect(screen, RED if is_hovered else (255, 50, 50), button_rect)
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
    screen.blit(quit_text, (SCREEN_WIDTH - 70, 15))
    pygame.display.flip()

# Main function
def main():
    # Initialize the array to be sorted
    array = np.random.randint(1, 100, 70)

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    global num_swaps, time_taken, num_comparisons, delay, visual_time
    num_swaps = 0
    time_taken = 0
    num_comparisons = 0
    delay = 0
    visual_time = 0

    # Main loop
    running = True
    for array, num_swaps, time_taken, num_comparisons in bubble_sort(array.copy()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw the bars and text
        draw_bars(array)

        # Cap the frame rate to make the animation faster
        clock.tick(90)  # Adjust this value to control the animation speed

    # Sorting is done, draw the quit button
    draw_quit_button(False)

    # Wait for user to quit
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if SCREEN_WIDTH - 90 <= mouse_x <= SCREEN_WIDTH - 10 and 10 <= mouse_y <= 40:
                    draw_quit_button(True)
                else:
                    draw_quit_button(False)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse click is inside quit button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if SCREEN_WIDTH - 90 <= mouse_x <= SCREEN_WIDTH - 10 and 10 <= mouse_y <= 40:
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
