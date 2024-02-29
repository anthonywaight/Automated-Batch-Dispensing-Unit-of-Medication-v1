import RPi.GPIO as GPIO
import time
import smbus

bus = smbus.SMBus(1)  # 1 indicates the I2C bus number, it might be 0 for some systems

# Define the I2C address of the PIC microcontroller
i2c_address = 0x30 # Change this to the actual I2C address of your PIC

# Function to encode the item and quantity and send it over I2C
def send_order(order_data):
    
    for order, items in order_data.items():
        for item, quantity in items:
            # Encode item and quantity
            encoded_data = (ord(item) - ord('A')) << 4 | quantity

            # Send the data over I2C
            bus.write_byte(i2c_address, encoded_data)

            time.sleep(.001)

    bus.close()

        
