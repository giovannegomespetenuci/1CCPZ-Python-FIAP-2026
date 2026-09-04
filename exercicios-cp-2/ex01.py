import pygame

pygame.mixer.init()
pygame.mixer.music.load("spiritcrusher.mp3") # falta só adicionar a música no diretório

decisao = input("Deseja tocar a música Spirit Crusher?")
while decisao.lower in ("sim"):
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    decisao = input("Deseja continuar a tocar a música Spirit Crusher?")