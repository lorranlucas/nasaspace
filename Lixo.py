import pygame
import random
import math

# Inicializa o Pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caça ao Lixo Espacial")

# FPS
clock = pygame.time.Clock()
FPS = 60

# Carregar imagens (imagens representativas da Terra, ISS e lixo)
earth_img = pygame.image.load("terra.png")  # Adicione imagem da Terra
iss_img = pygame.image.load("iss.png")      # Adicione imagem da ISS
debris_img = pygame.image.load("panela.png")# Adicione imagem de lixo espacial

# Funções auxiliares
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Classe para a Terra
class Earth:
    def __init__(self):
        self.x = WIDTH // 2 - 50
        self.y = HEIGHT // 2 - 50
        self.image = pygame.transform.scale(earth_img, (100, 100))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Classe para a Estação Espacial Internacional (orbita a Terra)
class ISS:
    def __init__(self):
        self.angle = 0  # Ângulo inicial da órbita
        self.orbital_radius = 200  # Raio da órbita da ISS (constante para circular)
        self.orbital_speed = 0.01  # Velocidade de movimento orbital
        self.earth_x = WIDTH // 2
        self.earth_y = HEIGHT // 2
        self.image = pygame.transform.scale(iss_img, (50, 50))
        self.x = self.earth_x + self.orbital_radius * math.cos(self.angle)
        self.y = self.earth_y + self.orbital_radius * math.sin(self.angle)

    def move(self):
        self.angle += self.orbital_speed  # Atualiza o ângulo da órbita
        self.x = self.earth_x + self.orbital_radius * math.cos(self.angle)
        self.y = self.earth_y + self.orbital_radius * math.sin(self.angle)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Classe para o lixo espacial em órbita elíptica
class SpaceDebris:
    def __init__(self):
        self.angle = random.uniform(0, 2 * math.pi)  # Ângulo inicial aleatório
        self.semi_major_axis = random.randint(150, 250)  # Eixo maior da elipse
        self.semi_minor_axis = random.randint(100, 200)  # Eixo menor da elipse
        self.orbital_speed = random.uniform(0.01, 0.03)  # Velocidade orbital
        self.earth_x = WIDTH // 2
        self.earth_y = HEIGHT // 2
        self.x = self.earth_x + self.semi_major_axis * math.cos(self.angle)
        self.y = self.earth_y + self.semi_minor_axis * math.sin(self.angle)
        self.image = pygame.transform.scale(debris_img, (30, 30))

    def move(self):
        # Atualiza a posição usando a equação da órbita elíptica
        self.angle += self.orbital_speed
        self.x = self.earth_x + self.semi_major_axis * math.cos(self.angle)
        self.y = self.earth_y + self.semi_minor_axis * math.sin(self.angle)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Função principal do jogo
def game_loop():
    earth = Earth()
    iss = ISS()
    debris_list = [SpaceDebris() for _ in range(5)]  # Criando 5 pedaços de lixo no começo
    running = True
    score = 0

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhar a Terra
        earth.draw()

        # Movimento e desenho da ISS em órbita circular
        iss.move()
        iss.draw()

        # Movimento e desenho do lixo espacial em órbita elíptica
        for debris in debris_list:
            debris.move()
            debris.draw()

            # Verifica colisão com a ISS
            if distance(debris.x, debris.y, iss.x, iss.y) < 30:
                print("A ISS foi atingida por lixo espacial!")
                #running = False

            # Verifica colisão com a Terra
            if distance(debris.x, debris.y, earth.x, earth.y) < 50:
                print("A Terra foi atingida por lixo espacial!")
                #running = False

        # Atualizar display
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

# Iniciar o jogo
game_loop()
