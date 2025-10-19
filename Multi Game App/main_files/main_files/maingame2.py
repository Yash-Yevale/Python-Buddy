import random
import pygame
import self

from objects import Background, Player, Enemy, Bullet, Explosion, Fuel, Powerup, Button, Message, BlinkingText

pygame.init()
SCREEN = WIDTH, HEIGHT = 960, 540

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# COLORS **********************************************************************

WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

# IMAGES **********************************************************************

plane_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\plane.png")
logo_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\spaceInvader.png")
fighter_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\fighterToBe.png")
clouds_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\clouds.png")
clouds_img = pygame.transform.scale(clouds_img, (WIDTH, 350))

home_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\Buttons\homeBtn.png")
replay_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\Buttons\replay.png")
sound_off_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\Buttons\soundOffBtn.png")
sound_on_img = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\Buttons\soundOnBtn.png")

# BUTTONS *********************************************************************

home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT // 2 + 120)
replay_btn = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT // 2 + 115)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT // 2 + 120)

# FONTS ***********************************************************************

game_over_font = 'upheavtt.ttf'
tap_to_play_font = 'upheavtt.ttf'
score_font = '8-BIT WONDER.TTF'
final_score_font = '8-BIT WONDER.TTF'

game_over_msg = Message(WIDTH // 2, 320, 30, 'Game Over', game_over_font, WHITE, win)
score_msg = Message(WIDTH - 50, 28, 30, '0', final_score_font, GOLD, win)  # DISPLAY END SCORE
final_score_msg = Message(WIDTH // 2, 290, 30, '0', final_score_font, GOLD, win)
tap_to_play_msg = tap_to_play = BlinkingText(WIDTH // 2, HEIGHT - 60, 50, "Tap To Play",
                                             tap_to_play_font, GOLD, win)

# SOUNDS **********************************************************************
try:
    player_bullet_fx = pygame.mixer.Sound('Sounds/gunshot.wav')
except FileNotFoundError:
    player_bullet_fx = None
    print("Warning: gunshot.wav not found.")

if player_bullet_fx:
    player_bullet_fx.play()

player_bullet_fx = pygame.mixer.Sound(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\gunshot.wav")
click_fx = pygame.mixer.Sound(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\click.mp3")
collision_fx = pygame.mixer.Sound(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\mini_exp.mp3")
blast_fx = pygame.mixer.Sound(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\blast.wav")
fuel_fx = pygame.mixer.Sound(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\fuel.wav")

pygame.mixer.music.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Sounds\Defrini - Spookie.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

# GROUPS & OBJECTS ************************************************************

bg = Background(win)
p = Player(144, HEIGHT - 100)

enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()


################################################ FUNCTIONS *******************************************************************


def shoot_bullet():
    x, y = p.rect.center[0], p.rect.y

    if p.powerup > 0:
        for dx in range(-3, 4):
            b = Bullet(x, y, 4, dx)
            player_bullet_group.add(b)
        p.powerup -= 1
    else:
        b = Bullet(x - 30, y, 6)
        player_bullet_group.add(b)
        b = Bullet(x + 30, y, 6)
        player_bullet_group.add(b)
    player_bullet_fx.play()


def reset():
    enemy_group.empty()
    player_bullet_group.empty()
    enemy_bullet_group.empty()
    explosion_group.empty()
    fuel_group.empty()
    powerup_group.empty()

    p.reset(p.x, p.y)


# VARIABLES *******************************************************************

plane_destroy_count = 0
plane_frequency = 10000
start_time = pygame.time.get_ticks()

moving_left = False
moving_right = False

home_page = True
game_page = False
score_page = False

score = 0
sound_on = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        if event.type == pygame.KEYDOWN and game_page:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot_bullet()

        if event.type == pygame.KEYDOWN:
            if home_page == True and pygame.K_DOWN:
                home_page = False
                game_page = True

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if home_page:
        #         home_page = False
        #         game_page = True
        #         click_fx.play()
        #     elif game_page:
        #         x, y = event.pos
        #         if p.rect.collidepoint((x, y)):
        #             shoot_bullet()
        #         elif x <= WIDTH // 2:
        #             moving_left = True
        #         elif x > WIDTH // 2:
        #             moving_right = True

        if event.type == pygame.KEYUP:
            moving_left = False
            moving_right = False

        if event.type == pygame.MOUSEBUTTONUP:
            moving_left = False
            moving_right = False

    if home_page:
        bg_image = pygame.image.load(r"C:\Users\Yash Yevale\Downloads\Multi-Game Application\Python_Mini_Project2\Python_Mini_Project\Assets\bg2.png")
        bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        win.blit(bg_image, (0, 0))
        logo_width, logo_height = logo_img.get_size()
        logo_x = (WIDTH - logo_width) // 2 - 320
        logo_y = (HEIGHT - logo_height) // 2 - 85

        pygame.draw.circle(win, WHITE, (WIDTH // 2 + 2, HEIGHT // 2 + 18), 181, 4)
        win.blit(fighter_img, (WIDTH//2 - 250, HEIGHT//2 - 230))
        win.blit(logo_img, (logo_x, logo_y + 10))
        tap_to_play_msg.update()

    if score_page:
        bg_image = pygame.image.load('Assets/bg2.png')
        bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        win.blit(bg_image, (0, 0))
        logo_x = (WIDTH - logo_width) // 2
        logo_y = (HEIGHT - logo_height) // 2 - 85
        win.blit(logo_img, (logo_x, logo_y))
        game_over_msg.update()
        final_score_msg.update(score)


        if home_btn.draw(win):
            home_page = True
            game_page = False
            score_page = False
            reset()
            click_fx.play()

            plane_destroy_count = 0
            score = 0

        if replay_btn.draw(win):
            score_page = False
            game_page = True
            reset()
            click_fx.play()

            plane_destroy_count = 0
            score = 0

        if sound_btn.draw(win):
            sound_on = not sound_on

            if sound_on:
                sound_btn.update_image(sound_on_img)
                pygame.mixer.music.play(loops=-1)
            else:
                sound_btn.update_image(sound_off_img)
                pygame.mixer.music.stop()

    if game_page:
        current_time = pygame.time.get_ticks()
        delta_time = current_time - start_time

        if delta_time >= plane_frequency:
            spawn_positions = [[(160, -150), (460, -150), (780, -150)],
                               [(460, -150), (160, -150), (780, -150)],
                               [(460, -150),(780, -150), (160, -150)]]
            pos = random.choice(spawn_positions)
            positions = random.sample(pos, 3)
            enemy = [Enemy(pos[0], pos[1]) for pos in positions]  # Assume `type` is defined elsewhere  # Assuming Enemy class takes x, y as parameters
            enemy_group.add(*enemy)
            start_time = current_time

        p.fuel -=0.025
        bg.update(1)
        win.blit(clouds_img,(0,70))

        p.update(moving_left, moving_right, explosion_group)
        p.draw(win)

        player_bullet_group.update()
        player_bullet_group.draw(win)
        enemy_bullet_group.update()
        enemy_bullet_group.draw(win)
        explosion_group.update()
        explosion_group.draw(win)
        fuel_group.update()
        fuel_group.draw(win)
        powerup_group.update()
        powerup_group.draw(win)

        enemy_group.update(enemy_bullet_group, explosion_group)
        enemy_group.draw(win)

        if p.alive:
            player_hit = pygame.sprite.spritecollide(p, enemy_bullet_group, False)
            for bullet in player_hit:
                p.health -= bullet.damage

                x, y = bullet.rect.center
                explosion = Explosion(x, y, 1)
                explosion_group.add(explosion)

                bullet.kill()
                collision_fx.play()

            for bullet in player_bullet_group:
                planes_hit = pygame.sprite.spritecollide(bullet, enemy_group, False)
                for plane in planes_hit:
                    # if plane.hits_correct_image(Enemy.image.image_path):
                    #     score += 10
                    plane.health -= bullet.damage

                    if plane.health <= 0:
                        x, y = plane.rect.center
                        rand = random.random()
                        if rand >= 0.9:
                            power = Powerup(x, y)
                            powerup_group.add(power)
                        elif rand >= 0.3:
                            fuel = Fuel(x, y)
                            fuel_group.add(fuel)

                        plane_destroy_count += 1
                        blast_fx.play()

                    x, y = bullet.rect.center
                    explosion = Explosion(x, y, 1)
                    explosion_group.add(explosion)

                    bullet.kill()
                    collision_fx.play()

            player_collide = pygame.sprite.spritecollide(p, enemy_group, True)
            if player_collide:
                x, y = p.rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)

                x, y = player_collide[0].rect.center
                explosion = Explosion(x, y, 2)
                explosion_group.add(explosion)

                p.health = 0
                p.alive = False

            if pygame.sprite.spritecollide(p, fuel_group, True):
                p.fuel += 25
                if p.fuel >= 100:
                    p.fuel = 100
                fuel_fx.play()

            if pygame.sprite.spritecollide(p, powerup_group, True):
                p.powerup += 2
                fuel_fx.play()

        if not p.alive or p.fuel <= -10:
            if len(explosion_group) == 0:
                game_page = False
                score_page = True
                reset()

        score += 1
        # score = Enemy.hits_correct_image(self,enemy_bullet_group)
        # score_msg.update(score)
        # print(score)
        fuel_color = RED if p.fuel <= 40 else GREEN
        pygame.draw.rect(win, fuel_color, (30, 20, p.fuel, 10), border_radius=4)
        pygame.draw.rect(win, WHITE, (30, 20, 100, 10), 2, border_radius=4)
        pygame.draw.rect(win, BLUE, (30, 32, p.health, 10), border_radius=4)
        pygame.draw.rect(win, WHITE, (30, 32, 100, 10), 2, border_radius=4)
        win.blit(plane_img, (10, 15))

    pygame.draw.rect(win, WHITE, (0, 0, WIDTH, HEIGHT), 5, border_radius=4)
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
"""
if(correct):
    score+=10
"""