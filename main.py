import arcade
import random
from dataclasses import dataclass  # ligne 1 à 3 import librairie
# ligne 5 à 25 déclaration des variable
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.PINK, arcade.color.PURPLE,
          arcade.color.BLUE, arcade.color.GREEN,
          arcade.color.RED]


@dataclass
class Cercle:
    centre_x: int
    centre_y: int
    rayon: int
    color: (int, int, int)

    def draw(self):
        arcade.draw_circle_filled(self.centre_x,
                                  self.centre_y,
                                  self.rayon,
                                  self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice arcade #1")
        self.liste_cercles = []

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            distance = (cercle.centre_x - x) ** 2 + (cercle.centre_y - y) ** 2
            if distance <= cercle.rayon ** 2:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.liste_cercles.remove(cercle)
                elif button == arcade.MOUSE_BUTTON_RIGHT:
                    cercle.color = random.choice(COLORS)

    def setup(self):

        for _ in range(20):
            rayon = random.randint(10, 50)
            centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            couleur = random.choice(COLORS)
            self.liste_cercles.append(Cercle(centre_x, centre_y, rayon, couleur))

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
