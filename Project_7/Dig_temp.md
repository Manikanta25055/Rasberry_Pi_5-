# Project Details


```python 
from gpiozero import RGBLED, DigitalOutputDevice, DigitalInputDevice
import time
import datetime
import csv

# Set up the relay
relay = DigitalOutputDevice(17)

# Set up the RGB LED
led = RGBLED(red=18, green=23, blue=24)

# Set up the digital temperature sensor
temp_sensor = DigitalInputDevice(4)

# Temperature threshold for activating the relay (based on the sensor's digita>
TEMP_THRESHOLD = 1  # The threshold to trigger the digital output

# Create a CSV file to log the temperature data
with open('temperature_log.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Temperature Status'])

def log_data(status):
    timestamp = datetime.datetime.now().isoformat()
    with open('temperature_log.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, status])
    print(f'{timestamp} - Temperature Status: {status}')

def update_led(status):
    if status == "High":
        led.color = (1, 0, 0)  # Red for high temperature
    else:
        led.color = (0, 0, 1)  # Blue for low temperature

while True:
    # Read the digital temperature sensor
    temperature_status = temp_sensor.value  # 0 or 1 based on the temperature >

    # Log the temperature data
    status = "High" if temperature_status == TEMP_THRESHOLD else "Low"
    log_data(status)

    # Update the RGB LED based on the temperature status
    update_led(status)

    # Control the relay based on the temperature status
    if temperature_status == TEMP_THRESHOLD:
        relay.on()
        print("Fan turned on!")
    else:
        relay.off()
        print("Fan turned off!")
```

