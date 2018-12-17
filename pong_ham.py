from sense_hat import SenseHat
from time import *

sense = SenseHat()

white = (255, 255, 255)
purple = (255, 0, 255)
red = (255,0,0)

bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], purple)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y +1):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 0:
        sense.show_message ("Failure.exe")
 
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
    sleep(.000001)
    sense.clear(0,0,0)
    draw_bat()
    draw_ball()
    sense.stick.direction_down = move_down
    sense.stick.direction_up = move_up
    sense.set_rotation(90)
    sleep(.000001)
    sense.set_rotation(180)
    sleep(.000001)
    sense.set_rotation(270)
    sleep(.000001)
