# Configurações gerais, e algumas explicações

"""
Separei as partes do jogo em arquivos diferentes porque fica muito mais facil de verificar as coisas,
Fica muito ruim de subir pra achar uma coisa pra modificar pq fica muito aglomerado
E sabendo o que eu quero modificar e onde, é só ir pro arquivo certo
Importante lembrar, que no pygame, o (0,0) não fica no centro da tela, e sim no canto superior esquerdo
Quando o jogo é executado, está acontecendo esse aviso 'libpng warning: iCCP: known incorrect sRGB profile',
não sei o que o causa, só que está relacionado as imagens dos personagens, mas isso não influencia nada, está
funcionando normal
"""

# Configurações

TelaX = 720
TelaY = 720
Nome = 'Project Winter'
FPS = 20

# Cores em RGB (Red Green Blue)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
AMARELO = (255, 255, 0)
AMARELO_ESCURO = (204, 204, 0)
ROXO = (128, 0, 128)
TESTE = (248, 248, 255)


'''
Coloquei todos os grupos de sprites aqui para facilitar a visualização e não precisar repetir as explicações
No meio do loop
Sprite é qualquer objeto que pode se mover na tela
A utilização de sprites facilita muito os mecanismos de colisão entre os objetos

level1 = pygame.sprite.Group()
level2 = pygame.sprite.Group()
plataformas1 = pygame.sprite.Group()
plataformas2 = pygame.sprite.Group()
nave = pygame.sprite.Group()
jogadores = pygame.sprite.Group()
inimigos1 = pygame.sprite.Group()
inimigos2 = pygame.sprite.Group()
playertiros = pygame.sprite.Group()
enemytiros = pygame.sprite.Group()

ship = SpaceShip(42, 120)
nave.add(ship)
level1.add(ship)

player = Jogador(100, 640)
jogadores.add(player)
level1.add(player)


# Uma plataforma normal é feita a partir da combinação de plataformas menores( 18 pixels por 10 pixels )
# Plataforma(x, y, pl), Plataforma(x + 18, y, pm), Plataforma(x + 36, y, pm), Plataforma(x + 54, y, pr),
# As com chao_neve representam o chao do mapa
# plataformas 1 e 2 representam o level a qual elas pertencem
platforms_1 = [Plataforma(0, 640, chao_neve), Plataforma(128, 640, chao_neve),
               Plataforma(128, 640, chao_neve), Plataforma(256, 640, chao_neve),
               Plataforma(384, 640, chao_neve),

               Plataforma(80, 370, pl), Plataforma(80 + 18, 370, pm), Plataforma(80 + 36, 370, pm),
               Plataforma(80 + 54, 370, pm), Plataforma(80 + 72, 370, pr),

               Plataforma(500, 300, pl), Plataforma(500 + 18, 300, pm), Plataforma(500 + 36, 300, pm),
               Plataforma(500 + 54, 300, pr),

               Plataforma(300, 500, pl), Plataforma(300 + 18, 500, pm), Plataforma(300 + 36, 500, pm),
               Plataforma(300 + 54, 500, pr),

               Plataforma(300, 500, pl), Plataforma(300 + 18, 500, pm), Plataforma(300 + 36, 500, pm),
               Plataforma(300 + 54, 500, pr),

               Plataforma(125, 525, pl), Plataforma(125 + 18, 525, pm), Plataforma(125 + 36, 525, pr),

               Plataforma(600, 450, pl), Plataforma(600 + 18, 450, pm), Plataforma(600 + 36, 450, pm),
               Plataforma(600 + 54, 450, pr),

               Plataforma(300 - 36, 150, pl), Plataforma(300 - 18, 150, pm), Plataforma(300, 150, pm),
               Plataforma(300 + 18, 150, pm), Plataforma(300 + 36, 150, pm), Plataforma(300 + 54, 150, pr),

               Plataforma(30, 150, pl), Plataforma(30 + 18, 150, pm), Plataforma(30 + 36, 150, pm),
               Plataforma(30 + 54, 150, pr),
               ]

platforms_2 = [Plataforma(30, 350, pl), Plataforma(30 + 18, 350, pm), Plataforma(30 + 36, 350, pm),
               Plataforma(30 + 54, 350, pr),
               Plataforma(30, 450, pl), Plataforma(30 + 18, 450, pm), Plataforma(30 + 36, 450, pm),
               Plataforma(30 + 54, 450, pr),
               Plataforma(30, 550, pl), Plataforma(30 + 18, 550, pm), Plataforma(30 + 36, 550, pm),
               Plataforma(30 + 54, 550, pr),
               Plataforma(30, 650, pl), Plataforma(30 + 18, 650, pm), Plataforma(30 + 36, 650, pm),
               Plataforma(30 + 54, 650, pr)
               ]

# inimigos para o level 1
lista_inimigos = [InimigoAmarelo(80, 370, 170), InimigoRoxo(600, 700, 500, -1), InimigoVerde(264, 150, 372),
                  InimigoVermelho(230, 550, 400, -1), InimigoAmarelo(600, 450, 672), InimigoVerde(500, 300, 572),
                  InimigoRoxo(400, 500, 300, -1), InimigoRoxo(192, 300, 75, 1), InimigoVermelho(500, 500, 340, 1)
                  ]

# Inimigo para o Level 2
chefao = Chefao(500, 700, 375)
level2.add(chefao)
inimigos2.add(chefao)

for ini in lista_inimigos:
    # Adicionando os inimigos nos grupos de sprites
    level1.add(ini)
    inimigos1.add(ini)

for plats in platforms_1:
    # Adicionando as plataformas nos grupos de sprites
    level1.add(plats)
    plataformas1.add(plats)

for plats in platforms_2:
    level2.add(plats)
    plataformas2.add(plats)
'''