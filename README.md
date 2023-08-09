# BEEPBERRY    PYTHON-LIB

This is a Python library for BeepBerry. Currently, it includes functionalities for key, RGB light, and screen, encompassing three types of hardware. It can be easily installed via pip and simplifies the process of driving these hardware components.

![](beepberry.jpg)


## Install instructions 

From pip:

```
pip install --upgrade beepberry-lib
```

## Examples

```python
import beepbeery

#rgb
bb=beepberry.BEEPBERRY()
bb.rgb(0,0,100)   #r,g,b   form 0 to 255 
time.sleep(1)
bb.rgb_off()

#button  See: https://gpiozero.readthedocs.io/en/stable/recipes.html#button 
bb.button   #button.is_pressed  button.wait_for_press() button.when_presse  button.when_released

#scr
scr=bb.lcd

font = ImageFont.truetype("yahei.ttf", 24)  # load font

scr.text(xy=(10,10),text='dice',fill='red',font=font)
scr.show() 

bb.show_pic('test.jpg')   #show pics directly
```
## KEYMAP


```
 *                  BBQ20KBD PMOD KEYBOARD LAYOUT
 *
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |      |          |BR     ↑TPY-       |           |       |
 *  | Ctrl |   PgDn   |←TPX- BL(HOME)TPX+→|   PgUp    | MENU  |
 *  |      |          |       ↓TPY+       |           |       |
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |                                                         |
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |#     |1    |2   |3   |(   |   )|_   |    -|    +|      @|
 *  |  Q   |  W  | E  | R  | T  |  Y |  U |  I  |  O  |   P   |
 *  |      |     |PgDn|PgUp|   \|UP  |^   |=    |{    |}      |
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |*     |4    |5   |6   |/   |   :|;   |    '|    "|    ESC|
 *  |  A   |  S  | D  | F  | G  |  H |  J |  K  |  L  |  BKSP |
 *  |     ?|     |   [|   ]|LEFT|HOME|RGHT|V+   |V-   |DLT    |
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |      |7    |8   |9   |?   |   !|,   |    .|    `|       |
 *  |LFTALT|  Z  | X  | C  | V  |  B |  N |  M  |  $  | ENTER |
 *  |      |   K+|  K-|   °|   <|DOWN|>   |MENU |Vx   |       |
 *  +------+-----+----+----+----+----+----+-----+-----+-------+
 *  |            |0   |TAB                |     |             |
 *  | LEFT_SHIFT | ~  |       SPACE       |RTALT| RIGHT_SHIFT |
 *  |            |  Kx|                  &|     |             |
 *  +------------+----+-------------------+-----+-------------+
```


## Change Log

### [0.0.1] - 2023-08-09

- First commit.



