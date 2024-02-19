from drivepins import control_gpio_pins
from ABDU import process_orders
import RPi.GPIO as GPIO
from monitortemp import get_cpu_temperature

cpu_temp = get_cpu_temperature()
print(f'CPU Temperature:{cpu_temp:.2f} Celsius') 

while cpu_temp < 75: #ensure system does not overheat
    #manage available quantities here
    item_quantities_available = {'A': 10, 'B': 20, 'C': 10, 'D': 5}
    order_dict = {
    "Order1": 0,  # Initial values can be set to 0; the user will select the item and quantity
    "Order2": 0,
    "Order3": 0,
    "Order4": 0
    }

    #call process_orders from ABDU.py
    results = process_orders(item_quantities_available,order_dict)
    print(results)
    try:
        for order, items in results.items():
            control_gpio_pins(items) #call control_gpio_pins from drivepins.py
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    finally:
        #clean up GPIO on program exit
        GPIO.cleanup()
