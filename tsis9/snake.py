import random
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) # 1p
col1 = (255, 100, 50)  # 2p
col2 = (50, 255, 155)  #3p
listofcol = list((YELLOW, col1, col2))
randp = 1
timesec = (randp) * 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake')
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        global listofcol, randp, timesec
        timesec = (5 - randp)
        col = listofcol[randp-1]
        pygame.draw.rect(
            SCREEN,
            col,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

    def check(self, snakebody):
        head = self.location
        for i in snakebody.location()[1:len(snakebody.location()) -1]:
            if head.x == i.x and head.y == i.y:
                self.spawn(1, snakebody)

    def spawn(self, b, snakebody):
        global WIDTH, HEIGHT
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        if b == 1:
            b = 0
            self.check(snakebody)

class Snakehead:
    def __init__(self):
        self.headp = Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2)

    def location(self):
        return self.headp

    def update(self):
        headp = self.headp
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                headp.x * BLOCK_SIZE,
                headp.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


    def move(self, dx, dy):
        headp = self.headp
        headp.x += dx
        headp.y += dy

        if headp.x > WIDTH // BLOCK_SIZE:
            headp.x = 0
        elif headp.x < 0:
            headp.x = WIDTH // BLOCK_SIZE - 1
        elif headp.y > HEIGHT // BLOCK_SIZE:
            headp.y = 0
        elif headp.y < 0:
            headp.y = HEIGHT // BLOCK_SIZE - 1

    def check_collision(self, food):
        if self.headp.x != food.x:
            return False
        if self.headp.y != food.y:
            return False
        return True

    def check_body(self, snakebody):
        head = self.headp
        for i in snakebody.location()[2:len(snakebody.location()) -1]:
            a, b = False, False
            if head.x == i.x:
                a = True
            if head.y == i.y:
                b = True
            if a and b:
                return True
        return False

class Snakebody():
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]
    
    def location(self):
        return self.body

    def draw(self):
        for body in self.body:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, snake):
        self.body[0].x = snake.location().x
        self.body[0].y = snake.location().y
        
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y




def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y), width=1)

a = 1
tp = 120
def main():
    running = True
    snake = Snakehead()
    food = Food(5, 5)
    dx, dy = 0, 0
    foodpoint =0
    snakebody = Snakebody()
    global a, randp, timesec, tp   
    cnt = 0
    while running:
        SCREEN.fill(BLACK)
        cnt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        tp -= timesec 
        print(tp)
        snake.move(dx, dy)
        snakebody.move(snake)
        if snake.check_collision(food) or tp <= 0:
            if snake.check_collision(food):
                foodpoint += 4- randp
            tp = 60
            randp = random.randint(1,3)
            snakebody.body.append(Point(food.x, food.y))
            food.spawn(0, snakebody)

        if snake.check_body(snakebody):
            running = False

        food.check( snakebody) #food check
        food.update()
        snakebody.draw()
        snake.update()
        draw_grid()

        scores = font_small.render('SCORE: '+str(foodpoint), True, BLUE)
        level = font_small.render('level: '+str(a), True, BLUE)
        SCREEN.blit(scores, (10,10)) #score
        SCREEN.blit(level, (720,10)) #level

        if foodpoint >= 5:
            foodpoint = 0
            print(a)
            a += 1
            main()
            running = False

        pygame.display.flip()
        clock.tick(4+2* a) # +speed


if __name__ == '__main__':
    main()