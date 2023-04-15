import collections
import math
import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
global BLUE, RED, GREEN
Blue = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
current_color = pygame.Color(255, 255, 255)

font = pygame.font.SysFont("Verdana", 10)

# Point = collections.namedtuple('Point', ['x', 'y'])

def write():
    size = 40
    global font, SCREEN, WHITE, WIDTH
    SCREEN.blit(font.render("RHOMB", True, WHITE), (WIDTH //2 - 10*(size //2),60))
    SCREEN.blit(font.render("RECT", True, WHITE), (WIDTH // 2 - size // 2,60))
    SCREEN.blit(font.render("ERES", True, WHITE), (WIDTH // 2 + 2*(size // 2),60))
    SCREEN.blit(font.render("CIRCL", True, WHITE), (WIDTH //2 - 4*(size //2),60))
    SCREEN.blit(font.render("SQUAR", True, WHITE), (WIDTH //2 + 5*(size //2),60))
    SCREEN.blit(font.render("RTRI", True, WHITE), (WIDTH //2 - 7*(size //2),60))
    SCREEN.blit(font.render("ETRI", True, WHITE), (WIDTH //2 + 8*(size //2),60))
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )
        self.ereser = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 + 2*(self.size // 2),
                20,
                self.size,
                self.size,
            )
        )
        self.circle = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 4*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        self.square = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 + 5*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        self.rtriangle = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 7*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        self.etriangle = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 + 8*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        self.rhomb = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 10*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 - self.size // 2,
                20,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH // 2 + 2*(self.size // 2),
                20,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 4*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )

        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 + 5*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 7*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 + 8*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                WIDTH //2 - 10*(self.size //2),
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Color(GameObject):
    def __init__(self):
        self.size = 40
        self.red = pygame.draw.rect(
            SCREEN,
            (255, 0, 0),
            (
                20,
                HEIGHT // 2 - self.size // 2,
                self.size,
                self.size,
            )
        )
        self.green = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                20,
                HEIGHT // 2 + 2*(self.size // 2),
                self.size,
                self.size,
            )
        )
        self.blue = pygame.draw.rect(
            SCREEN,
            (0, 0, 255),
            (
                20,
                HEIGHT //2 - 4*(self.size //2),
                self.size,
                self.size,
            )
        )
        

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255, 0, 0),
            (
                20,
                HEIGHT // 2 - self.size // 2,
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                20,
                HEIGHT // 2 + 2*(self.size // 2),
                self.size,
                self.size,
            )
        )
        pygame.draw.rect(
            SCREEN,
            (0, 0, 255),
            (
                20,
                HEIGHT //2 - 4*(self.size //2),
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        global current_color
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                current_color,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)


class Ereser(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                BLACK,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))


class Square(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            current_color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_x - start_pos_x,
            ),
            width=5,
        )
    
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos



class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            current_color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )
    
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = (self.start_pos.x+ self.end_pos.x) //2
        start_pos_y = (self.start_pos.y+ self.end_pos.y) //2

        rad = start_pos_x - self.start_pos.x
        if rad <= 0:
            rad = -1*rad

        pygame.draw.circle(
            SCREEN,
            current_color,
            (start_pos_x,
            start_pos_y),
            rad,
            width=5,
        )
  
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Rtriangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = min(self.start_pos.x, self.end_pos.x)
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            current_color,
            (
                (start_pos_x, start_pos_y),
                (start_pos_x, end_pos_y),
                (end_pos_x, end_pos_y)
            ),
            width=5,
        )
        
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Etriangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = min(self.start_pos.x, self.end_pos.x)
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            current_color,
            (
                ((start_pos_x +end_pos_x )//2, start_pos_y),
                (start_pos_x, ((end_pos_y - start_pos_y) * pow(3, 1/2))//1),
                (end_pos_x, ((end_pos_y - start_pos_y) * pow(3, 1/2))//1)
            ),
            width=5,
        )
        
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Rhomb(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        global current_color
        start_pos_x = min(self.start_pos.x, self.end_pos.x)
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            current_color,
            (
                ((start_pos_x +end_pos_x )//2, start_pos_y),
                (start_pos_x, (end_pos_y + start_pos_y)//2),
                ((start_pos_x +end_pos_x )//2, end_pos_y),
                (end_pos_x, (end_pos_y + start_pos_y)//2),
                
            ),
            width=5,
        )
        
    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    global BLUE, RED, GREEN, current_color
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    button = Button()
    coller = Color()
    objects = [
        button,
        coller
    ]
    size = 40
    

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                    # current_shape = button.connected_shape
                elif button.ereser.collidepoint(event.pos):
                    current_shape = Ereser
                elif button.circle.collidepoint(event.pos):
                    current_shape = Circle
                elif button.square.collidepoint(event.pos):
                    current_shape = Square
                elif button.rtriangle.collidepoint(event.pos):
                    current_shape = Rtriangle
                elif button.etriangle.collidepoint(event.pos):
                    current_shape = Etriangle
                elif button.rhomb.collidepoint(event.pos):
                    current_shape = Rhomb
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)
                
                if coller.green.collidepoint(event.pos):
                    current_color = GREEN
                    # current_shape = button.connected_shape
                elif coller.red.collidepoint(event.pos):
                    current_color = RED
                elif coller.blue.collidepoint(event.pos):
                    current_color = pygame.Color(0, 0, 255)



            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object

        for obj in objects:
            obj.draw()

        #button write
        write()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()