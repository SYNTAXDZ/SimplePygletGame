#!usr/bin/env python3
import pyglet;
from gameObjects import preload_image;
from random import randint;


class GameAnim(object):

    # collided: bool = False;

    def __init__(self, pos_x: int, pos_y: int, image: str, batch=None) -> None:

        self.pos_x: int = pos_x;
        self.pos_y: int = pos_y;
        self.image: str = image;
        self.batch = batch;
        self.object_sprite = None;


    def animate(self, rows_n, columns_n, width, height):

        POS_Y: int = 700;

        object_image = preload_image(self.image);

        object_sequence = pyglet.image.ImageGrid(object_image, rows_n, columns_n, width, height);

        object_anim = pyglet.image.Animation.from_image_sequence(object_sequence[0:], .1, True);

        self.object_sprite = pyglet.sprite.Sprite(object_anim, x=0, y=0, batch=self.batch);
        self.object_sprite.position = (randint(2, 720), POS_Y);


    def destroy(self):

        self.object_sprite.delete();


    def collided(self, other) -> bool:

        if self.object_sprite.x >= other.posX and self.object_sprite.x <= other.posX + other.width or self.object_sprite.x + self.object_sprite.width >= other.posX and self.object_sprite.x <= other.posX + other.width:

            if self.object_sprite.y > other.posY and self.object_sprite.y < other.posY + other.height or self.object_sprite.y + self.object_sprite.height <= other.posY:

                return True;


    def update(self, _y):

        if self.object_sprite != None:
            self.object_sprite.y -= _y;
