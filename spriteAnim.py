import pyglet;
from pyglet.window import FPSDisplay, key;
from random import randint;


class GameWindow( pyglet.window.Window ):

    def __init__( self, *args, **kwargs ):

        super( GameWindow, self ).__init__( *args, **kwargs );

        self.set_location( 500, 0 );
        self.frame_rate = 1/60.0;
        self.fps_display = FPSDisplay( self );
        self.fps_display.label.font_size = 26;

        self.main_batch = pyglet.graphics.Batch();

        # load the image
        enemy_image = pyglet.image.load( "resource/sprites/enemyShip_Sh01.png" );
        # create a grid of 1 row and 15 columns with 100 width and 100 height
        enemy_sequence = pyglet.image.ImageGrid( enemy_image, 1, 15, item_width = 100, item_height = 100 );
        # create a grid of textures from our sequence of enemies
        #enemy_texture = pyglet.image.TextureGrid( enemy_sequence );
        # create our animation from the first texture to the end with .2 seconds in playback
        # and it's looped animation that mean it's never stop
        enemy_anim = pyglet.image.Animation.from_image_sequence( enemy_sequence[0:], .2, True );

        # this is a self member to be used outside this method
        self.enemy_sprite = pyglet.sprite.Sprite( enemy_anim, x = 400, y = 300, batch = self.main_batch );

        # load the image of explosion
        explosion_image = pyglet.image.load( "resource/sprites/explosion.png" );
        # create a sequence of it in a Grid
        explosion_sequence = pyglet.image.ImageGrid( explosion_image, 4, 5, item_width = 96, item_height = 96 );
        # create a Grid of thier Textures
        #explosion_texture = pyglet.image.TextureGrid( explosion_sequence );
        # create the animation
        explosion_anim = pyglet.image.Animation.from_image_sequence( explosion_sequence[0:], .1, True );

        # finaly create the sprite, explosion and enemy have the same batch ( one batch can render many
        # sprites at the same time )
        self.explosion_sprite = pyglet.sprite.Sprite( explosion_anim, x = 400, y = 100, batch = self.main_batch );

        # like others, load the image create sequnce of it, ant animate it
        head_image = pyglet.image.load( "resource/sprites/ufoHead_Sh.png" );
        head_sequence = pyglet.image.ImageGrid( head_image, 1, 8, item_width = 100, item_height = 100 );
        head_anim = pyglet.image.Animation.from_image_sequence( head_sequence[0:], .1, True );

        self.head_sprite_list = [];

        for head_sprite in range( 5 ):

            self.head_sprite_list.append( pyglet.sprite.Sprite( head_anim, x = randint( 100, 600 ),
                                                                y = randint( 100, 400 ), batch = self.main_batch ) );

        text = pyglet.text.Label( "sub Window", x = 490, y = 560, batch = self.main_batch );
        text.anchor_x = "center";
        text.anchor_y = "center";
        text.bold = True;
        text.font_size = 24;
        text.color = ( 200, 150, 100, 255 );

        self.laser_sound = pyglet.media.load( "resource/sounds/player_gun.wav", streaming = False );


    def on_key_press( self, symbol, modifiers ):

        if symbol == key.SPACE:

            self.laser_sound.play();


    def on_draw( self ):

        self.clear();

        self.fps_display.draw();
        # instead of drawing sprites invidually, batch can draw them at the same time
        self.main_batch.draw();


    def update( self, dt ):

        pass;


if __name__ == "__main__":

    window = GameWindow( 800, 600, "Space Invader Testing", resizable = False );

    pyglet.clock.schedule_interval( window.update, window.frame_rate );

    pyglet.app.run();