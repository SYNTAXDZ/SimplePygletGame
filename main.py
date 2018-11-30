#!/usr/bin/env python3
import pyglet;
from pyglet.window import key, FPSDisplay;
# drna import lel class li na7tajouha
from gameObjects import GameObject, preload_image;
from gameAnim import GameAnim;

#TODO: add more features to the game
class GameWindow( pyglet.window.Window ):

    def __init__( self, *args, **kwargs ):

        # super() dir call lel constructor ta3 pyglet.window.Window w tkhalina
        # ndirou overriding lel methods ta3 pyglet.window.Window fel class ta3na
        super( GameWindow, self ).__init__( *args, **kwargs );

        # hadi location ta3 l window f screen
        self.set_location( 400, 0 );
        self.frame_rate: float = 1/60;

        # hna criyina display lel FPS
        self.fps_display = FPSDisplay( self );

        # set permission to go left or right, using the new syntax on python
        self.left:  bool = False;
        self.right: bool = False;
        self.fire:  bool = False;

        self.player_speed: int = 260;
        self.spawn_time:   int =  30;
        self.score:        int =   0;
        self.fire_rate:    int =  10;

        # hna criyina sprite ta3 l player ta3na
        player_sprite: object = pyglet.sprite.Sprite( preload_image( "PlayerShip.png" ) );

        # drna instance lel GameObject class bach criyina player ta3na
        self.player: object = GameObject( 190, 50, player_sprite );

        # the laser that will be launched by our player
        self.player_laser =  preload_image( "laser.png" );
        self.player_laser_list = [];

        # hna criyna list ta3 space
        self.space_list = [];

        # drna loading lel image from disk
        self.space_img = preload_image( "space.jpg" );

        # drna loop f range 2
        for i in range( 2 ):
            # space_list zadnalah GameObject() y mara ysawi 0 w GameObject zawej ysawi 1200
            self.space_list.append( GameObject( 0, i * 1200, pyglet.sprite.Sprite( self.space_img ) ) );

        # drna loop 3la space_list w koul wa7ed velocity.y ta3ah radinaha -45
        #for space in self.space_list:
         #   # hna space 3tinaha velocity 'y' bach yatmacha fel y axis
          #  space.velocity[1] = -70;
        self.mainBatch = pyglet.graphics.Batch();
        #enemy_image = preload_image( "enemyShip_Sh01.png" );
        self.enemies = [];
        #self.enemy1 = GameObject( 450, 600, pyglet.sprite.Sprite( enemy_image ), batch = self.mainBatch, image = enemy_image );
        self.enemy: GameAnim = GameAnim( pos_x = 450, pos_y = 700, image = "enemyShip_Sh01.png", batch = self.mainBatch );

        self.enemy.animate(1, 15, 100, 100);
        self.enemies.append(self.enemy);

        self.score_label: object = pyglet.text.Label( text = "score: " + str( self.score ), x = 370, y = 655, font_size = 32, batch = self.mainBatch );
        self.score_label.color = [ 200, 20, 100, 255 ];

    # hadi l func dir handle lel inputs, ta9bel two param, symbol ay l key li ta3fess 3lih w modifiers ay ctrl maj...
    def on_key_press( self, symbol, modifiers ):

        # loukan ta3fess 3la key.RIGHT
        if symbol == key.RIGHT:  self.right = True;
        elif symbol == key.LEFT:    self.left = True;
        elif symbol == key.ESCAPE: pyglet.app.exit();
        elif symbol == key.SPACE:   self.fire = True;

    # hadi l func ta3 ki ta3fess 3la key w tagla3 sba3ak
    def on_key_release( self, symbol, modifiers ):

        # loukan key howa RIGHT wala LEFT
        if symbol == key.RIGHT:   self.right = False;
        elif symbol == key.LEFT:  self.left  = False;
        elif symbol == key.SPACE: self.fire  = False;
        elif symbol == key.ESCAPE: pyglet.app.exit();


    def update_player( self, dt ):

        # drna call lel update ta3 gameObject
        self.player.update();

        if self.right and self.player.posX < 838:

            self.player.posX += self.player_speed * dt;

        if self.left and self.player.posX > 0:

            self.player.posX -= self.player_speed * dt;


    def update_player_laser( self, dt ):

        newEnemy: object = GameAnim( pos_x = 450, pos_y = 700, image = "enemyShip_Sh01.png", batch = self.mainBatch );

        for laser in self.player_laser_list:
            # update laser
            laser.update();

            # change it pos in the y-axis
            laser.posY += 400 * dt;
            # when it reaches this position
            if laser.posY >= 700:
                # remove the laser from the list
                self.player_laser_list.remove( laser );

            for enemy in self.enemies:

                if enemy.collided( laser ):

                    enemy.destroy();
                    self.enemies.remove( enemy );
                    self.score += 1;

                    newEnemy.animate( 1, 15, 100, 100 );
                    self.enemies.append( newEnemy );



    def player_fire( self, dt ):

        if self.fire_rate < 10: self.fire_rate += 1;

        # if you are shooting so append a new laser to the list of lasers
        if self.fire and self.fire_rate >= 10:
            # when you press SPACE you will add a player_laser object at position of the center of player
            self.player_laser_list.append( GameObject( self.player.posX + 30, self.player.posY + 93, pyglet.sprite.Sprite( self.player_laser ) ) );

            self.fire_rate = 0;



    # hadi l func hiya li dir handling lel space movements...
    def update_space( self, dt ):

        # hna drna update l koul space f space_list
        for space in self.space_list:

            space.update();
            space.posY -= 60 * dt;

            # loukan space pos ykoun l ta7t sceeen
            if space.posY <= -1300:
                # dilah remove
                self.space_list.remove( space );

                # 3awed zid wa7ed f top (posY=1100)
                self.space_list.append( GameObject( 0, 900, pyglet.sprite.Sprite( self.space_img ) ) );


    def update_enemy( self, dt ):

        newEnemy: GameAnim = GameAnim( pos_x = 450, pos_y = 700, image = "enemyShip_Sh01.png", batch = self.mainBatch );

        #self.enemy.update( _y = 150*dt );
        for _enemy in self.enemies:

            _enemy.update( 300*dt );

            if _enemy.collided( self.player ):

                _enemy.destroy();
                self.enemies.remove( _enemy );

                newEnemy.animate( 1, 15, 100, 100 );
                self.enemies.append( newEnemy );

            if _enemy.pos_y <= 0:

                _enemy.destroy();
                self.enemies.remove( _enemy );

                newEnemy.animate( 1, 15, 100, 100 );
                self.enemies.append( newEnemy );


    def update_score( self, dt ):

        self.score_label.text = "Score: " + str( self.score );

        if self.score < 35 and self.score > 19:

            self.score_label.color = [ 200, 120, 100, 255 ];

        elif self.score < 49 and self.score > 35:

            self.score_label.color = [ 200, 220, 100, 255 ];

        elif self.score < 100 and self.score > 49:

            self.score_label.color = [ 180, 255, 100, 255 ];


    # hadi dir update lel objects ay game loop ta3na, dt == deltaTime
    def update( self, dt ):
        # invoking the update methods
        self.update_player( dt );
        self.update_player_laser( dt );
        self.update_space( dt );
        self.player_fire( dt );
        self.update_enemy( dt );
        self.update_score( dt );


    # on_draw() func to draw everthing
    def on_draw( self ):

        # clear the screen
        self.clear();

        # hna drna draw l koul space f space_list
        for space in self.space_list:
            space.draw();

        # hna jabna draw( m GameObject class w rssamnah hna
        self.player.draw();

        # draw lasers
        for laser in self.player_laser_list:
            laser.draw();

        # drna draw lel fps ta3na
        self.fps_display.draw();
        self.mainBatch.draw();


def main() -> None:

    # create an instance of GameWindow class
    window = GameWindow(900, 700, "Space invader", resizable=False);

    # hadi clock.schedule_interval() dir call lel update func every frame
    pyglet.clock.schedule_interval(window.update, window.frame_rate);

    # run the app
    pyglet.app.run();


if __name__ == "__main__":

    main();
