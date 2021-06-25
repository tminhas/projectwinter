import pygame
import os
from Configs import *

""" Sobre as imagens utilizadas
    O jogador e os inimigos foram feitos por mim no photoshop, inspirados no jogo among us, o cenário, plataformas e 
    blocos foram retirados da internet do site : opengameheart.org, musicas são da internet"""

# Conjunto de Imagens do jogador
Player_direita = [pygame.image.load(os.path.join('imagens/black1.png')),
                  pygame.image.load(os.path.join('imagens/black2.png')),
                  pygame.image.load(os.path.join('imagens/black3.png'))]

Player_esquerda = [pygame.transform.flip(pygame.image.load(os.path.join('imagens/black1.png')), True, False),
                   pygame.transform.flip(pygame.image.load(os.path.join('imagens/black2.png')), True, False),
                   pygame.transform.flip(pygame.image.load(os.path.join('imagens/black3.png')), True, False)]

# Conjunto de Imagens do Inimigo Amarelo
Amarelo_direita = [pygame.image.load(os.path.join('imagens/yellow1.png')),
                   pygame.image.load(os.path.join('imagens/yellow2.png')),
                   pygame.image.load(os.path.join('imagens/yellow3.png'))]

Amarelo_esquerda = [pygame.transform.flip(pygame.image.load(os.path.join('imagens/yellow1.png')), True, False),
                    pygame.transform.flip(pygame.image.load(os.path.join('imagens/yellow2.png')), True, False),
                    pygame.transform.flip(pygame.image.load(os.path.join('imagens/yellow3.png')), True, False)]

# Conjunto de Imagens do Inimigo Rosa
Rosa_direita = [pygame.image.load(os.path.join('imagens/pink1.png')),
                pygame.image.load(os.path.join('imagens/pink2.png')),
                pygame.image.load(os.path.join('imagens/pink3.png'))]

Rosa_esquerda = [pygame.transform.flip(pygame.image.load(os.path.join('imagens/pink1.png')), True, False),
                 pygame.transform.flip(pygame.image.load(os.path.join('imagens/pink2.png')), True, False),
                 pygame.transform.flip(pygame.image.load(os.path.join('imagens/pink3.png')), True, False)]

Roxo_esquerda = pygame.image.load(os.path.join('imagens/purple.png'))

Roxo_direita = pygame.transform.flip(pygame.image.load(os.path.join('imagens/purple.png')), True, False)

# Conjunto de Imagens do Inimigo Verde
Verde_direita = [pygame.image.load(os.path.join('imagens/green1.png')),
                 pygame.image.load(os.path.join('imagens/green2.png')),
                 pygame.image.load(os.path.join('imagens/green3.png'))]

Verde_esquerda = [pygame.transform.flip(pygame.image.load(os.path.join('imagens/green1.png')), True, False),
                  pygame.transform.flip(pygame.image.load(os.path.join('imagens/green2.png')), True, False),
                  pygame.transform.flip(pygame.image.load(os.path.join('imagens/green3.png')), True, False)]

# Conjunto de imagens do Inimigo Vermelho
Vermelho_direita = pygame.image.load(os.path.join('imagens/red.png'))
Vermelho_esquerda = pygame.transform.flip(pygame.image.load(os.path.join('imagens/red.png')), True, False)

# Imagens do Chefão
Cyan_Dir = pygame.image.load(os.path.join('imagens/Ciano.png'))
Cyan_Esq = pygame.transform.flip(Cyan_Dir, True, False)

# Imagem da nave
ship = pygame.image.load(os.path.join('imagens/ship.png'))
# Icone do jogo e fundo
game_icon = pygame.image.load(os.path.join('imagens/game_icon.png'))
background = pygame.image.load(os.path.join('imagens/bg_snow_b.png'))
bg = pygame.transform.scale(background, (TelaX, TelaY + 50))  # .scale altera o tamanho da imagem para o valor desejado

# Imagens para o chão e plataformas
chao_neve = pygame.image.load(os.path.join('imagens/snow_54.png'))
background_boss = pygame.image.load(os.path.join('imagens/background_boss.png'))
fundo_boss = pygame.transform.scale(background_boss, (TelaX, TelaY))

# Plataformas
pr = pygame.image.load(os.path.join('imagens/tundraRight.png'))
pl = pygame.image.load(os.path.join('imagens/tundraLeft.png'))
pm = pygame.image.load(os.path.join('imagens/tundraMid.png'))

# Telas
menu = pygame.image.load(os.path.join('imagens/menu.png'))
vitoria = pygame.image.load(os.path.join('imagens/tela vitoria.png'))
dead = pygame.image.load(os.path.join('imagens/you-died.png'))