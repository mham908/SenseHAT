from sense_hat import SenseHat
from time import *

sense = SenseHat()

white = (255, 255, 255)
purple = (230, 230, 255)

bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_ball():
      sense.set_pixel(ball_position,ball_position,purple)
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1
    

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1



    
sense.clear(0,0,0)
while True:
    sleep(.25)
    sense.clear(0,0,0)
    draw_bat()
    sense.stick.direction_down = move_down
    sense.stick.direction_up = move_up