from sense_emu import SenseHat

x = y = 4
hat = SenseHat()

def update_screen():
    humidity = hat.humidity
    temp = hat.temp
    hat.clear()
    if humidity > 45:
        bg_color = (0, 0, 255)
    else:
        bg_color = (255, 255, 255)
    pixels = [bg_color for i in range(64)]
    hat.set_pixels(pixels)
    if temp > 25:
        cursor_color = (255, 0, 0)
    else:
        cursor_color = (0, 255, 0)
    hat.set_pixel(x, y, cursor_color)

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        x = clamp(x + {
            'left': -1,
            'right': 1,
            }.get(event.direction, 0))
        y = clamp(y + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))

update_screen()
while True:
    for event in hat.stick.get_events():
        move_dot(event)
        update_screen()
