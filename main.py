import arcade
import random


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)




def main():

    window = MyGame(640, 480, "Drawing Example")
# def on_draw(self):
    liste_couleur = [arcade.color.BLUE, arcade.color.RED, arcade.color.GREEN]
    arcade.start_render()
    i = 0
    while i < 20:
        couleur = random.choice(liste_couleur)
        rayon = random.randint(1, 20)
        cordone_x = random.randint(0+rayon, 640-rayon)
        cordone_y = random.randint(0+rayon, 480-rayon)
        arcade.draw_circle_filled(cordone_x, cordone_y, rayon, couleur)
        i += 1

    arcade.run()


main()
