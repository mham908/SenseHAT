from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)
draw_bat()
    

def move_up(event):
    global bat_y
    if event.action == 'pressed':
        bat_y -= 1

sense.stick.direction_up = move_up
