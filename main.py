a = 0

def on_gesture_shake():
    global a
    a = randint(0, 60)
    if a <= 15:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif a <= 30:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
    elif a <= 40:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif a <= 50:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif a <= 55:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    else:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
