# Projetil que o jogador e alguns inimigos usam
import pygame
from Configs import *


class ProjetilD(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.x = x
        self.y = y
        self.xvel = 10
        self.image = pygame.Surface((4, 4))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10  # y - 10 pra ele aparecer +- no meio do personagem

    def update(self):
        # Caso esteja dentro dos limites da tela, pode continuar o movimento
        if TelaX > self.rect.x > 0:
            self.rect.x += self.xvel

        # Caso va sair dos limites da tela, deletar a sprite
        # Comando .kill() é do grupo de sprites
        else:
            self.kill()


class ProjetilE(pygame.sprite.Sprite):
    def __init__(self, x, y, cor):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.x = x
        self.y = y
        self.xvel = 10
        self.image = pygame.Surface((4, 4))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10

    def update(self):
        if TelaX > self.rect.x > 0:
            self.rect.x -= self.xvel
        else:
            self.kill()


class ProjetilBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, cor, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.x = x
        self.y = y
        self.xvel = 10
        self.yvel = yvel
        self.image = pygame.Surface((4, 4))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 10

    def update(self):
        if TelaX > self.rect.x > 0:
            self.rect.x -= self.xvel
        else:
            self.kill()
        if TelaY > self.rect.y > 0:
            self.rect.y += self.yvel
        else:
            self.kill()


