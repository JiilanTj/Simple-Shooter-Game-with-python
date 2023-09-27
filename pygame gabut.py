import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Tembak-Tembakan")

# Pemain
player = pygame.image.load("player.png")
player_rect = player.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.bottom = SCREEN_HEIGHT - 10
player_speed = 5

# Peluru
bullet = pygame.image.load("bullet.png")
bullet_rect = bullet.get_rect()
bullet_speed = 10
bullet_state = "ready"

# Musuh
enemies = []
enemy_speed = 3
enemy_spawn_timer = 100

# Skor
score = 0
font = pygame.font.Font(None, 36)

# Fungsi untuk menampilkan skor
def show_score():
    text = font.render("Skor: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

# Fungsi untuk menggambar pemain
def draw_player():
    screen.blit(player, player_rect)

# Fungsi untuk menggambar peluru
def draw_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))

# Fungsi untuk menggambar musuh
def draw_enemy(x, y):
    screen.blit(enemy, (x, y))

# Fungsi untuk mengecek tabrakan antara peluru dan musuh
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:
        return True
    return False

# Memuat gambar musuh
enemy = pygame.image.load("enemy.png")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Menggerakkan pemain
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_rect.x += player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_rect.centerx
                bullet_y = player_rect.y
                draw_bullet(bullet_x, bullet_y)

    # Hapus layar
    screen.fill((0, 0, 0))

    # Membuat musuh
    if enemy_spawn_timer <= 0:
        enemy_x = random.randint(0, SCREEN_WIDTH - 64)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])
        enemy_spawn_timer = 100

    # Menggambar musuh
    for enemy_coords in enemies:
        draw_enemy(enemy_coords[0], enemy_coords[1])
        enemy_coords[1] += enemy_speed

    # Menggambar pemain
    draw_player()

    # Mengecek tabrakan peluru dengan musuh
    for enemy_coords in enemies:
        if is_collision(enemy_coords[0], enemy_coords[1], bullet_x, bullet_y):
            score += 1
            bullet_state = "ready"
            bullet_y = player_rect.y
            enemy_coords[0] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_coords[1] = 0

        if enemy_coords[1] >= SCREEN_HEIGHT:
            enemies.remove(enemy_coords)

    # Mengecek tabrakan musuh dengan pemain
    for enemy_coords in enemies:
        if enemy_coords[1] >= player_rect.y:
            running = False

    # Menggambar peluru
    if bullet_state == "fire":
        draw_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed

    # Mengupdate skor
    show_score()

    # Mengupdate layar
    pygame.display.update()

    # Mengurangi timer spawn musuh
    enemy_spawn_timer -= 1

# Menutup Pygame
pygame.quit()
