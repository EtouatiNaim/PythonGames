
import pygame
from random import randint

def drawFood():
    food_color = pygame.Color(210,45,60)
    food_rect = pygame.Rect((food[0]*tiles_w, food [1]*tiles_h),(tiles_w,tiles_h))
    pygame.draw.rect(wind, food_color ,food_rect)
def drawSnake():
    snk_color = pygame.Color(60,215,60)
    for cell in snake:
        cell_rect= pygame.Rect((cell[0]*tiles_w,cell[1]*tiles_h), (tiles_w, tiles_h))
        pygame.draw.rect(wind,snk_color, cell_rect)

def updateSnake(direction):
    global food
    dirX, dirY = direction
    head = snake[0].copy()
    head[0] = (head[0] + dirX)%tiles_x
    head[1] = (head[1]+dirY)%tiles_y

    if head in snake[1:]:
        return False
    elif head == food:
        food=None
        while food is None:
            newfood = [
                randint(0, tiles_x-1),
                randint(0, tiles_y-1)
            ]
            food = newfood if newfood not in snake else None
    else:
        snake.pop()

    snake.insert(0, head)
    return True


#Init the window
sw = 640
sh = 480
wind = pygame.display.set_mode((sw, sh))

bg_color = pygame.Color(22,41,85)

##Define the playground
tiles_x=32
tiles_y=24

tiles_w= sw// tiles_x
tiles_h =sh//tiles_y

#Define the snake
snk_x, snk_y= tiles_x //4, tiles_y//2
snake =[
    [snk_x , snk_y],
    [snk_x-1, snk_y],
    [snk_x-2, snk_y]
]

#define the food
food = [tiles_x //2, tiles_y//2]


#Game loop
running =True
direction =[1,0]
while running:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key== pygame.K_RIGHT and not direction == pygame.K_LEFT: #'d' to right
                direction = [1,0]
            if event.key== pygame.K_LEFT and not direction == pygame.K_RIGHT: #'q' to left
                direction = [-1,0]
            if event.key== pygame.K_UP and not direction == pygame.K_DOWN: #'z' to up
                direction = [0,-1]
            if event.key== pygame.K_DOWN and not direction == pygame.K_UP: #'s' to down
                direction = [0,1]
    #Update
    if updateSnake(direction) == False:
        print("Game Over")
        running = False

    # Draw
    wind.fill(bg_color)
    drawFood()
    drawSnake()


    pygame.display.update()

pygame.quit()
