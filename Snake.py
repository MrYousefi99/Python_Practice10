import arcade
import random


SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Joystick Example"

MOVEMENT_SPEED = 3

class Snake(arcade.Sprite) :
  def __init__(self,scale):
    super().__init__()
    
    self.color = arcade.color.BABY_BLUE
    self.width = 20
    self.height = 20
    self.speed = MOVEMENT_SPEED
    self.score = 0
    self.direction = "up"
    self.center_x = SCREEN_WIDTH//2
    self.center_y = SCREEN_HEIGHT//2
    
  
  def draw(self) :
    arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
    
  def move(self) :
        
    if    self.direction == "left":
          self.center_x -= MOVEMENT_SPEED
    elif  self.direction == "right":
          self.center_x += MOVEMENT_SPEED
    elif  self.direction == "up":
          self.center_y += MOVEMENT_SPEED
    elif  self.direction == "down":
          self.center_y -= MOVEMENT_SPEED  

class Apple(arcade.Sprite) :
  def __init__(self) :
        super().__init__()  
            
        self.center_x = random.randint(10, 480)
        self.center_y = random.randint(10, 480)
        txc = arcade.load_texture("sib.jpg")
        self.texture = txc
        self.scale = 0.09

  def on_draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 30, 30, self.texture)  
    
  
  
  
  
class Game(arcade.Window) :
  def __init__(self):
    super().__init__(width=600,height=500,title="Snake Game 2022")
    self.background_color = arcade.color.YELLOW
    self.food = Apple()
    self.snake = Snake(SPRITE_SCALING)
    
    
    self.all_sprites_list = None

    self.player_sprite = None
  
  def setup(self):
        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite =Snake(SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

  def on_draw(self):
    arcade.start_render()  
    self.snake.draw() 
    self.food.draw()
  
  
  def on_update(self, delta_time):

        self.all_sprites_list.update()
        self.snake.move()
        
        if arcade.check_for_collision(self.snake, self.food):
           self.food.center_x = random.randint(0, 600)
           self.food.center_y = random.randint(0, 500)
                  
                  
  def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED


  def on_key_release(self, key : int, modifiers: int):
        if key == arcade.key.LEFT:
            if self.snake.direction != "right":
                self.snake.direction = "left"
      
        elif key == arcade.key.DOWN:
            if self.snake.direction != "up":
                self.snake.direction = "down"  
        elif key == arcade.key.RIGHT:
            if self.snake.direction != "left":
                self.snake.direction = "right"
        elif key == arcade.key.UP:
            if self.snake.direction != "down":
                self.snake.direction = "up"
                   

            
  
    



mygame = Game()
mygame.setup()
arcade.run()


    

