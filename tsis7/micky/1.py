import pygame
import math
import time

pygame.init()

# Set up the clock window
clock = pygame.time.Clock()
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Mickey Clock')

# Load the image of Mickey Mouse and scale it
mickey = pygame.image.load('clock.jpg')
mickey = pygame.transform.scale(mickey, (300, 300))

# Set the initial angle for Mickey's hands
minute_angle = 0
second_angle = 0

# Set the position of Mickey in the center of the window
mickey_x = window_width // 2 - mickey.get_width() // 2
mickey_y = window_height // 2 - mickey.get_height() // 2

# Set the size and position of Mickey's hands
minute_hand = pygame.image.load('min.jpg')
second_hand = pygame.image.load('sec.jpg')
minute_hand_rect = minute_hand.get_rect(center=(mickey_x + mickey.get_width() // 2, mickey_y + mickey.get_height() // 2))
second_hand_rect = second_hand.get_rect(center=(mickey_x + mickey.get_width() // 2, mickey_y + mickey.get_height() // 2))

# Set the font for the clock text
font = pygame.font.Font(None, 50)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Clear the window
    window.fill((255, 255, 255))
    
    # Get the current time
    current_time = time.localtime()
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec
    
    # Calculate the angles for Mickey's hands
    minute_angle = (current_minute / 60) * 360 - 90
    second_angle = (current_second / 60) * 360 - 90
    
    # Rotate the hands
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    
    # Set the positions of the rotated hands
    rotated_minute_hand_rect = rotated_minute_hand.get_rect(center=minute_hand_rect.center)
    rotated_second_hand_rect = rotated_second_hand.get_rect(center=second_hand_rect.center)
    
    # Draw Mickey and his hands on the window
    window.blit(mickey, (mickey_x, mickey_y))
    window.blit(rotated_minute_hand, rotated_minute_hand_rect)
    window.blit(rotated_second_hand, rotated_second_hand_rect)
    
    # Display the current time in text on the window
    current_time_text = time.strftime('%I:%M:%S %p', current_time)
    time_text = font.render(current_time_text, True, (0, 0, 0))
    time_rect = time_text.get_rect(center=(window_width // 2, window_height - 50))
    window.blit(time_text, time_rect)
    
    # Update the window
    pygame.display.update()
    
    # Set the frame rate to 60 fps
    clock.tick(60)