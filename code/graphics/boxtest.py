import pygame
import sys

# Initialisation de pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zone de texte qui disparaît après appui sur 'E'")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police
font = pygame.font.Font(None, 36)

# Texte initial
text = "Hello"
text_rendered = font.render(text, True, BLACK)

# Variables de contrôle
text_visible = True

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vérifier si la touche 'E' est pressée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                text_visible = False

    # Remplir l'écran en blanc
    screen.fill(WHITE)

    # Si le texte est visible, l'afficher
    if text_visible:
        screen.blit(text_rendered, (50, 200))

    # Rafraîchir l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()
sys.exit()
