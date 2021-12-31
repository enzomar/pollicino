try:
    from RPi import GPIO
except:
    from fake_rpi.RPi import GPIO
    from fake_rpi import toggle_print

    # by default it prints everything to std.error
    toggle_print(False)  # turn on/off printing

from time import sleep

"""
GPIO BOARD– This type of pin numbering refers
to the number of the pin in the plug,
i.e, the numbers printed on the board,
for example, P1. The advantage of this type
of numbering is, it will not change even though
the version of board changes.

GPIO BCM– The BCM option refers to the pin
by “Broadcom SOC Channel. They signify the
Broadcom SOC channel designation. The BCM
channel changes as the version number changes.
"""
_BOARD = "BOARD"  # PIN
_BCM = "BCM"  # GPIO


def on(mode, pin):
    set(mode, pin, 1)


def off(mode, pin):
    set(mode, pin, 0)


def set(mode, pin, value):
    if mode == _BCM:
        GPIO.setmode(GPIO.BCM)
    elif mode == _BOARD:
        GPIO.setmode(GPIO.BOARD)
    else:
        raise ValueError("GPIO Mode {0} unknown".format(mode))
    try:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, value)
        sleep(0.033)
    except:
        raise ValueError("GPIO Pin {0} unknown".format(pin))
        GPIO.cleanup()


def get(mode, pin):
    if mode == _BCM:
        GPIO.setmode(GPIO.BCM)
    elif mode == _BOARD:
        GPIO.setmode(GPIO.BOARD)
    else:
        raise ValueError("GPIO Mode {0} unknown".format(mode))
    try:
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)
    except:
        raise ValueError("GPIO Pin {0} unknown".format(pin))
