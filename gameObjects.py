#!/usr/bin/env python3
import pyglet;
#from gameAnim import GameAnim;

# hna drna loading lel image ta3 sprite
def preload_image( image ):

    my_img = pyglet.image.load( "resource/sprites/" + image );

    return my_img;


# hadi l class khass bel objects ta3 gameplay ta3na ay biha ndifniw pos w image
class GameObject:

    # drna initialize func, w 3tinaha pos w image
    def __init__( self, posX, posY, sprite = None, batch = None, image = None ):

        self.posX = posX;
        self.posY = posY;
        self.batch = batch;
        self.image = image;

        self.velocity = [ 0, 0 ];

        # ki ta3ti image
        if sprite != None:

            # w criyina sprite object bach ndiroulah draw f screen
            self.objectSprite = sprite;
            # pos tal sprite drnaha hiya ta3 l object
            self.objectSprite.x = self.posX;
            self.objectSprite.y = self.posY;

            self.width = self.objectSprite.width;
            self.height = self.objectSprite.height;


    def draw( self ):

        self.objectSprite.draw();


    # hadi l func dir update lel gameObject
    def update( self ):

        # x ta3 gameObjct zidalha velocity * deltaTime
        #self.posX += self.velocity[0] * dt;
        #self.posY += self.velocity[1] * dt;

        self.objectSprite.x = self.posX;
        self.objectSprite.y = self.posY;

