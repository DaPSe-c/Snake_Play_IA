import pygame, sys, random, time

pygame.init() #Inicialización

play_screen = pygame.display.set_mode((500,500)) #pantalla de juego (dimensiones de la superficie)
fps = pygame.time.Clock() #Se establecen los fotogramas por segundo

def main(): #Función
    snake_head = [100,50] #Declaración y posicionamiento (x,y) de la cabeza de la serpiente
    snake_body = [[100,50],[90,50],[80,50]] #Cuerpo inicial de la serpiente

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        play_screen.fill((0,0,0))

main()

pygame.quit()
