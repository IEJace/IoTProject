On = False
Time = 0

def on_button_pressed_a():
    global On
    On = True
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(5000)
    basic.show_string("ON")
    basic.pause(5000)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global On
    On = False
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # # # . #
        """)
    basic.pause(5000)
    basic.show_string("OFF")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_every_interval():
    global Time
    while On == True:
        Time += 1
        datalogger.log(datalogger.create_cv("Temperature", input.temperature()),
            datalogger.create_cv("Light", input.light_level()),
            datalogger.create_cv("Sound", input.sound_level()),
            datalogger.create_cv("Time", Time))
loops.every_interval(60000, on_every_interval)
