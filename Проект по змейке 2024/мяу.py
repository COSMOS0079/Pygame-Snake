import pygame
import random

pear_color = (209, 226, 49)
snake_color = (31, 110, 112)
background = (0, 255, 255)
mesh_color =  (20, 255, 255)

acceleration_counter = 0
screen_width = 700
screen_height = 500
mesh_size = 20
fps = 5
x = screen_width // 2 - 10
y = screen_height // 2 - 10
speed = mesh_size 
pear_counters = -1
snake = [(x, y)]
pear_check = True

win = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
direction = 'RIGHT'
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(mesh_color)
pygame.draw.rect(screen, snake_color, (snake[0][0], snake[0][1],  mesh_size, mesh_size))
pygame.display.update()

def pear_random ():
    pear = (random.randrange(0, screen_width, 20), random.randrange(0, screen_height, 20))
    return pear

def drawing_pear (pear):
    pygame.draw.rect(screen, pear_color, (pear[0], pear[1],  mesh_size, mesh_size))
    pygame.display.update()

def drawing_snake ():
      for i in range(len(snake)):
        pygame.draw.rect(screen, snake_color, (snake[i][0], snake[i][1],  mesh_size, mesh_size))


def snake_pieces (snake, direction):
    for i in reversed(range(1, len(snake))):
        snake[i] = snake [i - 1]
        print(snake)

pear = pear_random ()
while True: 
    snake_pieces (snake, direction)
    drawing_snake ()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
            elif event.key == pygame.K_a and direction != 'RIGHT':
                        direction = 'LEFT'
            elif event.key == pygame.K_d and direction != 'LEFT':
                        direction = 'RIGHT'
            elif event.key == pygame.K_w and direction != 'DOWN':
                        direction = 'UP'
            elif event.key == pygame.K_s and direction != 'UP':
                        direction = 'DOWN'
    head = snake[0]
    if direction == 'LEFT':
            new_head = (head[0] - 20 , head[1])
    elif direction == 'RIGHT':
            new_head = (head[0] + 20, head[1])
    elif direction == 'UP':
            new_head = (head[0], head[1] - 20)
    elif direction == 'DOWN':
            new_head = (head[0], head[1] + 20)

    snake[0] = new_head

    win.fill(mesh_color)

    drawing_snake ()

    if pear_check == False:
            pear = pear_random ()
            pear_check = True
            pear_counters += 1
            snake.append(snake[0])
            acceleration_counter += 1
    elif pear_check == True:
            drawing_pear (pear) 
            if snake[0] in snake[1:]:
                pygame.quit()
                quit()
            if  acceleration_counter == 3:
                acceleration_counter = 0
                fps += 1

    if pear == snake[0]:
            pear_check = False
    if snake[0][0] - mesh_size < - mesh_size or snake[0][0] + mesh_size > screen_width:
            pygame.quit()
            quit()

    if snake[0][1] - mesh_size < - mesh_size or snake[0][1] + mesh_size > screen_height:
            pygame.quit()
            quit() 
    pygame.display.update()
    clock.tick(fps)

    