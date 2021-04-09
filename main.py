# se code est créé par philippe johnston
# se code est créé 11-03-2021
# se code a pour fonction le dévlopement des fonction de la librérie arcade

import arcade
import random
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLORS = [arcade.color.PINK, arcade.color.PURPLE,
          arcade.color.BLUE, arcade.color.GREEN,
          arcade.color.RED, arcade.color.AIR_FORCE_BLUE, arcade.color.BEIGE, arcade.color.WINE, arcade.color.BUBBLES]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    color: (int, int, int)
    change_x: float
    change_y: float

    def draw(self):
        arcade.draw_circle_filled(self.centre_x,
                                  self.centre_y,
                                  self.rayon,
                                  self.color)

    def update(self):

        if self.centre_x >= SCREEN_WIDTH-self.rayon:
            if self.centre_x >= SCREEN_WIDTH-self.rayon+3:
                self.centre_x = SCREEN_WIDTH-self.rayon-1
            else:
                self.change_x = self.change_x * -1
                self.color = random.choice(COLORS)

        if self.centre_x <= self.rayon:
            self.change_x = self.change_x * -1
            self.color = random.choice(COLORS)

        self.centre_x += self.change_x

        if self.centre_y >= SCREEN_HEIGHT-self.rayon:
            if self.centre_y >= SCREEN_HEIGHT - self.rayon + 3:
                self.centre_y = SCREEN_HEIGHT - self.rayon-1
            else:
                self.change_y = self.change_y * -1

        if self.centre_y <= 0+self.rayon:
            self.change_y *= -1
            self.color = random.choice(COLORS)

        self.centre_y += self.change_y


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1", resizable=True)
        self.liste_cercles = []

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            distance = (cercle.centre_x - x) ** 2 + (cercle.centre_y - y) ** 2
            if distance <= cercle.rayon ** 2:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.liste_cercles.remove(cercle)
                elif button == arcade.MOUSE_BUTTON_RIGHT:
                    cercle.color = random.choice(COLORS)
                elif button == arcade.MOUSE_BUTTON_MIDDLE:
                    Cercle.change_x = random.randint(-3, 3)
                    cercle.change_y = random.randint(-3, 3)

    def setup(self):

        for _ in range(20):
            rayon = random.randint(10, 50)
            centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            couleur = random.choice(COLORS)
            change_x = random.randint(-3, 3)
            change_y = random.randint(-3, 3)
            self.liste_cercles.append(Cercle(centre_x, centre_y, rayon, couleur, change_x, change_y))

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercles:
            cercle.update()

    def on_resize(self, width: float, height: float):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        super().on_resize(width, height)
        SCREEN_WIDTH = width
        SCREEN_HEIGHT = height


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
