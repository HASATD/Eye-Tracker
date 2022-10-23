import time
import sys
import RPi.GPIO as GPIO
import thingspeak

redPin = 18  # Set to appropriate GPIO
greenPin = 22  # Should be set in the
bluePin = 37  # GPIO.BOARD format

channel_id = 1847219  # put here the ID of the channel you created before
READ_key = '0X4ZSHAI9SQHFWFY'  # update the "READ KEY"


def channelRead(channel):
    try:
        response = channel.get({})

        if (response == current_led):
            return

        if response == "red":
            led_off.get(current_led)()
            redOn()
            current_led = "red"
        elif response == "green":
            led_off.get(current_led)()
            greenOn()
            current_led = "green"
        elif response == "blue":
            led_off.get(current_led)()
            blueOn()
            current_led = "blue"
        elif response == "yellow on":
            led_off.get(current_led)()
            yellowOn()
            current_led = "yellow"
        elif response == "white on":
            led_off.get(current_led)()
            whiteOn()
            current_led = "white"
        else:
            led_off.get(current_led)()
            allOff()
            current_led = "off"

    except:
        print("connection failure")


def blink(pin):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


def redOn():
    blink(redPin)


def redOff():
    turnOff(redPin)


def greenOn():
    blink(greenPin)


def greenOff():
    turnOff(greenPin)


def blueOn():
    blink(bluePin)


def blueOff():
    turnOff(bluePin)


def yellowOn():
    blink(redPin)
    blink(greenPin)


def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)


def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)


def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


def allOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)


current_led = "off"
led_off = {"red": redOff, "green":  greenOff,  "blue": blueOff,
           "yellow": yellowOff, "white": whiteOff, "off": allOff}

if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=READ_key)
    while True:
        channelRead(channel) 