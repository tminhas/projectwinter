from Configs import *
from Imagens import *
from Personagens import *
from Plataformas import *
from Projetil import *
import pygame

# Iniciando o pygame
pygame.init()
# Os parametros para fonte são (fonte, tamanho, negrito, italico)
fonte = pygame.font.SysFont('comicsans', 30, True)  # Iniciando a fonte no pygame para poder escrever na tela
fonte2 = pygame.font.SysFont('comicsans', 80, True)  # Fonte para o titulo
fonte3 = pygame.font.SysFont('comicsans', 15, True)  # Fonte para pontuação
fonte4 = pygame.font.SysFont('comicsans', 25, True)  # Fonte para pontuação

'''
# Musicas do jogo (removidas do arquivo por ocuparem muito espaço)
pygame.mixer.init()
# Musicas boss, menu e game retiradas do site https://wingless-seraph.net/
boss_sound = pygame.mixer.Sound(os.path.join('Sons', 'som boss.wav'))
boss_sound.set_volume(0.02)
deadsound = pygame.mixer.Sound(os.path.join('Sons', 'som dead.wav'))
deadsound.set_volume(0.01)
menu_sound = pygame.mixer.Sound(os.path.join('Sons', 'som menu.wav'))
menu_sound.set_volume(0.01)
game_sound = pygame.mixer.Sound(os.path.join('Sons', 'som game.wav'))
game_sound.set_volume(0.01)
win_sound = pygame.mixer.Sound(os.path.join('Sons', 'som win.wav'))
win_sound.set_volume(0.01)
'''
# Iniciando a tela do jogo, definindo o nome e o ícone
tela = pygame.display.set_mode((TelaX, TelaY))
pygame.display.set_caption(Nome)
pygame.display.set_icon(game_icon)

# Iniciando o relógio interno
clock = pygame.time.Clock()


# Praticamente todos os parametros das funções se referem a algum grupo de sprites, as sprites são inicializadas
# durante o loop do jogo, mas para visualização todas estão no arquivo Configs
# Função que desenha o 'menu inicial' do jogo, acontece quando estado == 0
def desenhar_menu():
    tela.blit(menu, (0, 0))
    start_game = fonte.render('Aperte P para começar', True, BRANCO)
    project_winter = fonte2.render('Project Winter', True, BRANCO)
    voce = fonte.render('Este é o seu personagem', True, BRANCO)
    atirar = fonte.render(' Utilize as setas para atirar', True, BRANCO)
    movimentacao = fonte.render('Utilize W A D para se movimentar', True, BRANCO)
    tela.blit(project_winter, (130, 100))
    tela.blit(voce, (300, 250))
    tela.blit(movimentacao, (TelaX / 2 - 125, 460))
    tela.blit(atirar, (TelaX / 2 - 125, 540))
    tela.blit(start_game, (TelaX / 2 - 125, 630))
    pygame.display.update()


# Função que desenha o jogo em si
def desenhar_level1(level, personagem, inimigos):
    tela.blit(bg, (0, -50))  # Tela de fundo do jogo
    level.draw(tela)  # Esse comando não foi definido, mas ele existe porque os objetos foram definidos como sprites

    # Texto indicando que é a energia
    energy_bar = fonte.render('Energia', True, PRETO)
    tela.blit(energy_bar, (TelaX - 205, TelaY - 30))

    # Retangulos que fazem a energia da jetpack
    pygame.draw.rect(tela, PRETO, (TelaX - 110, TelaY - 30, 100, 20))
    pygame.draw.rect(tela, VERMELHO, (TelaX - 110, TelaY - 30, 100 * (personagem.jetpack * 2 / 100), 20))

    # Texto indicando que é a barra de vida
    health_points = fonte.render('HP', True, PRETO)
    tela.blit(health_points, (20, 22))

    # Texto que indica os objetivos
    objetivo = fonte.render('Objetivos: ', True, PRETO)
    obj_inimigos = fonte.render(f'Matar inimigos: {len(inimigos)}', True, PRETO)  # len inimigos1
    obj_nave = fonte.render('Alcançar a nave', True, PRETO)
    tela.blit(objetivo, (TelaX - 220, 22))
    tela.blit(obj_inimigos, (TelaX - 220, 52))
    tela.blit(obj_nave, (TelaX - 220, 82))

    # Retangulos que fazem a barra de vida do personagem
    pygame.draw.rect(tela, PRETO, (60, 20, 100, 20))
    if personagem.hp > 60:
        pygame.draw.rect(tela, VERDE, (60, 20, personagem.hp, 20))
    elif personagem.hp > 30:
        pygame.draw.rect(tela, AMARELO, (60, 20, personagem.hp, 20))
    elif personagem.hp > 0:
        pygame.draw.rect(tela, VERMELHO, (60, 20, personagem.hp, 20))

    # Quantidade de vidas do jogador
    lifes = fonte.render(f'Vidas: {personagem.vidas}', True, PRETO)
    tela.blit(lifes, (20, 52))

    pygame.display.update()


def desenha_level2(level, personagem, boss):
    tela.blit(fundo_boss, (0, 0))
    level.draw(tela)

    # Texto indicando que é a energia
    energy_bar = fonte.render('Energia', True, PRETO)
    tela.blit(energy_bar, (TelaX - 205, TelaY - 30))
    # Retangulos que fazem a energia da jetpack
    pygame.draw.rect(tela, PRETO, (TelaX - 110, TelaY - 30, 100, 20))
    pygame.draw.rect(tela, VERMELHO, (TelaX - 110, TelaY - 30, 100 * (personagem.jetpack * 2 / 100), 20))

    # Texto indicando que é a barra de vida
    health_points = fonte.render('HP', True, PRETO)
    tela.blit(health_points, (20, 22))

    # Retangulos que fazem a barra de vida do personagem
    pygame.draw.rect(tela, PRETO, (60, 20, 100, 20))
    if personagem.hp > 60:
        pygame.draw.rect(tela, VERDE, (60, 20, personagem.hp, 20))
    elif personagem.hp > 30:
        pygame.draw.rect(tela, AMARELO, (60, 20, personagem.hp, 20))
    elif personagem.hp > 0:
        pygame.draw.rect(tela, VERMELHO, (60, 20, personagem.hp, 20))

    # Quantidade de vidas do jogador
    lifes = fonte.render(f'Vidas: {personagem.vidas}', True, PRETO)
    tela.blit(lifes, (20, 52))

    # Barra de vida do chefao
    pygame.draw.rect(tela, VERMELHO, (boss.x - 60, boss.y - 380, 100, 20))
    pygame.draw.rect(tela, VERDE, (boss.x - 60, boss.y - 380, boss.hp / 2, 20))

    pygame.display.update()


def desenhar_win(personagem):
    tela.blit(vitoria, (0, 0))
    # Status do Jogador
    vidas_sobrando = fonte4.render('Fairy in a bottle', True, BRANCO)
    atirador = fonte4.render('Quick Finger', True, BRANCO)
    acertado = fonte4.render('Sharpshooter', True, BRANCO)
    pontos = fonte4.render('Pontuação', True, BRANCO)
    # Escrevendo o status
    acertado1 = fonte3.render(f'Disparos acertados: {shots_landed}', True, BRANCO)
    atirador1 = fonte3.render(f' Quantidade de disparos: {shots_fired}', True, BRANCO)
    vidas_sobrando1 = fonte3.render(f'Vidas restantes: {personagem.vidas}', True, BRANCO)
    pontos1 = fonte3.render(f' Pontuação atingida: {score}', True, BRANCO)
    # Botões
    press_p = fonte.render('P', True, BRANCO)
    press_q = fonte.render('Q', True, BRANCO)

    tela.blit(vidas_sobrando, (100, 505))
    tela.blit(atirador, (300, 505))
    tela.blit(acertado, (460, 505))
    tela.blit(pontos, (300, 655))

    tela.blit(acertado1, (459, 527))
    tela.blit(atirador1, (271, 527))
    tela.blit(vidas_sobrando1, (100, 527))
    tela.blit(pontos1, (283, 678))

    tela.blit(press_q, (30, 580))
    tela.blit(press_p, (680, 580))
    pygame.display.update()


# Função que troca o fundo da tela
def desenhar_gameover():
    tela.blit(dead, (0, 0))
    press_p = fonte.render('P', True, BRANCO)
    press_q = fonte.render('Q', True, BRANCO)
    tela.blit(press_q, (30, 580))
    tela.blit(press_p, (680, 580))
    pygame.display.update()


# Função para detectar colisão com plataformas
def colisao_plataformas(personagem, chao):
    col = pygame.sprite.spritecollide(personagem, chao, False)
    # False quer dizer que não é pra deletar a sprite do grupo após verificar a colisão
    # Se houver colisão, o jogador vai para o topo da plataforma - 4 (-4 pra ficar visualmente melhor )
    if col:
        personagem.y = col[0].rect.top - 4


# Função para detectar colisão do jogador com os inimigos
def colisao_inimigos(personagem, enemies):
    col = pygame.sprite.spritecollide(personagem, enemies, False)
    if col:
        personagem.hp -= 2
        return True


def checar_morte(personagem, bullet_group1, bullet_group2, x, y):
    # Checa se o jogador 'morreu' e deveria perder uma vida, e se sim, renascer no local predefinido com a energia cheia
    if personagem.hp <= 0:
        personagem.vidas -= 1
        personagem.hp = 100
        personagem.x = x
        personagem.y = y
        personagem.jetpack = 50
        for tiro in bullet_group1:  # Deletando os tiros dos inimigos
            tiro.kill()
        for tiro in bullet_group2:  # Deletando os tiros do jogador
            tiro.kill()
    if personagem.y > TelaY:
        personagem.hp = 0


# Função para danificar os inimigos ao serem atingidos por um tiro
def matando_inimigos(enemy, bullet_group):
    col = pygame.sprite.spritecollide(enemy, bullet_group, False)  # bullet_group = playertiros
    if col:
        enemy.hp -= 1
        return True
    if enemy.hp <= 0:
        enemy.kill()


def destruindo_tiros(bullet_group, plat, personagem):
    # Esse loop, é para verificar a colisão entre os tiros inimigos quanto tiros do jogador
    # e os grupos de jogador, inimigo e plataformas

    for bala in bullet_group:
        # Caso um tiro encoste em um bloco, ele será deletado do grupo de tiros
        col_blocos = pygame.sprite.spritecollide(bala, plat, False)
        if col_blocos:
            bala.kill()
        # Caso um tiro encoste em um inimigo, ele será deletado do grupo de tiros
        col_ini = pygame.sprite.spritecollide(bala, personagem, False)
        if col_ini:
            bala.kill()


# Função que detecta se o jogador foi atingido por um tiro, e se sim, o danifica
def colisao_player_bullets(personagem, bullet_group, n):
    col = pygame.sprite.spritecollide(personagem, bullet_group, False)
    if col:
        personagem.hp -= n
        return True


# Função que detecta se o jogador colidiu com o foguete
def colisao_player_nave(personagem, foguete):
    col = pygame.sprite.spritecollide(personagem, foguete, False)
    if col:
        return True


jogo = True
estado = 0

while jogo:  # Loop do jogo
    ''' Estado funciona como se fosse uma máquina de estados, no estado 0 é o menu, estado 1 é onde jogamos o jogo, e
     o estado 2 é a tela de game over, essa 'maquina de estados' funciona de forma, que quando X coisa acontece, ela 
     muda para o próximo estágio'''
    if estado == 0:
        desenhar_menu()
        #menu_sound.play(-1)  # -1 para tocar infinitamente enquanto nesse estado
        #status para tela de vitoria
        shots_fired = 0
        shots_landed = 0
        score = 0

        for event in pygame.event.get():  # Verificando uma lista de eventos para ver se algum deles ocorreu
            if event.type == pygame.QUIT:  # Clicar no X  vai fechar o jogo
                jogo = False
            if event.type == pygame.KEYDOWN:  # Apertar algum botão faz algo
                if event.key == pygame.K_q:
                    jogo = False
                if event.key == pygame.K_p:  # Inicializa as sprites e começa o jogo
                    #menu_sound.stop()
                    level1 = pygame.sprite.Group()
                    plataformas1 = pygame.sprite.Group()
                    nave = pygame.sprite.Group()
                    jogadores = pygame.sprite.Group()
                    inimigos1 = pygame.sprite.Group()
                    playertiros = pygame.sprite.Group()
                    enemytiros = pygame.sprite.Group()
                    ship = SpaceShip(42, 120)
                    nave.add(ship)
                    level1.add(ship)

                    player = Jogador(100, 640)
                    jogadores.add(player)
                    level1.add(player)
                    platforms_1 = [Plataforma(0, 640, chao_neve), Plataforma(128, 640, chao_neve),
                                   Plataforma(128, 640, chao_neve), Plataforma(256, 640, chao_neve),
                                   Plataforma(384, 640, chao_neve),

                                   Plataforma(80, 370, pl), Plataforma(80 + 18, 370, pm), Plataforma(80 + 36, 370, pm),
                                   Plataforma(80 + 54, 370, pm), Plataforma(80 + 72, 370, pr),

                                   Plataforma(500, 300, pl), Plataforma(500 + 18, 300, pm),
                                   Plataforma(500 + 36, 300, pm),
                                   Plataforma(500 + 54, 300, pr),

                                   Plataforma(300, 500, pl), Plataforma(300 + 18, 500, pm),
                                   Plataforma(300 + 36, 500, pm),
                                   Plataforma(300 + 54, 500, pr),

                                   Plataforma(300, 500, pl), Plataforma(300 + 18, 500, pm),
                                   Plataforma(300 + 36, 500, pm),
                                   Plataforma(300 + 54, 500, pr),

                                   Plataforma(125, 525, pl), Plataforma(125 + 18, 525, pm),
                                   Plataforma(125 + 36, 525, pr),

                                   Plataforma(600, 450, pl), Plataforma(600 + 18, 450, pm),
                                   Plataforma(600 + 36, 450, pm),
                                   Plataforma(600 + 54, 450, pr),

                                   Plataforma(300 - 36, 150, pl), Plataforma(300 - 18, 150, pm),
                                   Plataforma(300, 150, pm),
                                   Plataforma(300 + 18, 150, pm), Plataforma(300 + 36, 150, pm),
                                   Plataforma(300 + 54, 150, pr),

                                   Plataforma(30, 150, pl), Plataforma(30 + 18, 150, pm), Plataforma(30 + 36, 150, pm),
                                   Plataforma(30 + 54, 150, pr),
                                   ]
                    lista_inimigos = [InimigoAmarelo(80, 370, 170), InimigoRoxo(600, 700, 500, -1),
                                      InimigoVerde(264, 150, 372),
                                      InimigoVermelho(230, 550, 400, -1), InimigoAmarelo(600, 450, 672),
                                      InimigoVerde(500, 300, 572),
                                      InimigoRoxo(400, 500, 300, -1), InimigoRoxo(192, 300, 75, 1),
                                      InimigoVermelho(500, 500, 340, 1)
                                      ]
                    for ini in lista_inimigos:
                        level1.add(ini)
                        inimigos1.add(ini)

                    for plats in platforms_1:
                        level1.add(plats)
                        plataformas1.add(plats)

                    estado = 1

    # preciso iniciar a musica separadamente do estado do level porque o comando clock.tick(fps)
    # acelera a musica, a distorcendo muito
    #if estado == 1:
        #game_sound.play(-1)  # -1 para tocar infinitamente enquanto nesse estado
    while estado == 1:
        clock.tick(FPS)
        # Atualizando Sprites e Rodando as funções referentes a esse level
        level1.update()  # Roda o comando .update() que foi definido para cada personagem em Personagens.py
        desenhar_level1(level1, player, inimigos1)
        colisao_plataformas(player, plataformas1)
        colisao_inimigos(player, inimigos1)
        colisao_player_bullets(player, enemytiros, 2)
        checar_morte(player, enemytiros, playertiros, 100, 640)

        # Para cada inimigo na lista de inimigos será realizada a função que os danifica caso atingidos por um tiro
        for a in lista_inimigos:
            matando_inimigos(a, playertiros)
            if matando_inimigos(a, playertiros):
                shots_landed += 1

        destruindo_tiros(playertiros, plataformas1, inimigos1)
        destruindo_tiros(enemytiros, plataformas1, jogadores)

        for event in pygame.event.get():
            # Apertando no X fecha o jogo
            if event.type == pygame.QUIT:
                estado = 0
                jogo = False

            elif event.type == pygame.KEYDOWN:
                # Sempre que o jogador atirar, os inimigos também atiram
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    for inimigo in lista_inimigos:
                        # Se o inimigo tiver permissão para atirar e estiver vivo, ele irá atirar para o lado de sua vel
                        if inimigo.atirar and inimigo in inimigos1:
                            # Se a velocidade for positiva, irá atirar a para a direita
                            if inimigo.xvel > 0:
                                tiroD = ProjetilD(inimigo.x, inimigo.y, inimigo.cor)
                                level1.add(tiroD)
                                enemytiros.add(tiroD)

                            # Se a velocidade for negativa, irá atirar para a esquerda
                            if inimigo.xvel < 0:
                                tiroE = ProjetilE(inimigo.x, inimigo.y, inimigo.cor)
                                level1.add(tiroE)
                                enemytiros.add(tiroE)

                # Apertando Q, fecha o jogo
                if event.key == pygame.K_q:
                    estado = 0
                    jogo = False

                # Caso a seta esquerda seja apertada e o jogador estiver olhando para a esquerda, atirar p/ esquerda
                if event.key == pygame.K_LEFT and player.esquerda:
                    tiroE = ProjetilE(player.x, player.y, PRETO)
                    # Adicionando o tiro aos grupos, para detectar colisão
                    shots_fired += 1
                    level1.add(tiroE)
                    playertiros.add(tiroE)

                if event.key == pygame.K_RIGHT and player.direita:
                    # Caso a seta direita seja apertada e o jogador estiver olhando para a direita, atirar p/ direita
                    shots_fired += 1
                    tiroD = ProjetilD(player.x, player.y, PRETO)
                    level1.add(tiroD)
                    playertiros.add(tiroD)

        if player.vidas < 0:
            #game_sound.stop()
            estado = 4

        if len(inimigos1) < 1 and colisao_player_nave(player, nave):
            # Caso o jogador possa seguir para a proxima fase, inicializa-se os componentes dela
            # E começa-se a proxima fase
            #game_sound.stop()
            level2 = pygame.sprite.Group()
            plataformas2 = pygame.sprite.Group()
            inimigos2 = pygame.sprite.Group()
            platforms_2 = [Plataforma(30, 350, pl), Plataforma(30 + 18, 350, pm), Plataforma(30 + 36, 350, pm),
                           Plataforma(30 + 54, 350, pr),
                           Plataforma(30, 450, pl), Plataforma(30 + 18, 450, pm), Plataforma(30 + 36, 450, pm),
                           Plataforma(30 + 54, 450, pr),
                           Plataforma(30, 550, pl), Plataforma(30 + 18, 550, pm), Plataforma(30 + 36, 550, pm),
                           Plataforma(30 + 54, 550, pr),
                           Plataforma(30, 650, pl), Plataforma(30 + 18, 650, pm), Plataforma(30 + 36, 650, pm),
                           Plataforma(30 + 54, 650, pr)
                           ]
            chefao = Chefao(500, 700, 375)
            level2.add(chefao)
            inimigos2.add(chefao)
            for plats in platforms_2:
                level2.add(plats)
                plataformas2.add(plats)
            level2.add(player)
            player.x = 80
            player.y = 250
            estado = 3

    # preciso iniciar a musica separadamente do estado do level porque o comando clock.tick(fps)
    # acelera a musica, distorcendo muito ela
    #if estado == 3:
        #boss_sound.play(-1)  # -1 pra tocar a musica infinitamente enquanto nesse level
    while estado == 3:
        clock.tick(FPS)
        # Atualizando Sprites e Rodando as funções referentes a esse level
        desenha_level2(level2, player, chefao)
        level2.update()
        colisao_plataformas(player, plataformas2)
        colisao_inimigos(player, inimigos2)
        colisao_player_bullets(player, enemytiros, 5)
        checar_morte(player, enemytiros, playertiros, 80, 250)
        matando_inimigos(chefao, playertiros)
        destruindo_tiros(playertiros, plataformas2, inimigos2)
        destruindo_tiros(enemytiros, plataformas2, jogadores)

        # não consegui fazer aumentar a quantidade de tiros acertados contra o chefão, mas como só tem um inimigo
        # no segundo level e a vida dele é 200, para matar é só acertar 200 tiros, e como só aparece a pontuação
        # caso o jogador vença o jogo, só irei somar 200 acertos na pontuação

        for event in pygame.event.get():
            # Apertando no X fecha o jogo
            if event.type == pygame.QUIT:
                estado = 0
                jogo = False

            elif event.type == pygame.KEYDOWN:
                # Se o inimigo tiver permissão para atirar e estiver vivo irá atirar sempre que uma ação for realizada
                if chefao.atirar and chefao in inimigos2:
                    if chefao.hp > 100:
                        # Se o chefao tiver mais de metade da vida, irá atirar normalmente para a esquerda
                        tiroE = ProjetilE(chefao.x - 100, chefao.y - 150, chefao.cor)
                        level2.add(tiroE)
                        enemytiros.add(tiroE)
                    else:
                        # Caso o chefao tenha menos de metade da vida, entra no modo de ataque especial
                        # Em que sai um tiro em linha reta, um para cima e um para baixo
                        tiroE = ProjetilE(chefao.x - 100, chefao.y - 150, chefao.cor)
                        level2.add(tiroE)
                        enemytiros.add(tiroE)
                        tiroBoss1 = ProjetilBoss(chefao.x - 100, chefao.y - 150, chefao.cor, 2)
                        level2.add(tiroBoss1)
                        enemytiros.add(tiroBoss1)
                        tiroBoss2 = ProjetilBoss(chefao.x - 100, chefao.y - 150, chefao.cor, -2)
                        level2.add(tiroBoss2)
                        enemytiros.add(tiroBoss2)

                # Apertando Q, fecha o jogo
                if event.key == pygame.K_q:
                    estado = 0
                    jogo = False

                # Caso a seta esquerda seja apertada e o jogador estiver olhando para a esquerda, atirar p/ esquerda
                if event.key == pygame.K_LEFT and player.esquerda:
                    tiroE = ProjetilE(player.x, player.y, PRETO)
                    # Adicionando o tiro aos grupos, para detectar colisão
                    shots_fired += 1
                    level2.add(tiroE)
                    playertiros.add(tiroE)

                if event.key == pygame.K_RIGHT and player.direita:
                    # Caso a seta direita seja apertada e o jogador estiver olhando para a direita, atirar p/ direita
                    shots_fired += 1
                    tiroD = ProjetilD(player.x, player.y, PRETO)
                    level2.add(tiroD)
                    playertiros.add(tiroD)

        # Caso a vida do chefão chegue a 0, vamos para a tela de vitória
        if chefao.hp <= 0:
            shots_landed += 200  # soma mencionada anteriormente já que não consegui fazer o loop para verificar acertos
            #boss_sound.stop()
            estado = 5

        # Caso o numero de vidas do jogador seja menor que 0, vamos para a tela de derrota 'You Died'
        if player.vidas < 0:
            #boss_sound.stop()
            estado = 4

    # Tela de Game Over
    if estado == 4:
        desenhar_gameover()
        #deadsound.play(-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = 0
                jogo = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    estado = 0
                    jogo = False

                if event.key == pygame.K_p:
                    #deadsound.stop()
                    estado = 0

    if estado == 5:
        # Só pensei em uma formula aleatoria pra pontuação
        score = (player.vidas * shots_landed) - (shots_fired - shots_landed)
        desenhar_win(player)
        #win_sound.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = 0
                jogo = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    estado = 0
                    jogo = False
                if event.key == pygame.K_p:
                    #win_sound.stop()
                    estado = 0
