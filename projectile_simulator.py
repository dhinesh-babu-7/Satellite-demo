import math
import pygame

# --------------------------------
# WINDOW SETTINGS
# --------------------------------

WIDTH = 1000
HEIGHT = 650

FPS = 60

ground_y = 550

# --------------------------------
# PHYSICS
# --------------------------------

g = 9.81

# --------------------------------
# USER INPUT
# --------------------------------

v0 = float(input("Enter Your Initial Velocity: "))
angle_deg = float(input("Enter The Launching angle: "))

angle_rad = math.radians(angle_deg)

# --------------------------------
# INITIAL VELOCITY COMPONENTS
# --------------------------------

vx = v0 * math.cos(angle_rad)
vy = v0 * math.sin(angle_rad)

# --------------------------------
# PYGAME SETUP
# --------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("2D Projectile Simulator")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)
big_font = pygame.font.SysFont("Arial", 28)

# --------------------------------
# SIMULATION VARIABLES
# --------------------------------

x = 0
y = 0

time = 0

trajectory = []

running = True
paused = False
finished = False

scale = 5

max_height = 0

# --------------------------------
# MAIN LOOP
# --------------------------------

while running:

    # --------------------------------
    # EVENTS
    # --------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Pause / Resume
            if event.key == pygame.K_SPACE:
                paused = not paused

            # Restart
            if event.key == pygame.K_r:

                x = 0
                y = 0
                time = 0

                trajectory = []

                vx = v0 * math.cos(angle_rad)
                vy = v0 * math.sin(angle_rad)

                max_height = 0

                finished = False

    # --------------------------------
    # PHYSICS
    # --------------------------------

    if not paused and not finished:

        dt = 1 / FPS

        # Gravity
        ay = -g

        # Update vertical velocity
        vy += ay * dt

        # Update position
        x += vx * dt
        y += vy * dt

        # Update time
        time += dt

        # Store trajectory
        trajectory.append((x, y))

        # Maximum height
        if y > max_height:
            max_height = y

        # Landing
        if y < 0:

            y = 0
            finished = True

    # --------------------------------
    # DRAW BACKGROUND
    # --------------------------------

    screen.fill((20, 25, 35))

    # --------------------------------
    # DRAW GROUND
    # --------------------------------

    pygame.draw.line(
        screen,
        (100, 100, 100),
        (0, ground_y),
        (WIDTH, ground_y),
        3
    )

    # --------------------------------
    # DRAW TRAJECTORY
    # --------------------------------

    for point in trajectory:

        px = int(point[0] * scale)

        py = int(
            ground_y - (point[1] * scale)
        )

        if 0 <= px < WIDTH and 0 <= py < HEIGHT:

            pygame.draw.circle(
                screen,
                (100, 180, 255),
                (px, py),
                2
            )

    # --------------------------------
    # PROJECTILE POSITION
    # --------------------------------

    projectile_x = int(x * scale)

    projectile_y = int(
        ground_y - (y * scale)
    )

    # --------------------------------
    # DRAW PROJECTILE
    # --------------------------------

    if (
        0 <= projectile_x < WIDTH
        and
        0 <= projectile_y < HEIGHT
    ):

        pygame.draw.circle(
            screen,
            (100, 180, 255),
            (projectile_x, projectile_y),
            10
        )

    # --------------------------------
    # SPEED
    # --------------------------------

    speed = math.sqrt(
        vx**2 + vy**2
    )

    # --------------------------------
    # INFORMATION
    # --------------------------------

    info = [

        f"Time: {time:.2f} s",

        f"Position X: {x:.2f} m",

        f"Position Y: {y:.2f} m",

        f"Velocity X: {vx:.2f} m/s",

        f"Velocity Y: {vy:.2f} m/s",

        f"Speed: {speed:.2f} m/s",

        f"Acceleration Y: {-g:.2f} m/s²",

        f"Maximum Height: {max_height:.2f} m",

    ]

    # --------------------------------
    # DRAW INFORMATION
    # --------------------------------

    for i, text in enumerate(info):

        surface = font.render(
            text,
            True,
            (230, 230, 230)
        )

        screen.blit(
            surface,
            (20, 20 + i * 25)
        )

    # --------------------------------
    # TITLE
    # --------------------------------

    title = big_font.render(
        "2D Projectile Simulator",
        True,
        (255, 255, 255)
    )

    screen.blit(
        title,
        (WIDTH - 360, 20)
    )

    # --------------------------------
    # PAUSE / FINISHED MESSAGE
    # --------------------------------

    if paused:

        pause_text = big_font.render(
            "PAUSED",
            True,
            (255, 255, 255)
        )

        screen.blit(
            pause_text,
            (WIDTH // 2 - 50, 50)
        )

    if finished:

        finished_text = big_font.render(
            "LANDED",
            True,
            (255, 255, 255)
        )

        screen.blit(
            finished_text,
            (WIDTH // 2 - 50, 50)
        )

    # --------------------------------
    # UPDATE SCREEN
    # --------------------------------

    pygame.display.flip()

    # --------------------------------
    # FPS
    # --------------------------------

    clock.tick(FPS)

# --------------------------------
# QUIT
# --------------------------------

pygame.quit()