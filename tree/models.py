import pygame
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
OBJECT_SIZE = 50
PLAYER = pygame.Surface((50, 50), pygame.SRCALPHA)
OBJECT = pygame.Surface((50, 50), pygame.SRCALPHA)
BG_COLOR = (255, 255, 255)
FPS = 60


class Tree:
    def __init__(self, x, y, is_target):
        self.x = x
        self.y = y
        self.is_target = is_target
        self.rect = pygame.Rect(x, y, OBJECT_SIZE, OBJECT_SIZE)
        self.ready_to_click = False

    def draw(self, window):
        pygame.draw.rect(window, (0, 128, 0) if self.is_target else (139, 69, 19), self.rect)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.direction = 1

    def move(self, min_x, max_x):
        self.x += self.direction
        if self.x > max_x:
            self.direction = -1
        elif self.x < min_x:
            self.direction = 1
        self.rect.x = self.x

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 255), self.rect)


def start_the_game():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    player = Player(WINDOW_WIDTH // 2 - PLAYER_SIZE // 2, WINDOW_HEIGHT - PLAYER_SIZE - 10)
    trees = [Tree(i * OBJECT_SIZE, (WINDOW_HEIGHT - OBJECT_SIZE) // 2, random.choice([True, False]))
             for i in range(WINDOW_WIDTH // OBJECT_SIZE)]
    score = 0
    trees_fertilized = 0
    run = True
    font = pygame.font.Font(None, 36)
    final_score_text = None

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for tree in trees:
                    if tree.rect.collidepoint((x, y)) and tree.ready_to_click:
                        trees.remove(tree)
                        score += 4 if tree.is_target else 1
                        trees_fertilized += 1

        if trees_fertilized >= 20:
            run = False
            final_score_text = font.render('Ваш счет: ' + str(score * 120), 1, (0, 0, 0))

        window.fill(BG_COLOR)
        text = font.render(f'Счет: {score}', 1, (0, 0, 0))
        window.blit(text, (10, 10))

        player.move(0, WINDOW_WIDTH - PLAYER_SIZE)
        player.draw(window)

        for tree in trees:
            if player.rect.colliderect(tree.rect):
                tree.ready_to_click = True
                pygame.time.wait(1000)  # ждем секунду
                if tree in trees:  # проверяем все еще ли дерево в списке
                    tree.ready_to_click = False
            tree.draw(window)
        pygame.display.update()

    window.blit(final_score_text, (WINDOW_WIDTH // 2 - final_score_text.get_width() // 2, WINDOW_HEIGHT // 2))
    pygame.display.flip()

    time.sleep(5)
    pygame.quit()


if __name__ == "__main__":
    start_the_game()