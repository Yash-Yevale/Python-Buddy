import pygame
import mysql.connector
from pygame.locals import *
import subprocess
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (960, 540)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Login Page")

# Initialize MySQL connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="snehanshu",
        password="SuperSpeed!2",
        database="pyproj"
    )
    cursor = connection.cursor()
except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)
    sys.exit(1)

# Set up the window
bg_image = pygame.image.load("images/newLoginPageBG.jpg")
bg_image = pygame.transform.scale(bg_image, (1200, 540))

font = pygame.font.Font("upheavtt.ttf", 40)
font_large = pygame.font.Font("8-BIT WONDER.TTF", 75)
font_med = pygame.font.Font("8-BIT WONDER.TTF", 50)

user_id_text = ""
password_text = ""
active_field = "user_id"

welcome_label_pos1 = (615, 123)
welcome_label_pos2 = (615, 198)
user_id_label_pos = (100, 230)
password_label_pos = (100, 290)
user_id_input_pos = (400, 230)
password_input_pos = (400, 290)
login_button_pos = (425, 350)

welcome_label1 = font_large.render("Py", True, (255, 255, 255))
welcome_label2 = font_med.render("Wizard", True, (255, 255, 255))
user_id_label = font.render("User ID:", True, (255, 255, 255))
password_label = font.render("Password:", True, (255, 255, 255))
login_button = font.render("Login", True, (255, 255, 255))

clock = pygame.time.Clock()
running = True
login_successful = False

while running and not login_successful:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if active_field == "user_id":
                if event.key == pygame.K_RETURN:
                    active_field = "password"
                elif event.key == pygame.K_BACKSPACE:
                    user_id_text = user_id_text[:-1]
                else:
                    user_id_text += event.unicode

            elif active_field == "password":
                if event.key == pygame.K_RETURN:
                    active_field = "login"
                elif event.key == pygame.K_BACKSPACE:
                    password_text = password_text[:-1]
                else:
                    password_text += event.unicode

            elif active_field == "login":
                if event.key == pygame.K_RETURN:
                    try:
                        # Check if user ID already exists
                        sql = "SELECT * FROM users WHERE user_id = %s"
                        cursor.execute(sql, (user_id_text,))
                        existing_user = cursor.fetchone()

                        if existing_user:
                            print("User ID already exists. Logging in...")
                            # Retrieve the password stored in the database
                            stored_password = existing_user[2]

                            # Implement your login logic here, for example:
                            # Compare the stored password from the database with the entered password
                            if stored_password == password_text:
                                print("Login successful!")
                                login_successful = True
                            else:
                                print("Invalid password!")

                        else:
                            # Insert user data into MySQL database
                            sql = "INSERT INTO users (user_id, password) VALUES (%s, %s)"
                            cursor.execute(sql, (user_id_text, password_text))
                            connection.commit()
                            print("Data inserted successfully!")
                            login_successful = True
                    except mysql.connector.Error as error:
                        print("Failed to perform operation in MySQL table", error)
                        connection.rollback()

    screen.blit(bg_image, (0, 0))
    screen.blit(welcome_label1, welcome_label_pos1)
    screen.blit(welcome_label2, welcome_label_pos2)
    screen.blit(user_id_label, user_id_label_pos)
    screen.blit(password_label, password_label_pos)

    user_id_surface = font.render(user_id_text, True, (255, 255, 255))
    password_surface = font.render("*" * len(password_text), True, (255, 255, 255))
    screen.blit(user_id_surface, user_id_input_pos)
    screen.blit(password_surface, password_input_pos)

    screen.blit(login_button, login_button_pos)

    if active_field == "user_id":
        pygame.draw.rect(screen, (255, 255, 255, 128), (user_id_input_pos[0] - 10, user_id_input_pos[1] - 5, 200, 55), 3)
    elif active_field == "password":
        pygame.draw.rect(screen, (255, 255, 255, 128), (password_input_pos[0] - 10, password_input_pos[1] - 5, 200, 55), 3)
    elif active_field == "login":
        pygame.draw.rect(screen, (212, 175, 55), (login_button_pos[0] - 15, login_button_pos[1] - 5, 150, 55), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
cursor.close()
connection.close()

# Check if login was successful
if login_successful:
    os.system("python main.py")
