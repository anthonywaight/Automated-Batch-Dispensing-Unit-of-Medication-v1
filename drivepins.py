import RPi.GPIO as GPIO
import time

#set GPIO mode to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

#define GPIO PIN

mode_pins = {
   
    'A': 23, #pull high to select motor 1
    'B': 24,
    'C': 25,
    'D': 18
}

#setup GPIO pins as outputs
for pin in mode_pins.values():
    GPIO.setup(pin,GPIO.OUT)



def control_gpio_pins(order_items):
    for candy, quantity in order_items:
        pin = mode_pins.get(candy)
        if pin is not None:
            for i in range(quantity):
                #set GPIO pin high for short duration
                GPIO.output(pin, GPIO.HIGH)
                print(f"Setting GPIO pin {pin} high for candy {candy}")
                #wait for short duration
                time.sleep(0.5)
                #set gpio pin low
                GPIO.output(pin,GPIO.LOW)
                print(f'Setting GPIO pin {pin} low for candy {candy}')