import pygame
import os


spaceship_width, spaceship_height = 55, 40
FPS = 60
velocity = 5



width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('uhm yes i guess dis  is geme')
white = (255, 255, 255)
black = (0, 0, 0)
border = pygame.Rect(width/2 - 5, 0, 10, height)


yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_spaceship_image, (spaceship_width, spaceship_height)), 270)


def draw_window(red, yellow):
    window.fill(white)
    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))
    pygame.draw.rect(window, black, border)
    pygame.display.update()



def yellow_handle_movement(keys_pressed, yellow):
     if keys_pressed[pygame.K_a] and yellow.x - velocity > 0:  # LEFT KEY
         yellow.x -= velocity

     if keys_pressed[pygame.K_d] and yellow.x + velocity + yellow.width < border.x: # RIGHT KEY
         yellow.x += velocity

     if keys_pressed[pygame.K_w] and yellow.y - velocity > 0:  # UP KEY
         yellow.y -= velocity

     if keys_pressed[pygame.K_s] and yellow.y + velocity + yellow.height < height - 15:  # DOWN KEY
         yellow.y += velocity

def red_handle_movement(keys_pressed, red):
     if keys_pressed[pygame.K_LEFT] and red.x - velocity > border.x + border.width:  # LEFT KEY
         red.x -= velocity

     if keys_pressed[pygame.K_RIGHT] and red.x + velocity + red.width < width:  # RIGHT KEY
         red.x += velocity

     if keys_pressed[pygame.K_UP] and red.y - velocity > 0:  # UP KEY
         red.y -= velocity

     if keys_pressed[pygame.K_DOWN] and red.y + velocity + red.height < height - 15:  # DOWN KEY
         red.y += velocity


def main():
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys_pressed = pygame.key.get_pressed() 
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
    
    
    pygame.quit()


if __name__ == "__main__":
    main()