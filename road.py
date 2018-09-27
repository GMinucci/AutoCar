import pygame
from map_file import map_draw


class Road(object):

    move_counter = 0
    mouse_map = []

    def __init__(self, screen_width=640, screen_height=480, tunnel_width=150,
        with_mouse=False, drawing=False):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.mouse_map = [320] * screen_height
        self.tunnel_width = tunnel_width
        self.with_mouse = with_mouse
        self.drawing = drawing

    def move_map(self, pos):
        if self.with_mouse:
            self.mouse_move_map(pos)
        else:
            self.move_counter += 1

    def mouse_move_map(self, pos):
        if not self.drawing:
            self.mouse_map.pop(0)
        self.mouse_map.append(pos)

    def draw(self, display):
        if self.with_mouse:
            self.mouse_draw(display)
        else:
            for y in range(self.screen_height):
                cur_pos = self.move_counter + y
                if cur_pos > 0 and cur_pos < len(map_draw):
                    middle = map_draw[cur_pos]
                    pygame.draw.rect(display, (255, 255, 255), (0, y, middle - self.tunnel_width/2, 1))
                    pygame.draw.rect(display, (255, 255, 255), (middle + self.tunnel_width/2, y, self.screen_width, 1))
                if cur_pos >= len(map_draw):
                    pygame.draw.rect(display, (255, 255, 255), (0, y, self.screen_width, 1))

    def mouse_draw(self, display):
        for y in reversed(range(self.screen_height)):
            middle = self.mouse_map[len(self.mouse_map) - y - 1]
            pygame.draw.rect(display, (255, 255, 255), (0, y, middle - self.tunnel_width/2, 1))
            pygame.draw.rect(display, (255, 255, 255), (middle + self.tunnel_width/2, y, self.screen_width, 1))

    def snap_map(self, y_pos):
        if self.with_mouse:
            return self.mouse_snap_map(y_pos)
        else:
            delta_pos = self.move_counter + y_pos
            if delta_pos > 0 and delta_pos < len(map_draw):
                middle = map_draw[delta_pos]
                return [
                    pygame.Rect(0, y_pos, middle - self.tunnel_width/2, 1),
                    pygame.Rect(middle + self.tunnel_width/2, y_pos, self.screen_width/2, 1)
                ]
            if delta_pos >= len(map_draw):
                pygame.Rect(0, y_pos, self.screen_width, 1)

    def mouse_snap_map(self, y_pos):
        middle = self.mouse_map[y_pos]
        return [
            pygame.Rect(0, y_pos, middle - self.tunnel_width/2, 1),
            pygame.Rect(middle + self.tunnel_width/2, y_pos, self.screen_width/2, 1)
        ]
