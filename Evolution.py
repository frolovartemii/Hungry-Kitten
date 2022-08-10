import arcade
import random
HEIGHT = 600
WIDTH = 1000
SCALE = 0.3
SPEED_ICH_X = 5
SPEED_ICH_Y = 5
TITLE = "Hungry Kitten"
class Cursor(arcade.Sprite):
    def __init__(self):
        super().__init__("Evolution\cursor.png",scale = 0.1)
class I(arcade.Sprite):
    def __init__(self, scale):
        super().__init__("Evolution\Cat.png", scale)
        self.center_x = kruk.width/2
        self.center_y = kruk.height/2
        self.sound = arcade.load_sound("Evolution\zvuk-myaukan-e-koshki (mp3cut.net).mp3")
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.bottom <= 0:
            self.bottom = 0
        if self.top >= kruk.height:
            self.top = kruk.height
        if self.right >= kruk.width:
            self.right = kruk.width
        if self.left <= 0:
            self.left = 0
class Yenemy(arcade.Sprite):
    def __init__(self, scale):
        a = kruk.height
        b = kruk.width
        super().__init__("Evolution\Don.png",scale)
        tx_1 = arcade.load_texture("Evolution\Clock.png")
        tx_2 = arcade.load_texture('Evolution\Don.png')
        tx_3 = arcade.load_texture("Evolution\Sun.png")
        tx_4 = arcade.load_texture("Evolution\Smile.png")
        tx_5 = arcade.load_texture("Evolution\Rad.png")
        list = [tx_1, tx_2, tx_3, tx_4, tx_5]
        self.sides = [ 'left', 'right', 'top', 'bottom']
        self.side = random.choice(self.sides)
        if self.side == "left":
            self.right = 0
            self.center_y = random.randint(0,a)
            self.change_x = random.uniform(1,5)
            self.change_y = random.uniform(-2, 2)
        if self.side == "right":
            self.left = b
            self.center_y = random.randint(0,a)
            self.change_x = random.uniform(-5,-1)
            self.change_y = random.uniform(-2, 2)
        if self.side == "top":
            self.bottom = a
            self.center_x = random.randint(0,b)
            self.change_x = random.uniform(-2,2)
            self.change_y = random.uniform(-5,-1)
        if self.side == "bottom":
            self.top = 0
            self.center_x = random.randint(0,b)
            self.change_x = random.uniform(-2,2)
            self.change_y = random.uniform(1,5)
        self.texture = random.choice(list)
    def update(self):
        a = kruk.height
        b = kruk.width
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.side == "left":
            if self.left > b or self.bottom > a or self.top < 0:
                self.kill()
        if self.side == "right":
            if self.right < 0 or self.bottom > a or self.top < 0:
                self.kill()
        if self.side == "top":
            if self.right < 0 or self.left > b or self.top < 0:
                self.kill()
        if self.side == "bottom":
            if self.right < 0 or self.left > b or self.bottom > a:
                self.kill()
class Window(arcade.Window):
    def __init__(self, width,height,title):
        super().__init__(width,height,title, True)
        self.tx_0 = arcade.load_texture("Evolution\start_screen.jpg")
        self.tx = arcade.load_texture("Evolution\Background_2.jpg")
        self.tx_2 = arcade.load_texture("Evolution\The_end.jpg")
        self.tx_3 = arcade.load_texture("Evolution\Background_3.jpg")
        self.ich = None
        self.start = False
        self.cursor = Cursor()
        self.a = SCALE
        self.b = self.width/2
        self.c = self.height/2
        self.game = False
        self.pause = False
        self.yenemies = arcade.SpriteList()
    def set_up(self):
        self.ich = I(0.3)
    def on_draw(self):
        if self.start == False:
            arcade.draw_texture_rectangle(center_x=self.width/2, center_y=self.height/2, height=self.height, width=self.width, texture= self.tx_0)
        elif self.game == False and self.pause == False:
            arcade.draw_texture_rectangle(center_x=self.width/2, center_y=self.height/2, height=self.height, width=self.width, texture= self.tx)
            self.yenemies.draw()
            self.ich.draw() 
        elif self.pause == True:
            arcade.draw_texture_rectangle(center_x=self.width/2, center_y=self.height/2, height=self.height, width=self.width, texture= self.tx_3)
            self.ich.draw()
        elif self.game == True:
            arcade.draw_texture_rectangle(center_x=self.width/2, center_y=self.height/2, height=self.height, width=self.width, texture= self.tx_2)
        self.cursor.draw()
    def on_update(self, delta_time):
        if self.game == False and self.pause == False and self.start == True:
            self.ich.scale = self.a
            self.ich.center_x = self.b
            self.ich.center_y = self.c
            self.yenemies.update()
            self.ich.update()
            while len(self.yenemies) < 30:
                yenemy = Yenemy(scale = random.uniform(0.1, self.ich.scale + 0.3))
                self.yenemies.append(yenemy)
            hit_list = arcade.check_for_collision_with_list(self.ich, self.yenemies)
            for yenemy in hit_list:
                if yenemy.scale < self.ich.scale + 0.05:
                    self.ich.scale += 0.01
                    yenemy.kill()
                if yenemy.scale > self.ich.scale + 0.05:
                    self.ich.scale -= 0.05
                    if self.ich.scale <= 0.2:
                        self.game = True
            self.a = self.ich.scale
            self.b = self.ich.center_x
            self.c = self.ich.center_y
        if self.pause == True:
            self.ich.scale = 1.8
            self.ich.center_x = self.width/2
            self.ich.center_y = self.height - 260
            self.ich.angle += 1
    def on_key_press(self, key: int, modifiers: int):
        if self.pause == False:
            if key == arcade.key.D:
                self.ich.change_x = SPEED_ICH_X
            if key == arcade.key.A:
                self.ich.change_x = -SPEED_ICH_X
            if key == arcade.key.W:
                self.ich.change_y = SPEED_ICH_Y
            if key == arcade.key.S:
                self.ich.change_y = -SPEED_ICH_Y
        if key == arcade.key.ESCAPE:
            self.close()
        if self.game == False and self.start == True:
            if key == arcade.key.ENTER:
                if self.pause == False:
                    self.pause = True
                else:
                    self.pause = False
        if self.start == False:
            if key == arcade.key.ENTER:
                self.start = True
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.D or key == arcade.key.A:
            self.ich.change_x = 0
        if key == arcade.key.S or key == arcade.key.W:
            self.ich.change_y = 0
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.set_mouse_visible(False)
        self.cursor.center_x = x
        self.cursor.center_y = y
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game == False and self.pause == False:
            if button == arcade.MOUSE_BUTTON_LEFT:
                if self.ich.left < x < self.ich.right and self.ich.bottom < y < self.ich.top:
                    self.ich.sound.play(1)
        elif self.pause == True:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.ich.sound.play(1)
        else:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.ich.sound.play(1)
kruk = Window(width = WIDTH, height=  HEIGHT,title =  TITLE)
kruk.set_up()
arcade.run()