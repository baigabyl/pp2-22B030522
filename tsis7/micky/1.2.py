from datetime import datetime 
import pygame 
import os
pygame.init() 
screen=pygame.display.set_mode((400,400)) 
a = datetime.now() 
image = pygame.image.load("clock.jpg") 
image = pygame.transform.scale(image, (400, 400)) 
handl = pygame.image.load('min.jpg') 
handl = pygame.transform.scale(handl, (200, 200)) 
handr =pygame.image.load("sec.jpg") 
handr = pygame.transform.scale(handr, (200, 200)) 
def left_hand(surf, image, topleft, angle):  
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#правая рука 
def right_hand(surf, image, topleft, angle):   
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#формулы нахождения позиции рук мауса 
anglel=(51-a.second)*6 
angleh=308-(a.minute*6) 
#координаты центра вращения стрелок 
x=100 
y=80 
running = True 
n=a.second 
while running: 
    #присвоил еще одной переменной метод "время сейчас",чтобы выполнялось условие b.second != n во время вращения секундной стрелки 
    b=datetime.now() 
    screen.fill((255,255,255)) 
    #вставил изображения мауса в окно 
    screen.blit(image,(0,0))    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            pygame.quit() 
            quit() 
    #вызов функции левой и правой руки 
    left_hand(screen, handl, [x,y], anglel) 
    right_hand(screen,handr,[x,y], angleh) 
    #обновление окна  
    pygame.display.update()   
    #увеличиваем угол вращения стрелок     
    if b.second>=0 and b.second !=n: 
        n=b.second 
        anglel-=6 
    if b.second==0: 
        angleh-=0.1 
    print(b.second)