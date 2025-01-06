import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()
# Herramienta para gestionar los sonidos y música
pygame.mixer.init()

# Configuración de la pantalla del juego
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mIAu")

# Fuentes
font = pygame.font.Font("fonts/dogica.ttf", 15)
font.set_bold(True)

# Colores RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
BEIGE = (245, 245, 220)
RED = (255, 0, 0)

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Cargar y reproducir música de fondo
pygame.mixer.music.load("sounds/background_music.mp3")  
pygame.mixer.music.set_volume(0.2)  # Ajusta el volumen 
pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

# Cargar los efectos de sonidos
jump_sound = pygame.mixer.Sound("sounds/jump.mp3")
jump_sound.set_volume(0.3)  

item_pickup_sound = pygame.mixer.Sound("sounds/item_pickup.mp3")
item_pickup_sound.set_volume(0.3)

falls_sound = pygame.mixer.Sound("sounds/falls.mp3")
falls_sound.set_volume(0.4)

enemy_hit_sound = pygame.mixer.Sound("sounds/enemy_hit.mp3")
enemy_hit_sound.set_volume(0.1)

final_sound = pygame.mixer.Sound("sounds/final_sound.mp3")
final_sound.set_volume(0.2)

# Cargar imágenes del jugador
cat_img_1 = pygame.image.load("images/gatito.png")  # Imagen con las patas normales
cat_img_2 = pygame.image.load("images/gatito2.png")  # Imagen con las patas invertidas
cat_img_1 = pygame.transform.scale(cat_img_1, (50, 50))
cat_img_2 = pygame.transform.scale(cat_img_2, (50, 50))

# Variables para simular movimiento del personaje
cat_img = cat_img_1  # Carga la primera imagen
last_move_time = pygame.time.get_ticks()  # Guardar el tiempo de la última acción de movimiento
movement_interval = 200  # Intervalo de tiempo en milisegundos para alternar entre las imágenes

# Carga de imagenes de objetos
logo_img = pygame.image.load("images/logo.png")
logo_img = pygame.transform.scale(logo_img, (180, 130))

food_img = pygame.image.load("images/food.png")
food_img = pygame.transform.scale(food_img, (40, 40))

water_img = pygame.image.load("images/water.png")
water_img = pygame.transform.scale(water_img, (35, 35))

toy_img = pygame.image.load("images/toy.png")
toy_img = pygame.transform.scale(toy_img, (30, 45))

star_img = pygame.image.load("images/star.png")
star_img = pygame.transform.scale(star_img, (50, 50))

churu_img = pygame.image.load("images/churu.png")
churu_img = pygame.transform.scale(churu_img, (30, 50))

grass_img = pygame.image.load("images/grass.png")
grass_img = pygame.transform.scale(grass_img, (60, 60))

litter_img = pygame.image.load("images/litter.png")
litter_img = pygame.transform.scale(litter_img, (30, 30))

wool_img = pygame.image.load("images/wool.png")
wool_img = pygame.transform.scale(wool_img, (45, 45))

mouse_img = pygame.image.load("images/mouse.png")
mouse_img = pygame.transform.scale(mouse_img, (45, 45))

# Carga de imagenes de enemigos
vacuum_img = pygame.image.load("images/vacuum.png")
vacuum_img = pygame.transform.scale(vacuum_img, (60, 60))

drone_img = pygame.image.load("images/dron.png")
drone_img = pygame.transform.scale(drone_img, (50, 50))

car_img = pygame.image.load("images/car.png")
car_img = pygame.transform.scale(car_img, (50, 50))

bike_img = pygame.image.load("images/bike.png")
bike_img = pygame.transform.scale(bike_img, (65, 65))

# Fondos para los niveles
level_1_bg = pygame.image.load("images/kitchen.png")
level_1_bg = pygame.transform.scale(level_1_bg, (WIDTH, HEIGHT))

level_2_bg = pygame.image.load("images/living_room.png")
level_2_bg = pygame.transform.scale(level_2_bg, (WIDTH, HEIGHT))

level_3_bg = pygame.image.load("images/attic.png")
level_3_bg = pygame.transform.scale(level_3_bg, (WIDTH, HEIGHT))

level_4_bg = pygame.image.load("images/garage.png")
level_4_bg = pygame.transform.scale(level_4_bg, (WIDTH, HEIGHT))

level_5_bg = pygame.image.load("images/bathroom.png")
level_5_bg = pygame.transform.scale(level_5_bg, (WIDTH, HEIGHT))

level_6_bg = pygame.image.load("images/backyard.png")
level_6_bg = pygame.transform.scale(level_6_bg, (WIDTH, HEIGHT))

level_7_bg = pygame.image.load("images/bedroom.png")
level_7_bg = pygame.transform.scale(level_7_bg, (WIDTH, HEIGHT))

# Fondo pantalla inicial
start_screen_bg = pygame.image.load("images/pantalla_inicio.png")  # Imagen para la pantalla de inicio
start_screen_bg = pygame.transform.scale(start_screen_bg, (WIDTH, HEIGHT))

# Fondo pantalla final
end_screen_bg = pygame.image.load("images/pantalla_final.png")
end_screen_bg = pygame.transform.scale(end_screen_bg, (WIDTH, HEIGHT))

# Plataforma sprite
platform_texture = pygame.image.load("images/platform_texture.png")  # Imagen para las plataformas
platform_texture = pygame.transform.scale(platform_texture, (100, 20))

# Variables globales
player_name = ""
current_level = 1
# Set para almacenar los objetos recogidos
collected_objects = set()

# Configuración del jugador
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5
player_jump = -15
player_velocity_y = 0
on_ground = True
player_facing_right = True

# Contador para la animación de caminar
walk_timer = 0
walk_switch_time = 10  # Tiempo de espera antes de cambiar la imagen

# Función para reflejar la imagen del personaje
def flip_image(image, flip):
    if flip:
        return pygame.transform.flip(image, True, False)
    return image

# Función para añadir iconos obtenidos en sección superior
def get_icon_for_object(coordinates):
    # Lógica para determinar el icono en base a las coordenadas
    if coordinates == (100, 200):  # Coordenadas para la comida
        return food_img  # Devolver el icono de comida
    elif coordinates == (300, 400):  # Coordenadas para el juguete
        return toy_img  # Devolver el icono de juguete
    elif coordinates == (500, 600):  # Coordenadas para el agua
        return water_img  # Devolver el icono de agua
    
# Configuración de enemigos
enemies = []
def create_enemy(x, y, img, platform):
    rect = pygame.Rect(x, y, 50, 50)
    return {"rect": rect, "img": img, "direction": random.choice([-1, 1]), "platform": platform}

# Aplicar efecto de opacidad al fondo
def apply_background_effect(background):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(100)  # Ajustar transparencia
    blurred_background = background.copy()
    blurred_background.blit(overlay, (0, 0))
    return blurred_background

# Configuración de niveles
levels = {
    1: {
        "background": apply_background_effect(level_1_bg),
        "object": food_img,
        "enemies": [vacuum_img],
        "message": "Has conseguido comida",
        "object_position": (700, 565, 30, 30), 
    },
    2: {
        "background": apply_background_effect(level_2_bg),
        "object": water_img,
        "enemies": [drone_img, vacuum_img],
        "message": "Has conseguido agua",
        "object_position": (600, 465, 30, 30),
    },
    3: {
        "background": apply_background_effect(level_3_bg),
        "object": toy_img,
        "enemies": [car_img, vacuum_img, drone_img],
        "message": "Has conseguido el resorte",
        "object_position": (760, 160, 30, 30),
    },
    4: {
        "background": apply_background_effect(level_4_bg),
        "object": churu_img,
        "enemies": [car_img, drone_img, vacuum_img],
        "message": "Has conseguido churu",
        "object_position": (650, 150, 30, 30),
    },
    5: {
        "background": apply_background_effect(level_5_bg),
        "object": grass_img,
        "enemies": [car_img, vacuum_img, drone_img],
        "message": "Has conseguido hierba",
        "object_position": (600, 250, 30, 30),
    },
    6: {
        "background": apply_background_effect(level_6_bg),
        "object": wool_img,
        "enemies": [car_img, drone_img, vacuum_img, bike_img],
        "message": "Has conseguido ovillo",
        "object_position": (100, 160, 30, 30),
    },
    7: {
        "background": apply_background_effect(level_7_bg),
        "object": mouse_img,
        "enemies": [car_img, drone_img, vacuum_img, bike_img],
        "message": "Has conseguido el ratoncito",
        "object_position": (650, 160, 30, 30),
    }
}

# Plataformas
platforms_by_level = {
    1: [
        pygame.Rect(0, 600, 900, 20), # Plataforma inicial
        pygame.Rect(100, 500, 300, 20),
        pygame.Rect(550, 500, 200, 20),
        pygame.Rect(400, 400, 150, 20),
    ],
    2: [
        pygame.Rect(0, 600, 900, 20),  # Plataforma inicial 
        pygame.Rect(150, 500, 750, 20),
        pygame.Rect(250, 400, 500, 20),
    ],
    3: [
        pygame.Rect(0, 600, 900, 20),  # Plataforma inicial 
        pygame.Rect(150, 500, 650, 20),
        pygame.Rect(20, 400, 500, 20),
        pygame.Rect(600, 350, 200, 20),
        pygame.Rect(150, 300, 400, 20),
        pygame.Rect(600, 200, 200, 20),
    ],
    4: [
        pygame.Rect(0, 600, 900, 20),  # Plataforma inicial 
        pygame.Rect(200, 500, 600, 20),
        pygame.Rect(50, 400, 750, 20),
        pygame.Rect(150, 300, 500, 20),
        pygame.Rect(500, 200, 200, 20),
    ],
    5: [
        pygame.Rect(0, 600, 800, 20),  # Plataforma inicial 
        pygame.Rect(200, 500, 600, 20),
        pygame.Rect(80, 400, 600, 20),
        pygame.Rect(150, 300, 250, 20),
        pygame.Rect(500, 300, 250, 20),
    ],
    6: [
        pygame.Rect(20, 600, 850, 20),  # Plataforma inicial 
        pygame.Rect(20, 500, 400, 20),
        pygame.Rect(550, 500, 300, 20),
        pygame.Rect(200, 400, 700, 20),
        pygame.Rect(150, 300, 500, 20),
        pygame.Rect(100, 200, 200, 20),
    ],
    7: [
        pygame.Rect(20, 600, 750, 20),  # Plataforma inicial 
        pygame.Rect(50, 500, 600, 20),
        pygame.Rect(100, 400, 300, 20),
        pygame.Rect(500, 400, 300, 20),
        pygame.Rect(150, 300, 300, 20),
        pygame.Rect(500, 200, 200, 20),
    ]
}

# Función de cambio de niveles
def reset_level():
    global player, enemies, collected_items, platforms
    player.topleft = (20, 600)
    player_x, player_y = player.topleft  # Coordenadas del gatito
    collected_items = 0
    enemies.clear()
    
    global platforms  # Aseguramos que se actualicen las plataformas globales
    platforms = platforms_by_level.get(current_level, [])
    
    if current_level <= len(levels):
        enemy_images = levels[current_level]["enemies"]
        for i, platform in enumerate(platforms[:len(enemy_images)]):
            while True:  # Bucle para encontrar una posición válida
                # Generar posición inicial del enemigo
                enemy_x = platform.left + random.randint(0, platform.width - 50)
                enemy_y = platform.top - 50

                # Verificar que no esté en la zona del gatito (exclusión o zona segura)
                if not (player_x - 150 <= enemy_x <= player_x + 150 and 
                        player_y - 150 <= enemy_y <= player_y + 150):
                    break
            
            # Crear enemigo en una posición válida
            enemy = create_enemy(enemy_x, enemy_y, enemy_images[i], platform)
            enemies.append(enemy)

# Función que dibuja todos los elementos del nivel actual en la pantalla.
def draw_level():
    screen.blit(levels[current_level]["background"], (0, 0))  # Fondo adaptado para cada nivel
    for platform in platforms:
        scaled_platform_texture = pygame.transform.scale(platform_texture, (platform.width, platform.height))
        screen.blit(scaled_platform_texture, platform.topleft)  # Dibuja la plataforma con la textura escalada

    for enemy in enemies:
        screen.blit(enemy["img"], enemy["rect"])

    # Usar la posición definida de los objetos a recoger
    object_position = levels[current_level]["object_position"]
    object_rect = pygame.Rect(object_position[0], object_position[1], 30, 30)
    screen.blit(levels[current_level]["object"], object_rect)
    return object_rect

# Función de movimiento de los enemigos
def move_enemies():
    enemy_speed = 2 + int(3 * (current_level - 1)**0.5)  # Velocidad con crecimiento lento
    for enemy in enemies:
        if enemy["platform"]:
            enemy["rect"].x += enemy["direction"] * enemy_speed
            if enemy["rect"].left <= enemy["platform"].left or enemy["rect"].right >= enemy["platform"].right:
                enemy["direction"] *= -1

# Función para mostrar información en la parte superior en los niveles
def display_ui():
    ui_background = pygame.Surface((WIDTH, 70))
    ui_background.fill((0, 0, 0))
    screen.blit(ui_background, (0, 0))

    name_text = font.render(f"Tu gatitx: {player_name}", True, BEIGE)
    screen.blit(name_text, (10, 10))

    items_text = font.render("Objetos recogidos:", True, BEIGE)
    screen.blit(items_text, (10, 40))

    # Redimensionar los objetos recogidos al tamaño deseado
    resized_objects = [pygame.transform.scale(obj, (30, 30)) for obj in collected_objects]

    # Dibujar los iconos de los objetos recogidos
    x_offset = 280  # Ajustamos la posición inicial de los iconos
    
    # Mostrar los iconos redimensionados
    for obj in resized_objects:
        screen.blit(obj, (x_offset, 35))  # Dibujamos el icono redimensionado
        x_offset += 40  # Espaciado entre los iconos

# Pantalla inicial
MAX_NAME_LENGTH = 15  # Define el límite de caracteres que puede tener el nombre

def display_start_screen():
    global player_name, error_message
    screen.blit(start_screen_bg, (0, 0))

    box_width = WIDTH - 300
    box_height = 250
    box_x = (WIDTH - box_width) // 2
    box_y = HEIGHT // 3
    pygame.draw.rect(screen, BEIGE, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

    title = font.render("¡BIENVENENIDX A mIAu!", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, box_y + 30))

    prompt = font.render("Escribe el nombre de tu gatitx: ", True, BLACK)
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, box_y + 90))

    enter_message = font.render("Presiona < Enter > para comenzar", True, BLACK)
    screen.blit(enter_message, (WIDTH // 2 - enter_message.get_width() // 2, box_y + 190))

    screen.blit(logo_img, (5, 5))

    pygame.display.flip() 

    name_entered = False
    input_box_width = 300 # ancho
    input_box = pygame.Rect(WIDTH // 2 - input_box_width // 2, box_y + 130, input_box_width, 40)
    error_message = ""

    while not name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name.strip() == "":
                        error_message = "No has ingresado el nombre de tu gatitx"
                    else:
                        name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    if len(player_name) < MAX_NAME_LENGTH:
                         player_name += event.unicode
                    else:
                        error_message = "El nombre no debe exceder 15 caracteres"

        pygame.draw.rect(screen, WHITE, input_box)
        pygame.draw.rect(screen, BLACK, input_box, 2)

        text_surface = font.render(player_name, True, BLACK)
        text_x = input_box.x + (input_box.width - text_surface.get_width()) // 2
        text_y = input_box.y + (input_box.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

        # Mostrar mensaje de error si existe
        if error_message:
            error_surface = font.render(error_message, True, RED)
            screen.blit(error_surface, (WIDTH // 2 - error_surface.get_width() // 2, box_y + 220))

        pygame.display.flip()

# Pantalla final
def display_end_screen():
    screen.blit(end_screen_bg, (0, 0))
    final_sound.play()

    # Función para renderizar texto con fondo negro
    def render_with_black_background(text, color, pos):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        
        # Fondo negro detrás del texto (ajustamos el tamaño del rectángulo)
        padding = 10  # Espaciado entre el texto y el fondo
        background_rect = pygame.Rect(text_rect.x - padding, text_rect.y - padding, text_rect.width + 2 * padding, text_rect.height + 2 * padding)
        pygame.draw.rect(screen, BLACK, background_rect)  # Dibuja el fondo negro
        screen.blit(text_surface, text_rect)  # Dibuja el texto sobre el fondo negro

    # Llamadas a la función para los mensajes
    render_with_black_background(f"¡Lo lograste! '{player_name}' ha superado todos los peligros.", WHITE, (WIDTH // 2, HEIGHT // 7))
    render_with_black_background(f"Gracias a ti, ahora '{player_name}' puede disfrutar", WHITE, (WIDTH // 2, HEIGHT // 5))
    render_with_black_background("de su comida, de su agua y de su juguete en paz.", WHITE, (WIDTH // 2, HEIGHT // 4))
    render_with_black_background("* Presiona < Enter > para jugar de nuevo. *", WHITE, (WIDTH // 2, HEIGHT // 2 + 100))

    # Dibujar los iconos de comida, agua y juguete
    icon_x = WIDTH // 2 - 100  
    icon_y = HEIGHT - 200

    # Dibuja el icono de la comida
    screen.blit(food_img, (icon_x, icon_y))
    # Dibuja el icono del agua
    screen.blit(water_img, (icon_x + 60, icon_y))  
    # Dibuja el icono del juguete
    screen.blit(toy_img, (icon_x + 120, icon_y))  
    # Dibuja el icono de las estrellas
    screen.blit(star_img, (icon_x - 70, HEIGHT - 210)) 
    screen.blit(star_img, (icon_x + 180, HEIGHT - 210)) 
    # Dibujar el logo
    screen.blit(logo_img, (5, 550))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
                reset_level()
                global current_level
                current_level = 1

# Pantalla de transición entre niveles
def display_level_transition(level):
    transition_screen_bg = pygame.Surface((WIDTH, HEIGHT))
    transition_screen_bg.fill(BLACK)  # Fondo negro
    screen.blit(transition_screen_bg, (0, 0))

    # Mensajes
    title = font.render(f"¡Felicidades! Has completado el Nivel {level}", True, WHITE)
    instruction = font.render("Presiona < Enter > para continuar", True, WHITE)

    # Mensaje específico del nivel
    if level == 1:
        level_message = font.render("Has conseguido comida", True, WHITE)
    elif level == 2:
        level_message = font.render("Has conseguido agua", True, WHITE)
    elif level == 3:
        level_message = font.render("Has conseguido resorte", True, WHITE)
    elif level == 4:
        level_message = font.render("Has conseguido churu", True, WHITE) 
    elif level == 5:
        level_message = font.render("Has conseguido hierba", True, WHITE)
    elif level == 6:
        level_message = font.render("Has conseguido ovillo", True, WHITE)
    elif level == 7:
        level_message = font.render("Has conseguido ratoncito", True, WHITE)  

    # Iconos del gatito y objeto obtenido
    cat_icon = cat_img_1  # Icono del gatito
    object_icon = levels[level]["object"]  # Icono del objeto correspondiente al nivel

    # Coordenadas de los elementos
    cat_x, cat_y = WIDTH // 4 - cat_icon.get_width() // 2, HEIGHT // 2 - 50
    object_x, object_y = 3 * WIDTH // 4 - object_icon.get_width() // 2, HEIGHT // 2 - 50

    # Centrar mensajes en pantalla
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(level_message, (WIDTH // 2 - level_message.get_width() // 2, HEIGHT // 3 + 40))
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT // 2 + 100))

    # Dibujar los iconos en pantalla
    screen.blit(cat_icon, (cat_x, cat_y))
    screen.blit(object_icon, (object_x, object_y))

    # Etiquetas debajo de los iconos
    cat_label = font.render("Tu Gatito", True, WHITE)
    object_label = font.render("Premio", True, WHITE)
    screen.blit(cat_label, (cat_x + cat_icon.get_width() // 2 - cat_label.get_width() // 2, cat_y + 60))
    screen.blit(object_label, (object_x + object_icon.get_width() // 2 - object_label.get_width() // 2, object_y + 60))

    pygame.display.flip()

    # Esperar a que el jugador presione Enter
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
    global current_level, collected_items, player_velocity_y, on_ground, player_facing_right, cat_img, last_move_time

    clock = pygame.time.Clock()
    running = True

    display_start_screen()
    reset_level()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Si el gato se cae de la pantalla (fuera de los límites)
        if player.y > HEIGHT:  # Si el gato se sale por la parte inferior
            falls_sound.play()
            reset_level()  # Resetear al inicio del nivel
            player_velocity_y = 0  # Detener la velocidad de caída

        # Movimiento del jugador
        player_velocity_y += 1  # Gravedad
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
            player_facing_right = False
            if pygame.time.get_ticks() - last_move_time > movement_interval:
                cat_img = cat_img_1 if cat_img == cat_img_2 else cat_img_2
                last_move_time = pygame.time.get_ticks()  # Actualizamos el tiempo del último movimiento
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
            player_facing_right = True
            if pygame.time.get_ticks() - last_move_time > movement_interval:
                cat_img = cat_img_1 if cat_img == cat_img_2 else cat_img_2
                last_move_time = pygame.time.get_ticks()  # Actualizamos el tiempo del último movimiento
        if keys[pygame.K_SPACE] and on_ground:
            player_velocity_y = player_jump
            on_ground = False
            jump_sound.play()

        # Actualización de la posición vertical del jugador
        player.y += player_velocity_y

        # Verificar si el jugador colisiona con las plataformas
        on_ground = False
        for platform in platforms:
            if player.colliderect(platform) and player_velocity_y > 0:
                player.bottom = platform.top
                player_velocity_y = 0
                on_ground = True

        object_rect = draw_level()
        flipped_cat_img = flip_image(cat_img, not player_facing_right)
        screen.blit(flipped_cat_img, player)

        move_enemies()
        for enemy in enemies:
            if player.colliderect(enemy["rect"]):
                enemy_hit_sound.play()
                reset_level()
        
        if player.colliderect(object_rect):
            item_pickup_sound.play()
            collected_objects.add(levels[current_level]["object"])  # Añadir la imagen del objeto
            collected_items += 1  # Incrementar el contador de objetos recogidos
            display_level_transition(current_level)  # Mostrar la pantalla de transición
            current_level += 1
            if current_level > len(levels):
                display_end_screen()  # Mostrar la pantalla final
                reset_level()  # Reiniciar el nivel
                current_level = 1  # Volver al primer nivel
                collected_items = 0  # Reiniciar los objetos recogidos
                display_start_screen()  # Mostrar la pantalla inicial nuevamente
            else:
                reset_level()  # Reiniciar el nuevo nivel

        display_ui()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()