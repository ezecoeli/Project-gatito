import pygame
import random
import sys
import math
import time

# Inicialización de Pygame
pygame.init()
# Herramienta para gestionar los sonidos y música
pygame.mixer.init()

# Configuración de la pantalla del juego
WIDTH, HEIGHT = 1000, 800
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
GREEN = (0, 255, 0)   
YELLOW = (255, 255, 0)  
PURPLE = (128, 0, 128)  

# Reloj para controlar FPS
clock = pygame.time.Clock()
FPS = 60

# Cargar y reproducir música de fondo
start_screen_music = "sounds/start_screen_music.mp3"
level_music = "sounds/level_music.mp3"
end_screen_music = "sounds/end_screen_music.mp3"
game_over_music = "sounds/game_over_music.mp3"

# Cargar los efectos de sonidos
jump_sound = pygame.mixer.Sound("sounds/jump.mp3")
jump_sound.set_volume(0.4)  

item_pickup_sound = pygame.mixer.Sound("sounds/item_pickup.mp3")
item_pickup_sound.set_volume(0.5)

falls_sound = pygame.mixer.Sound("sounds/falls.mp3")
falls_sound.set_volume(0.5)

enemy_hit_sound = pygame.mixer.Sound("sounds/enemy_hit.mp3")
enemy_hit_sound.set_volume(0.3)

game_over_sound = pygame.mixer.Sound("sounds/game_over_sound.mp3")
game_over_sound.set_volume(0.3)

final_sound = pygame.mixer.Sound("sounds/final_sound.mp3")
final_sound.set_volume(0.4)

# Cargar imágenes del jugador
cat_img_1 = pygame.image.load("images/gatito.png")  # Imagen con las patas normales
cat_img_2 = pygame.image.load("images/gatito2.png")  # Imagen con las patas invertidas
cat_img_1 = pygame.transform.scale(cat_img_1, (50, 50))
cat_img_2 = pygame.transform.scale(cat_img_2, (50, 50))

# Variables para simular movimiento del personaje
cat_img = cat_img_1  # Carga la primera imagen
last_move_time = pygame.time.get_ticks()  # Guardar el tiempo de la última acción de movimiento
movement_interval = 200  # Intervalo de tiempo en milisegundos para alternar entre las imágenes

# Carga de imágenes
logo_img = pygame.image.load("images/logo.png")
logo_img = pygame.transform.scale(logo_img, (180, 130))

controls_img = pygame.image.load("images/controls.png")
controls_img = pygame.transform.scale(controls_img, (200, 100))

heart_img = pygame.image.load("images/heart.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))

quit_img = pygame.image.load("images/quit.png")
quit_img = pygame.transform.scale(quit_img, (100, 30))

# Carga de imágenes de objetos
food_img = pygame.image.load("images/food.png")
food_img = pygame.transform.scale(food_img, (50, 40))

water_img = pygame.image.load("images/water.png")
water_img = pygame.transform.scale(water_img, (45, 35))

toy_img = pygame.image.load("images/toy.png")
toy_img = pygame.transform.scale(toy_img, (30, 45))

star_img = pygame.image.load("images/star.png")
star_img = pygame.transform.scale(star_img, (50, 50))

churu_img = pygame.image.load("images/churu.png")
churu_img = pygame.transform.scale(churu_img, (30, 50))

grass_img = pygame.image.load("images/grass.png")
grass_img = pygame.transform.scale(grass_img, (60, 60))

litter_img = pygame.image.load("images/litter.png")
litter_img = pygame.transform.scale(litter_img, (55, 55))

wool_img = pygame.image.load("images/wool.png")
wool_img = pygame.transform.scale(wool_img, (45, 45))

mouse_img = pygame.image.load("images/mouse.png")
mouse_img = pygame.transform.scale(mouse_img, (45, 45))

box_img = pygame.image.load("images/box.png")
box_img = pygame.transform.scale(box_img, (55, 55))

bed_img = pygame.image.load("images/bed.png")
bed_img = pygame.transform.scale(bed_img, (65, 65))

# Carga de imagenes de enemigos
thunder_img = pygame.image.load("images/thunder.png")
thunder_img = pygame.transform.scale(thunder_img, (10, 20))

vacuum_img = pygame.image.load("images/vacuum.png")
vacuum_img = pygame.transform.scale(vacuum_img, (65, 65))

drone_img = pygame.image.load("images/dron.png")
drone_img = pygame.transform.scale(drone_img, (60, 60))

car_img = pygame.image.load("images/car.png")
car_img = pygame.transform.scale(car_img, (60, 60))

bike_img = pygame.image.load("images/bike.png")
bike_img = pygame.transform.scale(bike_img, (90, 80))

lawn_mower_img = pygame.image.load("images/lawn_mower.png")
lawn_mower_img = pygame.transform.scale(lawn_mower_img, (85, 75))

washing_machine_img = pygame.image.load("images/washing_machine.png")
washing_machine_img = pygame.transform.scale(washing_machine_img, (85, 75))

iron_img = pygame.image.load("images/iron.png")
iron_img = pygame.transform.scale(iron_img, (70, 70))

plane_img = pygame.image.load("images/plane.png")
plane_img = pygame.transform.scale(plane_img, (70, 70))

robot_img = pygame.image.load("images/robot.png")
robot_img = pygame.transform.scale(robot_img, (70, 70))

gameboy_img = pygame.image.load("images/gameboy.png")
gameboy_img = pygame.transform.scale(gameboy_img, (75, 75))

drill_img = pygame.image.load("images/drill.png")
drill_img = pygame.transform.scale(drill_img, (65, 65))

tv_img = pygame.image.load("images/tv.png")
tv_img = pygame.transform.scale(tv_img, (70, 70))

pc_img = pygame.image.load("images/pc.png")
pc_img = pygame.transform.scale(pc_img, (100, 100))

# Carga de imágenes de fondos para los niveles
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

level_8_bg = pygame.image.load("images/laundry_room.png")
level_8_bg = pygame.transform.scale(level_8_bg, (WIDTH, HEIGHT))

level_9_bg = pygame.image.load("images/childrens_room.png")
level_9_bg = pygame.transform.scale(level_9_bg, (WIDTH, HEIGHT))

level_10_bg = pygame.image.load("images/study_room.png")
level_10_bg = pygame.transform.scale(level_10_bg, (WIDTH, HEIGHT))

# Fondo pantalla inicial
start_screen_bg = pygame.image.load("images/pantalla_inicio.png") 
start_screen_bg = pygame.transform.scale(start_screen_bg, (WIDTH, HEIGHT))

# Fondo pantalla game over
game_over_bg = pygame.image.load("images/game_over_background.png")
game_over_bg = pygame.transform.scale(game_over_bg, (WIDTH, HEIGHT))

# Fondo pantalla final
end_screen_bg = pygame.image.load("images/pantalla_final.png")
end_screen_bg = pygame.transform.scale(end_screen_bg, (WIDTH, HEIGHT))

# Plataforma sprite
platform_texture = pygame.image.load("images/platform_texture.png")  
platform_texture = pygame.transform.scale(platform_texture, (100, 20))

# Variables globales
player_name = ""
current_level = 1
collision_count = 0
player_lives = 3
enemy_bullets = []  # Lista para almacenar los disparos activos
collected_objects = set() # Set para almacenar los objetos recogidos
all_sparks = [] # Lista global para almacenar los efectos de chispas

# Configuración del jugador
player = pygame.Rect(100, 500, 40, 40)
player_speed = 5
player_jump = -15
player_velocity_y = 0
on_ground = True
player_facing_right = True

# Contador para la animación de caminar
walk_timer = 0
walk_switch_time = 10  # Tiempo de espera antes de cambiar la imagen

# Función para reproducir cambios de música
def play_music(music_file, loop=True, volume=0.3):
    """Reproduce música desde el archivo especificado."""
    pygame.mixer.music.stop()  # Detiene la música actual
    pygame.mixer.music.load(music_file)  # Carga la nueva pista
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1 if loop else 0)  # Reproduce en bucle si loop=True

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
def create_enemy(x, y, image, platform):
    enemy = {
        "rect": pygame.Rect(x, y, 50, 50),
        "image": image,
        "platform": platform,
        "direction": random.choice([-1, 1]),  # Dirección inicial aleatoria
        "jumping": False,  # Comienza sin saltar
        "jump_velocity": 0,  # Velocidad del salto
        "jump_height": 10,  # Altura máxima del salto
        "jump_timer": random.randint(2, 5),  # Tiempo aleatorio para el salto
    }
    return enemy

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
        "object_position": (490, 369, 30, 30),
        "object_name": "comida" 
    },
    2: {
        "background": apply_background_effect(level_2_bg),
        "object": water_img,
        "enemies": [vacuum_img, tv_img],
        "message": "Has conseguido agua",
        "object_position": (600, 370, 30, 30),
        "object_name": "agua"
    },
    3: {
        "background": apply_background_effect(level_3_bg),
        "object": toy_img,
        "enemies": [car_img, vacuum_img, drone_img],
        "message": "Has conseguido el resorte",
        "object_position": (760, 160, 30, 30),
        "object_name": "resorte"
    },
    4: {
        "background": apply_background_effect(level_4_bg),
        "object": churu_img,
        "enemies": [drone_img, drill_img, car_img],
        "message": "Has conseguido churu",
        "object_position": (650, 150, 30, 30),
        "object_name": "churu"
    },
    5: {
        "background": apply_background_effect(level_5_bg),
        "object": grass_img,
        "enemies": [car_img, vacuum_img, drone_img],
        "message": "Has conseguido hierba",
        "object_position": (600, 250, 30, 30),
        "object_name": "hierba"
    },
    6: {
        "background": apply_background_effect(level_6_bg),
        "object": wool_img,
        "enemies": [bike_img, lawn_mower_img, drone_img, plane_img],
        "message": "Has conseguido ovillo",
        "object_position": (100, 160, 30, 30),
        "object_name": "ovillo"
    },
    7: {
        "background": apply_background_effect(level_7_bg),
        "object": mouse_img,
        "enemies": [tv_img, car_img, vacuum_img, drone_img],
        "message": "Has conseguido ratoncito",
        "object_position": (650, 160, 30, 30),
        "object_name": "ratoncito"
    },
    8: {
        "background": apply_background_effect(level_8_bg),
        "object": litter_img,
        "enemies": [iron_img, vacuum_img, washing_machine_img, drone_img],
        "message": "Has conseguido arenero",
        "object_position": (500, 160, 30, 30),
        "object_name": "arenero"
    },
    9: {
        "background": apply_background_effect(level_9_bg),
        "object": box_img,
        "enemies": [car_img, gameboy_img, robot_img, drone_img, plane_img],
        "message": "Has conseguido caja",
        "object_position": (780, 160, 30, 30),
        "object_name": "caja"
    },
    10: {
        "background": apply_background_effect(level_10_bg),
        "object": bed_img,
        "enemies": [vacuum_img, tv_img, pc_img, drone_img, plane_img],
        "message": "Has conseguido cama",
        "object_position": (210, 160, 30, 30),
        "object_name": "cama"
    }
}

# Plataformas
platforms_by_level = {
    1: [
        pygame.Rect(0, 700, 900, 20), # Plataforma inicial
        pygame.Rect(100, 600, 700, 20),
        pygame.Rect(250, 500, 350, 20),
        pygame.Rect(350, 400, 350, 20),
    ],
    2: [
        pygame.Rect(0, 700, 900, 20),  # Plataforma inicial 
        pygame.Rect(150, 600, 750, 20),
        pygame.Rect(150, 500, 700, 20),
        pygame.Rect(450, 400, 300, 20),
        pygame.Rect(50, 400, 300, 20),
    ],
    3: [
        pygame.Rect(0, 700, 900, 20),  # Plataforma inicial 
        pygame.Rect(150, 600, 650, 20),
        pygame.Rect(20, 500, 500, 20),
        pygame.Rect(600, 450, 200, 20),
        pygame.Rect(150, 400, 400, 20),
        pygame.Rect(600, 300, 300, 20),
        pygame.Rect(600, 200, 200, 20),
    ],
    4: [
        pygame.Rect(0, 700, 900, 20),  # Plataforma inicial 
        pygame.Rect(200, 600, 600, 20),
        pygame.Rect(50, 500, 750, 20),
        pygame.Rect(150, 400, 500, 20),
        pygame.Rect(500, 300, 200, 20),
        pygame.Rect(100, 300, 300, 20),
        pygame.Rect(600, 200, 100, 20),
    ],
    5: [
        pygame.Rect(0, 700, 800, 20),  # Plataforma inicial 
        pygame.Rect(200, 600, 600, 20),
        pygame.Rect(80, 500, 600, 20),
        pygame.Rect(150, 400, 250, 20),
        pygame.Rect(500, 400, 250, 20),
        pygame.Rect(500, 300, 250, 20),
    ],
    6: [
        pygame.Rect(20, 700, 850, 20),  # Plataforma inicial 
        pygame.Rect(20, 600, 400, 20),
        pygame.Rect(550, 600, 300, 20),
        pygame.Rect(200, 500, 700, 20),
        pygame.Rect(150, 400, 500, 20),
        pygame.Rect(250, 300, 200, 20),
        pygame.Rect(50, 200, 200, 20),
    ],
    7: [
        pygame.Rect(20, 700, 750, 20),  # Plataforma inicial 
        pygame.Rect(50, 600, 600, 20),
        pygame.Rect(0, 500, 400, 20),
        pygame.Rect(500, 500, 300, 20),
        pygame.Rect(150, 400, 350, 20),
        pygame.Rect(600, 400, 200, 20),
        pygame.Rect(400, 300, 150, 20),
        pygame.Rect(600, 200, 100, 20),
    ],
    8: [
        pygame.Rect(20, 700, 750, 20),  # Plataforma inicial 
        pygame.Rect(300, 600, 600, 20),
        pygame.Rect(0, 500, 400, 20),
        pygame.Rect(500, 500, 300, 20),
        pygame.Rect(100, 400, 450, 20),
        pygame.Rect(600, 400, 200, 20),
        pygame.Rect(200, 300, 200, 20),
        pygame.Rect(450, 200, 200, 20),
    ],
    9: [
        pygame.Rect(20, 700, 750, 20),  # Plataforma inicial 
        pygame.Rect(0, 600, 350, 20),
        pygame.Rect(550, 600, 350, 20),
        pygame.Rect(0, 500, 900, 20),
        pygame.Rect(50, 400, 300, 20),
        pygame.Rect(450, 400, 350, 20),
        pygame.Rect(350, 300, 300, 20),
        pygame.Rect(700, 200, 200, 20),
    ],
    10: [
        pygame.Rect(20, 700, 750, 20),  # Plataforma inicial 
        pygame.Rect(0, 600, 350, 20),
        pygame.Rect(550, 600, 350, 20),
        pygame.Rect(0, 500, 900, 20),
        pygame.Rect(50, 400, 300, 20),
        pygame.Rect(450, 400, 350, 20),
        pygame.Rect(400, 300, 200, 20),
        pygame.Rect(200, 200, 100, 20),
    ] 
}

# Clase para representar disparo de enemigos
class EnemyBullet:
    def __init__(self, x, y, thunder_img, speed=1):
        self.image = thunder_img  # Imagen del disparo
        self.rect = self.image.get_rect(center=(x, y)) 
        self.speed = speed  

    def move(self):
        self.rect.y += self.speed  # Mover 

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Amarillo

# Clase para representar una partícula
class Particle:
    def __init__(self, x, y, color, speed, lifespan):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.lifespan = lifespan
        self.size = 2
    
    def update(self):
        # Actualizamos la posición de la partícula para crear el efecto de dispersión
        self.x += random.randint(-self.speed, self.speed)
        self.y += random.randint(-self.speed, self.speed)
        self.lifespan -= 1  # Disminuir la vida útil de la partícula
    
    def draw(self, screen):
        # Dibujamos la partícula
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Clase que gestiona el efecto de chispas
class SparkEffect:
    def __init__(self, x, y):
        self.particles = []
        for _ in range(30):  # Generamos 30 partículas por colisión
            color = (255, random.randint(200, 255), 0)  # Color amarillo o blanco
            speed = random.randint(6, 12)  # Velocidad de dispersión
            lifespan = random.randint(20, 40)  # Duración de la partícula
            self.particles.append(Particle(x, y, color, speed, lifespan))
    
    def update(self):
        # Actualizamos las partículas y eliminamos las que ya han expirado
        for particle in self.particles[:]:
            particle.update()
            if particle.lifespan <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        # Dibujamos las partículas en la pantalla
        for particle in self.particles:
            particle.draw(screen)

# Lista ordenada de objetos por nivel
required_objects_order = ["comida", "agua", "resorte", "churu", "hierba", "ovillo", "ratoncito", "arenero", "caja", "cama"]

# Función para renderizar texto con fondo negro
def render_with_black_background(text, color, pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
        
    # Fondo negro detrás del texto 
    padding = 10  # Espaciado entre el texto y el fondo
    background_rect = pygame.Rect(text_rect.x - padding, text_rect.y - padding, text_rect.width + 2 * padding, text_rect.height + 2 * padding)        
    pygame.draw.rect(screen, BLACK, background_rect)  # Dibuja el fondo negro
    screen.blit(text_surface, text_rect)  # Dibuja el texto sobre el fondo negro

# Función que resetea el juego
def reset_game():
    global current_level, collected_objects, collision_count
    current_level = 1
    collected_objects.clear()
    collision_count = 0
    reset_level()  # Reiniciar el nivel actual
    display_start_screen()  # Mostrar pantalla inicial

# Función de cambio de niveles
def reset_level():
    global player, enemies, platforms
    player.topleft = (20, 700)
    player_x, player_y = player.topleft  # Coordenadas del gatito
    enemies.clear()

    global platforms  # Aseguramos que se actualicen las plataformas globales
    platforms = platforms_by_level.get(current_level, [])
    
    # Filtrar las plataformas ocupadas por el jugador
    available_platforms = [platform for platform in platforms if not player.colliderect(platform)]
    
    if current_level <= len(levels):
        enemy_images = levels[current_level]["enemies"]
        for i, platform in enumerate(available_platforms[:len(enemy_images)]):
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
        screen.blit(enemy["image"], enemy["rect"])

    # Usar la posición definida de los objetos a recoger
    object_position = levels[current_level]["object_position"]
    object_rect = pygame.Rect(object_position[0], object_position[1], 30, 30)
    screen.blit(levels[current_level]["object"], object_rect)
    return object_rect

# Función de movimiento de los enemigos
def move_enemies():
    enemy_speed = 2 + int(2 * (current_level - 1)**0.5)  # Velocidad con crecimiento lento
    for enemy in enemies:
        # Movimiento horizontal
        if enemy["platform"]:
            enemy["rect"].x += enemy["direction"] * enemy_speed
            if enemy["rect"].left <= enemy["platform"].left or enemy["rect"].right >= enemy["platform"].right:
                enemy["direction"] *= -1  # Cambiar dirección si toca el borde de la plataforma
            # Generar disparo aleatorio
            if random.randint(1, 500) <= 1:  # 5% de probabilidad de disparo
                new_bullet = EnemyBullet(
                    enemy["rect"].centerx, enemy["rect"].bottom, thunder_img
                )
                enemy_bullets.append(new_bullet)

            # Controlar el salto aleatorio
            if not enemy["jumping"]:
                # Activar el salto aleatorio con un pequeño porcentaje de probabilidad
                if random.random() < 0.01:  # 1% de probabilidad de salto en cada frame
                    enemy["jumping"] = True
                    enemy["jump_velocity"] = 5  # Inicializar la velocidad de salto hacia arriba
                    enemy["jump_timer"] = random.randint(2, 5)  # Asignar nuevo intervalo de salto aleatorio

            # Si el enemigo está saltando
            if enemy["jumping"]:
                # Movimiento de salto
                if enemy["jump_velocity"] > 0:  # Subiendo
                    enemy["rect"].y -= enemy["jump_velocity"]
                    enemy["jump_velocity"] -= 0.5  # Gravedad
                else:  # Bajando
                    enemy["rect"].y += 2  # Velocidad de caída
                    if enemy["rect"].bottom >= enemy["platform"].top:  # Aterrizando
                        enemy["rect"].bottom = enemy["platform"].top  # Aseguramos que el enemigo esté en la plataforma
                        enemy["jumping"] = False  # El enemigo deja de saltar
                        enemy["jump_velocity"] = 0  # Reseteamos la velocidad del salto

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
    
    # Mostrar el nivel actual
    level_text = font.render(f"Nivel {current_level}", True, BEIGE)  # Texto del nivel
    screen.blit(level_text, (WIDTH - level_text.get_width() -10, 10))  # Posición
    
    # Calcular y mostrar vidas en forma de corazones
    remaining_lives = 3 - collision_count  # Si collision_count es 1, mostrará 2 corazones, etc.
    # Dibujar los corazones en la parte superior de la pantalla
    for i in range(remaining_lives):
        screen.blit(heart_img, (WIDTH -(i + 1) * (heart_img.get_width() + 5), 35))  # Ajusta la posición

# Función pantalla Game Over
def display_game_over_screen():
    global render_with_black_background
    
    screen.blit(game_over_bg, (0, 0)) # Dibujar imagen de fondo
    
    play_music(game_over_music, volume=0.5)
    # Texto 
    render_with_black_background("¡Has perdido! La IA se interpuso en tu camino", WHITE, (WIDTH // 2, HEIGHT - 550))
    render_with_black_background("Presiona < Enter > para intentar de nuevo", WHITE, (WIDTH // 2, HEIGHT - 518))

    pygame.display.flip()

    # Esperar a que el jugador presione Enter para reiniciar
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Salir del juego con la tecla F1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
                reset_game()  # Reiniciar el juego

# Transición entre musicas
def transition_to_next_music(new_music_file, fade_duration=1000, volume=0.5):
    
    # Reproducir la música actual a un volumen bajo mientras cambia
    pygame.mixer.music.fadeout(fade_duration // 2)  # Baja gradualmente la música actual
    pygame.time.wait(fade_duration // 2)  # Espera a que termine el fadeout

    # Cargar y reproducir la nueva música
    pygame.mixer.music.load(new_music_file)  # Cargar la nueva música
    pygame.mixer.music.play(-1, 0.0)  # Reproducir en bucle (si es necesario)
    
    # Comenzamos con el volumen en 0
    pygame.mixer.music.set_volume(0)
    
    # Aumenta el volumen gradualmente
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    
    while pygame.time.get_ticks() - start_time < fade_duration:
        # Calcula el porcentaje de tiempo transcurrido
        elapsed_time = pygame.time.get_ticks() - start_time
        volume_level = (elapsed_time / fade_duration) * volume  # El volumen aumenta de 0 a 'volume'
        pygame.mixer.music.set_volume(volume_level)
        
        clock.tick(60)  # Controlar la velocidad de la transición
        
    # Asegurar que el volumen final sea el volumen deseado
    pygame.mixer.music.set_volume(volume)

    # Crea una pantalla negra que se desvanezca
    fade_surface = pygame.Surface((WIDTH, HEIGHT))  # Pantalla negra
    fade_surface.fill(BLACK)  # Llénala de color negro
    screen.blit(fade_surface, (0, 0))  # Dibujar la pantalla negra
    pygame.display.flip()  # Mostrar la pantalla negra

    # Hace que la pantalla negra se desvanezca 
    fade_alpha = 255  # Opacidad inicial

    while fade_alpha > 0:
        fade_alpha -= 5  # Reducir la opacidad
        fade_surface.set_alpha(fade_alpha)  # Ajustar la opacidad de la pantalla negra
        screen.blit(fade_surface, (0, 0))  # Dibujar la pantalla con opacidad
        pygame.display.flip()  # Actualizar la pantalla
        clock.tick(60)  # Controlar la velocidad de la transición


# Pantalla inicial
MAX_NAME_LENGTH = 15  # Define el límite de caracteres que puede tener el nombre

def display_start_screen():
    global player_name, error_message
    
    play_music(start_screen_music, volume=0.5)  # Reproduce la música de la pantalla inicial
    screen.blit(start_screen_bg, (0, 0))

    box_width = WIDTH - 300
    box_height = 250
    box_x = (WIDTH - box_width) // 2
    box_y = HEIGHT // 3
    pygame.draw.rect(screen, BEIGE, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

    title = font.render("¡BIENVENIDX A mIAu!", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, box_y + 30))

    prompt = font.render("Escribe el nombre de tu gatitx: ", True, BLACK)
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, box_y + 90))

    enter_message = font.render("Presiona < Enter > para comenzar", True, BLACK)
    screen.blit(enter_message, (WIDTH // 2 - enter_message.get_width() // 2, box_y + 190))

    screen.blit(logo_img, (5, 5))
    screen.blit(quit_img, (895, 765))
    screen.blit(controls_img, (5, 695))

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

            # Salir del juego con la tecla F1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name.strip() == "":
                        error_message = "No has ingresado el nombre de tu gatitx"
                    else:
                        name_entered = True
                        # Llamar a la transición antes de continuar con los niveles
                        transition_to_next_music(level_music, fade_duration=1000, volume=0.4)  # Transición de música
                        # Continuar con el juego...
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
    play_music(end_screen_music)  # Reproduce la música de la pantalla final
    screen.blit(end_screen_bg, (0, 0))
    final_sound.play()

    # Función para renderizar texto con fondo negro
    def render_with_beige_background(text, color, pos):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=pos)
        
        # Fondo negro detrás del texto 
        padding = 10  # Espaciado entre el texto y el fondo
        background_rect = pygame.Rect(text_rect.x - padding, text_rect.y - padding, text_rect.width + 2 * padding, text_rect.height + 2 * padding)
        pygame.draw.rect(screen, BEIGE, background_rect)  # Dibuja el fondo negro
        screen.blit(text_surface, text_rect)  # Dibuja el texto sobre el fondo negro

    # Llamadas a la función para los mensajes
    render_with_beige_background(f"¡Lo lograste! '{player_name}' ha superado todos los peligros.", BLACK, (WIDTH // 2, HEIGHT // 9))
    render_with_beige_background(f"Gracias a ti, ahora '{player_name}' puede disfrutar", BLACK, (WIDTH // 2, HEIGHT // 5))
    render_with_beige_background("de todos sus preciados objetos y descansar en paz.", BLACK, (WIDTH // 2, HEIGHT // 4))
    render_with_beige_background("* Presiona < Enter > para jugar de nuevo *", BLACK, (WIDTH // 2, HEIGHT - 200))

    # Dibujar el logo
    screen.blit(logo_img, (5, 650))
    # Indicador para salir del juego
    screen.blit(quit_img, (895, 765))

    # Dibujar los iconos 
    icon_x = WIDTH // 2 - 100  
    icon_y = HEIGHT - 200

    # Definir el espaciado entre los objetos y su radio de disposición circular
    spacing = 20
    object_width = 50  # Ancho de los objetos
    radius = 100  

    # Posiciones iniciales de los grupos
    left_group_center = (WIDTH // 4, HEIGHT // 2)  
    right_group_center = (3 * WIDTH // 4, HEIGHT // 2)  

    # Agrupar los objetos en dos grupos de 5
    left_objects = collected_objects[:5]  
    right_objects = collected_objects[5:10]  

    # Función para calcular la posición en un círculo
    def get_circle_position(center, index, total_objects, radius):
        angle = (index / total_objects) * (2 * math.pi)  # Ángulo de separación entre los objetos
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        return x, y

    # Dibujar objetos en el grupo izquierdo (en círculo)
    for i, obj in enumerate(left_objects):
        x, y = get_circle_position(left_group_center, i, len(left_objects), radius)
        screen.blit(obj, (x - object_width // 2, y - object_width // 2))  # Ajustar para centrar el objeto
        item_pickup_sound.set_volume(0.5)  # Ajustar el volumen al 50% 
        item_pickup_sound.play()  # Reproducir el sonido cuando se dibuja el objeto
        pygame.display.flip()  # Actualizar pantalla
        time.sleep(0.5)  # Retardo de 0.5 segundos entre cada objeto

    # Dibujar objetos en el grupo derecho (en círculo)
    for i, obj in enumerate(right_objects):
        x, y = get_circle_position(right_group_center, i, len(right_objects), radius)
        screen.blit(obj, (x - object_width // 2, y - object_width // 2))  
        item_pickup_sound.set_volume(0.5)  
        item_pickup_sound.play()  
        pygame.display.flip()  
        time.sleep(0.5)  

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Salir del juego con la tecla F1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
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
    elif level == 8:
        level_message = font.render("Has conseguido arenero", True, WHITE)
    elif level == 9:
        level_message = font.render("Has conseguido caja", True, WHITE)
    elif level == 10:
        level_message = font.render("Has conseguido cama", True, WHITE)

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

# Función para manejar efecto de colision
def handle_collision_with_effects(x, y):
    # Crear el efecto de chispas en la posición de la colisión
    spark_effect = SparkEffect(x, y)
    all_sparks.append(spark_effect)  # Agregar el efecto a la lista

# Función para manejar las vidas del jugador (enemigos o caidas)
def handle_collision():
    global collision_count

    collision_count += 1  # Incrementa el contador de colisiones o vidas perdidas

    if collision_count > 3:  # Límite de vidas
        game_over_sound.play()
        render_with_black_background("GAME OVER", WHITE, (WIDTH // 2, HEIGHT // 2))
        display_ui()
        pygame.display.flip()
        pygame.time.wait(2000)  # Pausa de 2 segundos
        display_game_over_screen()
    else:
        reset_level()  # Resetear el nivel actual

# Bucle principal
collected_objects = []  # Cambiar de set() a lista vacía
def main():
    global current_level, player_velocity_y, on_ground, player_facing_right, cat_img, last_move_time

    clock = pygame.time.Clock()
    running = True

    screen.blit(start_screen_bg, (0, 0))
    display_start_screen()
    reset_level()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Salir del juego con la tecla F1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Si el gato se cae de la pantalla (fuera de los límites)
        if player.y > HEIGHT:  # Si el gato se sale por la parte inferior
            falls_sound.play()
            handle_collision()  # Manejar colisión por caída
            player_velocity_y = 0  # Detener la velocidad de caída

        # Movimiento del jugador
        player_velocity_y += 1  # Gravedad
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
            player_facing_right = False
            if pygame.time.get_ticks() - last_move_time > movement_interval:
                cat_img = cat_img_1 if cat_img == cat_img_2 else cat_img_2
                last_move_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            player.x += player_speed
            player_facing_right = True
            if pygame.time.get_ticks() - last_move_time > movement_interval:
                cat_img = cat_img_1 if cat_img == cat_img_2 else cat_img_2
                last_move_time = pygame.time.get_ticks()
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
                handle_collision_with_effects(player.centerx, player.centery)  # Crear el efecto de chispas
                handle_collision()  # Manejar colisión con enemigo

        # Actualizar y dibujar los efectos de chispas
        for spark in all_sparks[:]:
            spark.update()  # Actualizar partículas
            spark.draw(screen)  # Dibujar partículas en pantalla

        if player.colliderect(object_rect):
            if levels[current_level]["object"] not in collected_objects:
                item_pickup_sound.play()  # Reproduce el sonido al recoger el objeto
                collected_objects.append(levels[current_level]["object"])  # Añadir el objeto al inventario
                
                display_level_transition(current_level)  # Mostrar la pantalla de transición
                current_level += 1  # Pasar al siguiente nivel

                if current_level > len(levels):
                    display_end_screen()  # Mostrar la pantalla final
                    reset_game()
                else:
                    reset_level()  # Reiniciar el nuevo nivel

        for bullet in enemy_bullets[:]:
            bullet.move()
            bullet.draw(screen)

            # Verificar colisión con el jugador
            if player.colliderect(bullet.rect):
                handle_collision_with_effects(bullet.rect.x, bullet.rect.y)  # Efecto de colisión
                enemy_hit_sound.play()
                handle_collision()  # Reducir vidas del jugador
                enemy_bullets.remove(bullet)  # Eliminar el disparo tras la colisión

            # Eliminar disparos fuera de la pantalla
            if bullet.rect.top > HEIGHT:
                enemy_bullets.remove(bullet)


        display_ui()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
