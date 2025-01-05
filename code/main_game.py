import pygame, sys
import cv2
from settings import *
from level import Level

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Kill them all')
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)

        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)


    def draw_text(self,text, font, color, surface, x, y):
        """Utility function to draw centered text on the screen."""
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    def main_menu(self):
        background = pygame.image.load("graphics/test/mm2.png")
        background = pygame.transform.scale(background, (WIDTH, HEIGTH))
        while True:
            self.screen.blit(background, (0, 0))
            self.draw_text("Kill them all", self.font, BLACK, self.screen, WIDTH // 2, HEIGTH // 2 - 50)
            self.draw_text("Press ENTER to Start and R to Restart", self.small_font, BLACK, self.screen, WIDTH // 2, HEIGTH // 2 + 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Start the game
                        return  # Exit the main menu loop

            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)



def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        sys.exit()

    # Get video width and height from OpenCV
    video_width = WIDTH
    video_height = HEIGTH

    # Set up the Pygame window for video
    screen = pygame.display.set_mode((video_width, video_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            # Break the loop once the video finishes
            break

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert frame into Pygame surface
        frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

        # Display the frame
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

        # Control the frame rate (adjust as necessary)
        pygame.time.Clock().tick(30)

    cap.release()



if __name__ == '__main__':
    game = Game()

    # Start the game loop after the video ends
    game.main_menu()
    game.run()

