from smbus2 import SMBus
from PIL import Image, ImageDraw, ImageFont
import os
import time

#------------------------
__version__ = '0.0.2'
__last_modified__ = '2023/8/14'

"""
PYTHON-LIB FOR BEEPBERRY BY jd3096
CONTAINS：button|rgb|screen|battery
 *					BBQ20KBD PMOD KEYBOARD LAYOUT
 *
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|      |          |BR     ↑TPY-       |           |       |
 *	| Ctrl |   PgDn   |←TPX- BL(HOME)TPX+→|   PgUp    | MENU  |
 *	|      |          |       ↓TPY+       |           |       |
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|                                                         |
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|#     |1    |2   |3   |(   |   )|_   |    -|    +|      @|
 *	|  Q   |  W  | E  | R  | T  |  Y |  U |  I  |  O  |   P   |
 *	|      |     |PgDn|PgUp|   \|UP  |^   |=    |{    |}      |
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|*     |4    |5   |6   |/   |   :|;   |    '|    "|    ESC|
 *	|  A   |  S  | D  | F  | G  |  H |  J |  K  |  L  |  BKSP |
 *	|     ?|     |   [|   ]|LEFT|HOME|RGHT|V+   |V-   |DLT    |
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|      |7    |8   |9   |?   |   !|,   |    .|    `|       |
 *	|LFTALT|  Z  | X  | C  | V  |  B |  N |  M  |  $  | ENTER |
 *	|      |   K+|  K-|   °|   <|DOWN|>   |MENU |Vx   |       |
 *	+------+-----+----+----+----+----+----+-----+-----+-------+
 *	|            |0   |TAB                |     |             |
 *	| LEFT_SHIFT | ~  |       SPACE       |RTALT| RIGHT_SHIFT |
 *	|            |  Kx|                  &|     |             |
 *	+------------+----+-------------------+-----+-------------+
 *
"""

class BEEPBERRY():

    def __init__(self):
        self.width=400
        self.height=240
        self.i2c=SMBus(1)  
        from gpiozero import Button 
        self.button=Button(17)  #https://gpiozero.readthedocs.io/en/stable/recipes.html#button    
        #button.is_pressed  button.wait_for_press() button.when_presse  button.when_released
        self.image = Image.new("RGB", (self.width, self.height), color=(0,0,0)) 
        self.lcd=ImageDraw.Draw(self.image)
        self.fb_path='/dev/fb1'

    def remove_keyboard(self):
        os.system('sudo modprobe -r bbqX0kbd')

    def load_keyboard(self):
        os.system('sudo modprobe bbqX0kbd')
    
    def rgb(self,r,g,b):
        self.remove_keyboard()  # Must release the I2C bus from the keyboard driver fitst.
        self.i2c.open(1)
        self.i2c.write_byte_data(0x1f, 0xa1, r)
        self.i2c.write_byte_data(0x1f, 0xa2, g)
        self.i2c.write_byte_data(0x1f, 0xa3, b)
        self.i2c.write_byte_data(0x1f, 0xa0, 0xff)
        self.load_keyboard()

    def rgb_off(self):
        self.remove_keyboard()  # Must release the I2C bus from the keyboard driver fitst.
        self.i2c.open(1)
        self.i2c.write_byte_data(0x1f, 0xa0, 0x00)
        self.load_keyboard()
    
    def show(self):
        image_data = self.image.tobytes()
        fb_file = open(self.fb_path, 'wb+')
        fb_file.write(image_data)
        fb_file.close()

    def show_pic(self,filename):
        img1 = Image.open(filename)
        img1 = img1.resize((400, 240))
        gray = img1.convert("1")
        img1=gray.convert("RGB")
        image_data = img1.tobytes()
        fb_file = open(self.fb_path, 'wb+')
        fb_file.write(image_data)
        fb_file.close()
        # box1 = (0, 0, 400, 240)
        # region = img1.crop(box1)
        # self.image.paste(region, (0, 0))
        # self.show()

    def battery(self):
        self.remove_keyboard() 
        rw=self.i2c.read_i2c_block_data(0x1f, 0x17, 2)
        value=rw[1]*256+rw[0]
        vbat = 3.3* (value/4095) * 2
        vbat=round(vbat,2)
        self.load_keyboard()
        return vbat

