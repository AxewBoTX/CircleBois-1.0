import pygame,os,time

class Button():
    def __init__(self,x,y,image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
    def draw_button(self,master):
        #Button Function
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Screen Blitting
        master.blit(self.image,(self.rect.x,self.rect.y))
        return action