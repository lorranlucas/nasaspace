import pygame
import random

# Inicialização do pygame
pygame.init()

# Definir tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Criar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pouse o foguete na plataforma")

# Definir o relógio para controlar o FPS
clock = pygame.time.Clock()

# Carregar imagens
background_image = pygame.image.load('fundo(2).jpg')  # Substitua pelo caminho da sua imagem de fundo
rocket_image = pygame.image.load('foguete.png')  # Substitua pelo caminho da sua imagem de foguete
rocket_image = pygame.transform.scale(rocket_image, (30, 50))  # Redimensionar se necessário

# Criar a plataforma (balsa)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
platform_x = (SCREEN_WIDTH - PLATFORM_WIDTH) // 2
platform_y = SCREEN_HEIGHT - 40
platform_speed = 7
platform_image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
platform_image.fill((169, 169, 169))  # Cinza para a plataforma

# Criar o foguete
rocket_width, rocket_height = rocket_image.get_size()
rocket_x = random.randint(0, SCREEN_WIDTH - rocket_width)
rocket_y = 0
rocket_speed = 2

# Variável de controle
game_over = False

# Função para desenhar a plataforma
def draw_platform(x, y):
    screen.blit(platform_image, (x, y))

# Função para desenhar o foguete
def draw_rocket(x, y):
    screen.blit(rocket_image, (x, y))

# Função para verificar se o foguete pousou na plataforma
def check_landing(rocket_x, rocket_y, platform_x, platform_y):
    if platform_x < rocket_x < platform_x + PLATFORM_WIDTH and rocket_y + rocket_height >= platform_y:
        return True
    return False

# Loop principal do jogo
while not game_over:
    # Desenhar o fundo (céu e mar)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x < SCREEN_WIDTH - PLATFORM_WIDTH:
        platform_x += platform_speed

    # Movimentar o foguete para baixo
    rocket_y += rocket_speed

    # Verificar se o foguete pousou
    if check_landing(rocket_x, rocket_y, platform_x, platform_y):
        print("Foguete pousou com sucesso!")
        #game_over = True

    # Verificar se o foguete caiu na água
    if rocket_y > SCREEN_HEIGHT:
        print("Foguete caiu na água!")
        #game_over = True

    # Desenhar o foguete e a plataforma
    draw_platform(platform_x, platform_y)
    draw_rocket(rocket_x, rocket_y)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS
    clock.tick(60)

pygame.quit()
