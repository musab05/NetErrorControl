import pygame
import random
import time
from queue import Queue
from heapq import heappop, heappush

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30  # Grid size
TILE_SIZE = WIDTH // COLS
SCREEN = pygame.display.set_mode((WIDTH + 200, HEIGHT))  # Extra space for stats and buttons

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Fonts
FONT = pygame.font.SysFont('Arial', 20)

# Pathfinding algorithms
def bfs(grid, start, end):
    queue = Queue()
    queue.put((start, [start]))
    visited = set([start])

    while not queue.empty():
        (x, y), path = queue.get()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.put(((nx, ny), path + [(nx, ny)]))

    return []

def dfs(grid, start, end):
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    return []

def a_star(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    pq = []
    heappush(pq, (0, start, [start]))
    g_costs = {start: 0}
    visited = set()

    while pq:
        _, (x, y), path = heappop(pq)

        if (x, y) == end:
            return path

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_cost = g_costs[(x, y)] + 1
                if (nx, ny) not in g_costs or new_cost < g_costs[(nx, ny)]:
                    g_costs[(nx, ny)] = new_cost
                    heappush(pq, (new_cost + heuristic((nx, ny), end), (nx, ny), path + [(nx, ny)]))

    return []

# Maze generation
def create_maze():
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < 0.2:  # Random walls
                grid[i][j] = 1
    return grid

# Drawing functions
def draw_grid(grid, start, end, path=None, player=None):
    SCREEN.fill(WHITE)

    for i in range(ROWS):
        for j in range(COLS):
            color = WHITE
            if grid[i][j] == 1:
                color = BLACK
            elif (i, j) == start:
                color = RED  # Source in red
            elif (i, j) == end:
                color = BLUE  # Destination in blue
            pygame.draw.rect(SCREEN, color, (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    if path:
        for (x, y) in path:
            pygame.draw.rect(SCREEN, GREEN, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Path in green

    if player:
        pygame.draw.rect(SCREEN, GREEN, (player[0] * TILE_SIZE, player[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Player moving

    # Draw grid lines
    for i in range(ROWS + 1):
        pygame.draw.line(SCREEN, BLACK, (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))
    for j in range(COLS + 1):
        pygame.draw.line(SCREEN, BLACK, (0, j * TILE_SIZE), (WIDTH, j * TILE_SIZE))

def display_stats(distance, time_elapsed):
    pygame.draw.rect(SCREEN, WHITE, (WIDTH, 0, 200, HEIGHT))
    stats_text = FONT.render(f"Distance: {distance}", True, BLACK)
    time_text = FONT.render(f"Time: {time_elapsed:.2f}s", True, BLACK)
    SCREEN.blit(stats_text, (WIDTH + 20, 50))
    SCREEN.blit(time_text, (WIDTH + 20, 100))

def draw_button(x, y, w, h, text, color, action=None):
    pygame.draw.rect(SCREEN, color, (x, y, w, h))
    text_surface = FONT.render(text, True, BLACK)
    SCREEN.blit(text_surface, (x + 10, y + 10))

# Main loop
def main():
    clock = pygame.time.Clock()
    grid = create_maze()

    start = (0, 0)
    end = (COLS - 1, ROWS - 1)
    path = []

    running = True
    selected_algorithm = bfs
    start_time = 0
    distance = 0
    player = start
    step_index = 0  # For step-by-step movement

    while running:
        clock.tick(10)  # Set speed of movement

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if WIDTH <= mouse_x <= WIDTH + 200:
                    if 150 <= mouse_y <= 200:
                        selected_algorithm = bfs
                    elif 250 <= mouse_y <= 300:
                        selected_algorithm = dfs
                    elif 350 <= mouse_y <= 400:
                        selected_algorithm = a_star
                else:
                    grid_x, grid_y = mouse_x // TILE_SIZE, mouse_y // TILE_SIZE
                    if 0 <= grid_x < COLS and 0 <= grid_y < ROWS:
                        end = (grid_x, grid_y)
                        start_time = time.time()
                        path = selected_algorithm(grid, start, end)
                        distance = len(path)
                        player = start
                        step_index = 0

        time_elapsed = time.time() - start_time if path else 0

        if path and step_index < len(path):  # Move step-by-step along the path
            player = path[step_index]
            step_index += 1

        draw_grid(grid, start, end, path, player)
        display_stats(step_index, time_elapsed)

        # Draw buttons for algorithm selection
        draw_button(WIDTH + 20, 150, 160, 50, "BFS", GRAY if selected_algorithm == bfs else DARK_GRAY)
        draw_button(WIDTH + 20, 250, 160, 50, "DFS", GRAY if selected_algorithm == dfs else DARK_GRAY)
        draw_button(WIDTH + 20, 350, 160, 50, "A*", GRAY if selected_algorithm == a_star else DARK_GRAY)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
