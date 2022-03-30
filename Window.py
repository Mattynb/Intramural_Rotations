from Rotations import call, mix
import pygame.mixer

pygame.init()
pygame.mixer.get_init()
pygame.mixer.get_num_channels()
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.load('lets.wav')
pygame.mixer.music.play()

pygame.mixer.Sound.play('lets.wav')