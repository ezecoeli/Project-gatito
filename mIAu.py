import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mIAu")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
BEIGE = (245, 245, 220)
RED = (255, 0, 0)

# Cargar imágenes
cat_img = pygame.image.load("gatito.png")
cat_img = pygame.transform.scale(cat_img, (50, 50))

food_img = pygame.image.load("comida.png")
food_img = pygame.transform.scale(food_img, (30, 30))

water_img = pygame.image.load("agua.png")
water_img = pygame.transform.scale(water_img, (30, 30))

toy_img = pygame.image.load("juguete.png")
toy_img = pygame.transform.scale(toy_img, (30, 30))

vacuum_img = pygame.image.load("aspiradora.png")
vacuum_img = pygame.transform.scale(vacuum_img, (50, 50))

drone_img = pygame.image.load("dron.png")
drone_img = pygame.transform.scale(drone_img, (50, 50))

car_img = pygame.image.load("auto.png")
car_img = pygame.transform.scale(car_img, (50, 50))

# Fondo pantalla inicial
start_screen_bg = pygame.image.load("pantalla_inicio.png")
start_screen_bg = pygame.transform.scale(start_screen_bg, (WIDTH, HEIGHT))

# Fuentes
font = pygame.font.Font(None, 36)

# Variables globales
player_name = ""
current_level = 1
collected_items = 0

# Configuración del jugador
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5
player_jump = -15
player_velocity_y = 0
on_ground = True
player_facing_right = True

# Configuración de enemigos
enemies = []
def create_enemy(x, y, img):
    rect = pygame.Rect(x, y, 50, 50)
    return {"rect": rect, "img": img, "direction": random.choice([-1, 1])}

# Configuración de niveles
levels = {
    1: {"background": BLUE, "object": food_img, "enemies": [vacuum_img]},
    2: {"background": BLUE, "object": water_img, "enemies": [drone_img]},
    3: {"background": BLUE, "object": toy_img, "enemies": [car_img]}
}

# Plataforma
platforms = [
    pygame.Rect(100, 550, 600, 20),
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(400, 350, 200, 20),
]

# Funciones
def reset_level():
    global player, enemies, collected_items
    player.topleft = (100, 500)
    enemies = [create_enemy(random.randint(200, WIDTH - 100), random.randint(300, HEIGHT - 100), levels[current_level]["enemies"][0])]
    collected_items = 0

def draw_level():
    screen.fill(levels[current_level]["background"])
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

    for enemy in enemies:
        screen.blit(enemy["img"], enemy["rect"])

    object_rect = pygame.Rect(700, 500, 30, 30)
    screen.blit(levels[current_level]["object"], object_rect)
    return object_rect

def move_enemies():
    for enemy in enemies:
        enemy["rect"].x += enemy["direction"] * 2
        if enemy["rect"].left <= 0 or enemy["rect"].right >= WIDTH:
            enemy["direction"] *= -1

def display_ui():
    name_text = font.render(f"Nombre: {player_name}", True, BLACK)
    screen.blit(name_text, (10, 10))

    items_text = font.render(f"Objetos recogidos: {collected_items}/1", True, BLACK)
    screen.blit(items_text, (10, 40))

# Pantalla inicial
def display_start_screen():
    global player_name
    screen.blit(start_screen_bg, (0, 0))

    # Dibujar recuadro para contraste
    box_width = WIDTH - 100
    box_height = 200
    box_x = (WIDTH - box_width) // 2
    box_y = HEIGHT // 3
    pygame.draw.rect(screen, BEIGE, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

    title = font.render("Bienvenido a mIAu", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, box_y + 20))

    prompt = font.render("Escribe el nombre de tu gatito: ", True, BLACK)
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, box_y + 80))

    enter_message = font.render("Presiona -Enter- para comenzar", True, BLACK)
    screen.blit(enter_message, (WIDTH // 2 - enter_message.get_width() // 2, box_y + 155))

    pygame.display.flip()

    name_entered = False
    input_box = pygame.Rect(WIDTH // 2 - 100, box_y + 110, 200, 40)
    error_message = ""

    while not name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name.strip() == "":
                        error_message = "No has ingresado el nombre de tu gatito"
                    else:
                        name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.draw.rect(screen, WHITE, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)

        text_surface = font.render(player_name, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        if error_message:
            error_surface = font.render(error_message, True, RED)
            screen.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, box_y + 160))

        pygame.display.flip()

# Pantalla final
def display_end_screen():
    screen.fill(WHITE)

    message = font.render(f"¡Lo lograste! {player_name} ha superado todos los peligros.", True, BLACK)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 3))

    sub_message = font.render("Gracias a ti, ahora puede disfrutar de su comida, agua y juguete en paz.", True, BLACK)
    screen.blit(sub_message, (WIDTH // 2 - sub_message.get_width() // 2, HEIGHT // 3 + 40))

    restart_message = font.render("Presiona -Enter- para jugar de nuevo.", True, BLACK)
    screen.blit(restart_message, (WIDTH // 2 - restart_message.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

# Bucle principal
def main():
    global current_level, collected_items, player_velocity_y, on_ground, player_facing_right

    clock = pygame.time.Clock()
    running = True

    display_start_screen()
    reset_level()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
            player_facing_right = False
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
            player_facing_right = True
        if keys[pygame.K_SPACE] and on_ground:
            player_velocity_y = player_jump
            on_ground = False

        player_velocity_y += 1  # Simula la gravedad
        player.y += player_velocity_y

        # Comprobar colisiones con plataformas
        on_ground = False
        for platform in platforms:
            if player.colliderect(platform) and player_velocity_y >= 0:
                player.bottom = platform.top
                player_velocity_y = 0
                on_ground = True

        # Dibujar nivel
        object_rect = draw_level()

        # Mover enemigos y comprobar colisiones
        move_enemies()
        for enemy in enemies:
            if player.colliderect(enemy["rect"]):
                print(f"{player_name} ha sido atrapado por un enemigo. Reiniciando nivel...")
                reset_level()

        # Comprobar si se recoge el objeto
        if player.colliderect(object_rect):
            collected_items += 1
            if collected_items >= 1:
                current_level += 1
                if current_level > 3:
                    display_end_screen()
                    current_level = 1
                    reset_level()
                else:
                    print(f"Nivel {current_level}. ¡Avanza al siguiente desafío!")
                    reset_level()

        # Dibujar jugador
        flipped_cat = pygame.transform.flip(cat_img, not player_facing_right, False)
        screen.blit(flipped_cat, player)

        # Mostrar interfaz
        display_ui()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
