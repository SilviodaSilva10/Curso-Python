import pygame

# inicializar pygame
pygame.init()

# carregar o arquivo de áudio
pygame.mixer.music.load("audio025.mp3")

# tocar o áudio (uma vez)
pygame.mixer.music.play()


# esperar até o áudio terminar
while pygame.mixer.music.get_busy():   # enquanto estiver tocando
    pygame.time.Clock().tick(10)       # dá um tempo para não travar a CPU

# fechar pygame
pygame.quit()
