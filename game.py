import pygame
import numpy as np
from state import GameState


class Game:

    def __init__(self, q_table, dim=400):
        self.q_table = q_table
        self.state = GameState()
        self.dim = dim
        self.section = dim / 3
        self.line_color = (30, 30, 30)
        self.line_width = 10
        self.screen = pygame.display.set_mode((self.dim, self.dim))

    def start(self):
        pygame.init()
        self.draw_board()

        while 1:
            self.q_table_move()
            self.draw()
            if self.state.get_winner() is not None: return

            self.user_move()
            self.draw()
            if self.state.get_winner() is not None: return

    def q_table_move(self):
        cell_idx = np.argmax(self.q_table[self.state])
        print(self.state.board)
        print(cell_idx)
        x = cell_idx % 3
        y = cell_idx / 3
        self.state.board[x][y] = self.state.turn
        print(self.state.board)
        print ("")
        self.state.switch_turn()

    def user_move(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_state_with_mouse()
                    done = True

    def update_state_with_mouse(self):
        (x, y) = pygame.mouse.get_pos()
        cell_x = x / self.section
        cell_y = y / self.section
        self.state.board[cell_x][cell_y] = self.state.turn
        self.state.switch_turn()

    def draw(self):
        cross_cols, cross_rows = np.where(self.state.board == 1)
        circle_cols, circle_rows = np.where(self.state.board == -1)

        for i in range(len(cross_cols)):
            self.draw_cross(cross_cols[i], cross_rows[i])

        for i in range(len(circle_cols)):
            self.draw_circle(circle_cols[i], circle_rows[i])
        pygame.display.flip()

    def draw_circle(self, cell_x, cell_y):
        pygame.draw.circle(self.screen, self.line_color,
                           (cell_x * self.section + self.section / 2, cell_y * self.section + self.section / 2),
                           self.section / 3, self.line_width)

    def draw_cross(self, cell_x, cell_y):
        base_x = cell_x * self.section
        base_y = cell_y * self.section
        line_start = self.section / 4
        line_end = self.section * 3 / 4
        pygame.draw.line(self.screen, self.line_color, (base_x + line_start, base_y + line_start),
                         (base_x + line_end, base_y + line_end), 10)
        pygame.draw.line(self.screen, self.line_color, (base_x + line_end, base_y + line_start),
                         (base_x + line_start, base_y + line_end), 10)

    def draw_element(self, turn):
        (x, y) = pygame.mouse.get_pos()
        cell_x = x / self.section
        cell_y = y / self.section
        if turn:
            self.draw_circle(cell_x, cell_y)
        else:
            self.draw_cross(cell_x, cell_y)

    def draw_board(self):
        background_color = (200, 180, 200)
        pygame.draw.rect(self.screen, background_color, (0, 0, self.dim, self.dim))

        pygame.draw.line(self.screen, self.line_color, (self.section, 0), (self.section, self.dim), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (2 * self.section, 0), (2 * self.section, self.dim),
                         self.line_width)
        pygame.draw.line(self.screen, self.line_color, (0, self.section), (self.dim, self.section), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (0, 2 * self.section), (self.dim, 2 * self.section),
                         self.line_width)
