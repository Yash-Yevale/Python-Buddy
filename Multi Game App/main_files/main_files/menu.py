import sys
import pygame
import os
from menu import *
from game import *


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Space Invader"
        self.startx, self.starty = self.mid_w, self.mid_h + 20
        self.quizx, self.quizy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        main_menu_bg = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\images\main_menu_bg.png").convert()
        main_menu_bg = pygame.transform.scale(main_menu_bg, (self.game.DISPLAY_W, self.game.DISPLAY_H))

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(main_menu_bg, (0, 0))
            self.game.draw_text('PY', 75, self.game.DISPLAY_W * 0.722, self.game.DISPLAY_H / 2 - 110)
            self.game.draw_text('WIZARD', 50, self.game.DISPLAY_W * 0.80, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Space Invader", 20, self.startx, self.starty)
            self.game.draw_text("Quiz", 20, self.quizx, self.quizy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Space Invader':
                self.cursor_rect.midtop = (self.quizx + self.offset, self.quizy)
                self.state = 'Quiz'
            elif self.state == 'Quiz':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Shooter'
        elif self.game.UP_KEY:
            if self.state == 'Space Invader':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Quiz':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Space Invader'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quizx + self.offset, self.quizy)
                self.state = 'Quiz'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Space Invader':
                self.game.curr_menu = self.game.shooter
            elif self.state == 'Quiz':
                self.game.curr_menu = self.game.quiz
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class ShooterMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        os.system("python maingame2.py")
        shooter_menu_bg = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\images\main_menu_bg.png").convert()
        shooter_menu_bg = pygame.transform.scale(shooter_menu_bg, (
        self.game.DISPLAY_W, self.game.DISPLAY_H))

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(shooter_menu_bg, (0, 0))
            self.game.draw_text('Thanks for Playing', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Space Invader', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 )
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

class QuizMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        os.system("python maingame1.py")
        quiz_menu_bg = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\images\main_menu_bg.png").convert()
        quiz_menu_bg = pygame.transform.scale(quiz_menu_bg, (
        self.game.DISPLAY_W, self.game.DISPLAY_H))

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(quiz_menu_bg, (0, 0))
            self.game.draw_text('Thanks for playing', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text('Quiz', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 )
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        credits_menu_bg = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\images\credits_menu_bg.jpg").convert()
        credits_menu_bg = pygame.transform.scale(credits_menu_bg, (
        self.game.DISPLAY_W, self.game.DISPLAY_H))

        while self.run_display:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.game.curr_menu = self.game.main_menu
                        self.run_display = False
                elif event.type == pygame.QUIT:
                    self.run_display = False
                    pygame.quit()
                    sys.exit()

            self.game.check_events()
            self.game.display.blit(credits_menu_bg, (0, 0))
            credits_x_val = self.game.DISPLAY_W * 0.75
            self.game.draw_text('Credits', 20, credits_x_val, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text('MADE BY ', 15, credits_x_val, self.game.DISPLAY_H / 2 - 10)
            self.game.draw_text('Jai       43', 15, credits_x_val, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Snehanshu 46', 15, credits_x_val, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('Harshad   56', 15, credits_x_val, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text('Sanmay    71', 15, credits_x_val, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text('Yash      72', 15, credits_x_val, self.game.DISPLAY_H / 2 + 90)
            self.blit_screen()


class Game:
    def __init__(self):
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = "arial"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.curr_menu = MainMenu(self)
        self.main_menu = MainMenu(self)
        self.shooter = ShooterMenu(self)
        self.quiz = QuizMenu(self)
        self.credits = CreditsMenu(self)
        self.BACK_KEY = pygame.K_BACKSPACE
        self.UP_KEY = pygame.K_UP
        self.DOWN_KEY = pygame.K_DOWN
        self.START_KEY = pygame.K_RETURN

    def run(self):
        while True:
            self.window.fill(self.BLACK)
            self.curr_menu.display_menu()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
