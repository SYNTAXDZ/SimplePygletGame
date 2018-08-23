#!usr/bin/env python3
import pyglet;
from gameObjects import preload_image;
from random import random, randint, randrange;



class GameAnim:

    collided: bool = False;

    def __init__( self, pos_x, pos_y, image, batch = None ):

        self.pos_x: int = pos_x;
        self.pos_y: int = pos_y;
        self.image: str = image;
        self.batch = batch;
        self.object_sprite = None;
        #self.collided: bool = False;


    def animate( self, rows_n, columns_n, width, height ):

        object_image = preload_image( self.image );

        object_sequnce = pyglet.image.ImageGrid( object_image, rows_n, columns_n, width, height );

        object_anim = pyglet.image.Animation.from_image_sequence( object_sequnce[0:], .1, True );

        self.object_sprite = pyglet.sprite.Sprite( object_anim, x = self.pos_x, y = self.pos_y, batch = self.batch );
        self.object_sprite.position = ( randint( 2, 720 ), self.pos_y );



    def destroy( self ):

        self.object_sprite.delete();


    def collision( self, other ) -> bool:

        global collided;

        if self.object_sprite.x >= other.posX and self.object_sprite.x <= other.posX + other.width or self.object_sprite.x + self.object_sprite.width >= other.posX and self.object_sprite.x <= other.posX + other.width:

            if self.object_sprite.y > other.posY and self.object_sprite.y < other.posY + other.height or self.object_sprite.y + self.object_sprite.height <= other.posY:

                collided = True;

                return collided;


    def update( self, _y ):

        if self.object_sprite != None:
            #_x = self.pos_x;
            #self.object_sprite.x = _x;
            self.object_sprite.y -= _y;
        else:
            print( "sprite isn't updated!!" );




