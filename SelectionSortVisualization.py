
import random
import time
import pygame
from pygame.locals import *
 
pygame.init()
 
width, height = 500, 500

GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)



screen = pygame.display.set_mode((width, height))

def create_list(start_num,end_num,length):
    new_list = []

    for i in range(length):
        new_list.append(random.randint(start_num,end_num))
    return new_list

test_list = create_list(0,400,100)



def display_list():
    screen.fill(BLACK)
    rect_x = 0

    for i in range(len(test_list)):
        pygame.draw.rect(screen,(0,255,0),(rect_x,500-test_list[i],4,test_list[i]))
        rect_x += 5

    pygame.display.flip()
    

def draw_time(screen,x,y,time):
    font = pygame.font.Font(None, 36)
    text = font.render("Time: " + str(time) + "s", 1, WHITE)
    screen.blit(text,(x,y))

def sort():
    
    #Iterate through the whole list
    for i in range (len(test_list)):

        if i >= len(test_list)-1:
            break

        #Set the current smallest index
        smallest = i

        #Iterate through the elements that come after the current element
        for j in range(i+1,len(test_list)):
            
            #Checking if there is a smaller element and setting it equal to smallest
            if test_list[smallest] > test_list[j]:
                smallest = j

        
        
        test_list[i],test_list[smallest] = test_list[smallest],test_list[i]
        display_list()
        #pygame.time.wait(100)


# Game loop.
run = True
start = time.time()
sort()
end = time.time()
time_elapsed = round(end - start,2)
while run:
  
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    
    draw_time(screen,75,75,time_elapsed)

    pygame.display.flip()

pygame.quit()
    



  
  
