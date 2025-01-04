import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Menu with Animation')

# Load three images for animation
frame1 = pygame.image.load('graphics/menu/menu0.png').convert_alpha()
frame2 = pygame.image.load('graphics/menu/menu1.png').convert_alpha()
frame3 = pygame.image.load('graphics/menu/menu2.png').convert_alpha()

# Scale images to fit the screen (optional)
frame1 = pygame.transform.scale(frame1, (WIDTH, HEIGHT))
frame2 = pygame.transform.scale(frame2, (WIDTH, HEIGHT))
frame3 = pygame.transform.scale(frame3, (WIDTH, HEIGHT))

# Create a list to hold the frames
frames = [frame1, frame2, frame3, frame2]

# Variables for animation
current_frame = 0
animation_speed = 150  # Time in milliseconds between frames
last_update = pygame.time.get_ticks()  # Track the time of the last frame switch

# Main menu loop
def menu():
    global current_frame, last_update
    font = pygame.font.Font(None, 60)
    menu_running = True

    while menu_running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Start the game
                    menu_running = False
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()

        # Animation logic (switch frames every `animation_speed` milliseconds)
        current_time = pygame.time.get_ticks()
        if current_time - last_update > animation_speed:
            current_frame = (current_frame + 1) % len(frames)  # Loop over the frames
            last_update = current_time

        # Display the current frame
        screen.blit(frames[current_frame], (0, 0))

        # Display menu text
        start_text = font.render("Press 'S' to Start", True, (255, 255, 255))
        quit_text = font.render("Press 'Q' to Quit", True, (255, 255, 255))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 450))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, 500))

        pygame.display.update()
        pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

# Run the menu
if __name__ == '__main__':
    menu()
