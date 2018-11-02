#!/usr/bin/env python3
import pyglet;

# hna drna loading lel image ta3 sprite
def preload_image( image: str ):

    my_img = pyglet.image.load( "resource/sprites/" + image );

    return my_img;


# hadi l class khass bel objects ta3 gameplay ta3na ay biha ndifniw pos w image
class GameObject( object ):

    # drna initialize func, w 3tinaha pos w image
    def __init__( self, posX, posY, sprite = None, batch = None, image = None ):

        self.posX: int = posX;
        self.posY: int = posY;

        self.batch = batch;
        self.image = image;

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

        self.objectSprite.x = self.posX;
        self.objectSprite.y = self.posY;


