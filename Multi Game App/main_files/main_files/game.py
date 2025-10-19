
import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        # running -> for game itself    playing -> for when the player interacts
        self.running, self.playing = True, False
        # to iterate through the menu
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # initializing canvas size
        self.DISPLAY_W, self.DISPLAY_H = 960, 540
        # canvas creation
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        # window creation
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.shooter = ShooterMenu(self)
        self.quiz = QuizMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    # GAME LOOP
    def game_loop(self):
        main_menu_bg = pygame.image.load('images/main_menu_bg.png').convert()  # Load the background image
        main_menu_bg = pygame.transform.scale(main_menu_bg, (self.DISPLAY_W, self.DISPLAY_H))  # Scale the image to fit the display

        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False

            # Blit the background image onto the display
            # OUR CANVAS ON WHICH THE ACTIONS PERFORMED WILL BE DISPLAYED
            self.display.blit(main_menu_bg, (0, 0))

            # Draw text on top of the background image
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)

            # Update the display
            self.window.blit(self.display, (0, 0))
            # UPDATES THE IMAGE
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            # CLOSING THE PROGRAM TO BY CLICKING THE 'X' BUTTON
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            # DESCRIBES ALL THE POSSIBLE EVENTS WHILE THE SPECIFIC KEY IS CLICKED DOWN
            if event.type == pygame.KEYDOWN:
                #   INDICATES ENTER KEY IS PRESSED
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                #   INDICATES BACKSPACE KEY IS PRESSED
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                #   INDICATES DOWN KEY IS PRESSED
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                #   INDICATES UP KEY IS PRESSED
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    # function that resets the values of keys so that once the user stop clicking keys won't remain true
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

