import pygame
import math
import random

# Inicialização do pygame
pygame.init()

# Definir tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Criar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Órbitas do Sistema Solar")

# Definir o relógio para controlar o FPS
clock = pygame.time.Clock()

# Definir cores
YELLOW = (255, 255, 0)

# Carregar as imagens dos planetas e do sol
sun_image = pygame.image.load('sun.png')
sun_image = pygame.transform.scale(sun_image, (60, 60))  # Ajuste o tamanho conforme necessário

# Substitua pelos caminhos corretos das suas imagens
planet_images = {
    "Mercury": pygame.transform.scale(pygame.image.load('mercury.png'), (20, 20)),
    "Venus": pygame.transform.scale(pygame.image.load('venus.png'), (25, 25)),
    "Earth": pygame.transform.scale(pygame.image.load('earth.png'), (30, 30)),
    "Mars": pygame.transform.scale(pygame.image.load('mars.png'), (20, 20)),
    "Jupiter": pygame.transform.scale(pygame.image.load('jupiter.png'), (50, 50)),
    "Saturn": pygame.transform.scale(pygame.image.load('saturn.png'), (45, 45)),
    "Uranus": pygame.transform.scale(pygame.image.load('uranus.png'), (40, 40)),
    "Neptune": pygame.transform.scale(pygame.image.load('neptune.png'), (40, 40))
}

# Dados dos planetas
planets = [
    {"name": "Mercury", "radius": 60, "speed": 0.04},
    {"name": "Venus", "radius": 90, "speed": 0.03},
    {"name": "Earth", "radius": 120, "speed": 0.02},
    {"name": "Mars", "radius": 150, "speed": 0.015},
    {"name": "Jupiter", "radius": 200, "speed": 0.008},
    {"name": "Saturn", "radius": 250, "speed": 0.006},
    {"name": "Uranus", "radius": 300, "speed": 0.004},
    {"name": "Neptune", "radius": 350, "speed": 0.003}
]

# Posição inicial dos planetas (ângulo)
for planet in planets:
    planet["angle"] = random.uniform(0, 2 * math.pi)

# Função para desenhar o Sol no centro
def draw_sun():
    screen.blit(sun_image, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 30))  # Ajuste para o centro

# Função para desenhar os planetas
def draw_planets():
    for planet in planets:
        # Atualizar posição (ângulo)
        planet["angle"] += planet["speed"]
        x = SCREEN_WIDTH // 2 + math.cos(planet["angle"]) * planet["radius"]
        y = SCREEN_HEIGHT // 2 + math.sin(planet["angle"]) * planet["radius"]
        
        # Desenhar o planeta como imagem
        planet_image = planet_images[planet["name"]]
        planet_rect = planet_image.get_rect(center=(int(x), int(y)))
        screen.blit(planet_image, planet_rect)

# Loop principal do jogo
running = True
while running:
    # Desenhar o fundo (preto)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenhar o Sol e os planetas
    draw_sun()
    draw_planets()

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS
    clock.tick(60)

pygame.quit()
