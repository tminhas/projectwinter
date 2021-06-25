# Personagens do jogo, Jogador e Inimigos
import pygame
from Configs import *
from Imagens import *


class Jogador(pygame.sprite.Sprite):  # Inicializando a classe como sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player_esquerda[0]  # Só funciona como sprite se eu usar self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.xvel = 5
        self.pulando = False
        self.caindo = True
        self.direita = False     # Indica a direção que o jogador está olhando, caso seja True, olhando para direita
        self.esquerda = False    # Indica a direção que o jogador está olhando, caso seja True, olhando esquerda
        self.vidas = 3           # Quantidade de vezes que o jogador pode 'morrer'
        self.hp = 100            # Vida máxima do jogador
        self.pulo = 8            # Distancia em y que o jogador 'pula'
        self.passos = 0          # Será utilizado para mudar a imagem do jogador
        self.jetpack = 50        # Energia que permite o 'voo' do jogador

    # Controla a movimentação do jogador, e a mudança de imagens
    def update(self):
        if self.passos + 1 >= 9:    # Como eu só tenho 3 imagens, quero que mude de imagem a cada 3 movimentações
            self.passos = 0         # Quando eu coloco self.passos = 0, é pra reiniciar as imagens da lista

        keys = pygame.key.get_pressed()  # Cria um dicionario com as keys do teclado

        if self.x + self.xvel > TelaX - 15:  # Limitando a movimenação para dentro da tela, pela direita
            self.x = TelaX - 15
            self.passos += 1
            self.direita = True
            self.esquerda = False
        else:
            if keys[pygame.K_d]:  # Apertando 'd', move-se para direita
                # Quando self.passos for 3, 6 as imagens do jogador são atualizadas, quando chega em 8 volta para 0
                self.image = Player_direita[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x += self.xvel
                self.passos += 1
                self.direita = True
                self.esquerda = False

        if self.x - self.xvel < 15:  # Limitando a movimenação para dentro da tela, pela esquerda
            self.x = 15
            self.passos += 1
            self.direita = False
            self.esquerda = True

        # Apertando 'a', move-se para esquerda
        else:
            if keys[pygame.K_a]:
                self.image = Player_esquerda[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x -= self.xvel
                self.passos += 1
                self.direita = False
                self.esquerda = True

        # Função de voo via uma 'jetpack' do personagem
        if keys[pygame.K_w]:
            if self.jetpack > 0:
                self.pulando = True
                self.y -= self.pulo
                self.caindo = True
                self.jetpack -= 1

        else:
            self.pulando = False

        # Recarregando a jetpack caso não esteja usando
        if self.jetpack < 50 and not self.pulando:
            self.jetpack += 20 / FPS
            if self.jetpack > 50:
                self.jetpack = 50

        # Limitando a movimentação para dentro da pela, pela parte de cima
        if self.y - self.pulo < 20:
            self.y = 30
            self.caindo = True

        # O jogador constantemente cai enquanto não estiver em uma plataforma
        if self.caindo:
            self.y += 5

        # Atualizando o retangulo do jogador
        self.rect.midbottom = (self.x, self.y)


class InimigoAmarelo(pygame.sprite.Sprite):
    # Para o inimigo amarelo, eu copiei o codigo do jogador, alterei as imagens e coloquei 'final' e 'caminho'
    # Que representam a área que o inimigo patrulha
    # E adicionei permissão para atirar
    def __init__(self, x, y, final):
        pygame.sprite.Sprite.__init__(self)
        self.image = Amarelo_direita[0]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.cor = AMARELO_ESCURO
        self.final = final
        self.xvel = 5
        self.hp = 5
        self.passos = 0
        self.caminho = [self.x, self.final]
        self.atirar = True  # Permissão para o personagem atirar

    def update(self):
        if self.passos + 1 >= 9:
            self.passos = 0

        # Para a movimentação do inimigo, caso a velocidade dele seja positiva ele continua em seu caminho
        # E quando chegar no seu limite, inverter a velocidade
        if self.xvel > 0:
            if self.x + self.xvel < self.caminho[1]:
                self.image = Amarelo_direita[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x += self.xvel
                self.passos += 1
            else:
                # Caso ele não possa mais andar para a direita, final do caminho, inverter a velocidade
                self.xvel = self.xvel * -1
                self.passos = 0

        else:
            if self.x + self.xvel > self.caminho[0]:
                self.image = Amarelo_esquerda[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x += self.xvel
                self.passos += 1
            else:
                self.xvel = self.xvel * -1
                self.passos = 0

        # Atualizando o retangulo do inimigo
        self.rect.midbottom = (self.x, self.y)


class InimigoVerde(pygame.sprite.Sprite):
    # O inimigo verde é igual ao amarelo, porém ele  não pode atirar
    def __init__(self, x, y, final):
        pygame.sprite.Sprite.__init__(self)
        self.image = Verde_direita[0]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.cor = VERDE
        self.final = final
        self.xvel = 10
        self.hp = 10
        self.passos = 0
        self.caminho = [self.x, self.final]
        self.atirar = False

    def update(self):
        if self.passos + 1 >= 9:
            self.passos = 0

        if self.xvel > 0:
            if self.x + self.xvel < self.caminho[1]:
                self.image = Verde_direita[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x += self.xvel
                self.passos += 1
            else:
                # Caso ele não possa mais andar para a direita, final do caminho, inverter a velocidade
                self.xvel = self.xvel * -1
                self.passos = 0

        else:
            if self.x + self.xvel > self.caminho[0]:
                self.image = Verde_esquerda[self.passos // 3]
                self.rect = self.image.get_rect()
                self.x += self.xvel
                self.passos += 1
            else:
                self.xvel = self.xvel * -1
                self.passos = 0

        # Atualizando o retangulo do inimigo
        self.rect.midbottom = (self.x, self.y)


class InimigoVermelho(pygame.sprite.Sprite):
    # Falta por uma cor
    # A diferença desse inimigo para os outros, é que a patrulha dele é vertical ao inves de horizontal
    def __init__(self, x, y, final, lado):
        pygame.sprite.Sprite.__init__(self)
        self.lado = lado
        if self.lado > 0:
            self.image = Vermelho_direita
            self.rect = self.image.get_rect()
        else:
            self.image = Vermelho_esquerda
            self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.final = final
        self.yvel = 5
        self.hp = 10
        self.caminho = [self.y, self.final]
        self.atirar = False

    def update(self):
        if self.yvel > 0:
            if self.y - self.yvel > self.caminho[1]:
                self.y -= self.yvel
            else:
                # Caso ele não possa mais subir, final do caminho, inverter a velocidade
                self.yvel = self.yvel * -1

        else:
            if self.y - self.yvel < self.caminho[0]:
                self.y -= self.yvel
            else:
                self.yvel = self.yvel * -1

        # Atualizando o retangulo do inimigo
        self.rect.midbottom = (self.x, self.y)


class InimigoRoxo(pygame.sprite.Sprite):
    # Esse inimigo patrulha verticalmente, e atira quando o jogador realiza um movimento
    # If self.xvel > 0: self.image = um, if self.x <0 self.image = outro
    def __init__(self, x, y, final, xvel):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.cor = ROXO
        self.final = final
        # Apesar de não andar horizontalmente, possui xvel para indicar que vai atirar para a direita ou esquerda
        self.xvel = xvel
        if self.xvel < 0:
            self.image = Roxo_direita
            self.rect = self.image.get_rect()
        else:
            self.image = Roxo_esquerda
            self.rect = self.image.get_rect()
        self.yvel = 5
        self.hp = 5
        self.caminho = [self.y, self.final]
        self.atirar = True

    def update(self):
        if self.yvel > 0:
            if self.y - self.yvel > self.caminho[1]:
                self.y -= self.yvel
            else:
                # Caso ele não possa mais subir, final do caminho, inverter a velocidade
                self.yvel = self.yvel * -1

        else:
            if self.y - self.yvel < self.caminho[0]:
                self.y -= self.yvel
            else:
                self.yvel = self.yvel * -1

        # Atualizando o retangulo do inimigo
        self.rect.midbottom = (self.x, self.y)


class Chefao(pygame.sprite.Sprite):
    # A diferença desse inimigo para os outros, é que a patrulha dele é vertical ao inves de horizontal
    def __init__(self, x, y, final):
        pygame.sprite.Sprite.__init__(self)
        self.image = Cyan_Esq
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.cor = CIANO
        self.final = final
        self.xvel = -1
        self.yvel = 5
        self.hp = 200
        self.caminho = [self.y, self.final]
        self.atirar = True

    def update(self):
        if self.yvel > 0:
            if self.y - self.yvel > self.caminho[1]:
                self.y -= self.yvel
            else:
                # Caso ele não possa mais subir, final do caminho, inverter a velocidade
                self.yvel = self.yvel * -1

        else:
            if self.y - self.yvel < self.caminho[0]:
                self.y -= self.yvel
            else:
                self.yvel = self.yvel * -1

        # Atualizando o retangulo do inimigo
        self.rect.midbottom = (self.x, self.y)


class SpaceShip(pygame.sprite.Sprite):
    # Jogador completa a fase quando matar todos os inimigos E colidir com a nave
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
