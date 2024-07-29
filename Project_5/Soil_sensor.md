# Project Details

```python
from gpiozero import DigitalInputDevice
import time
import datetime
import csv

# Set up the soil moisture sensor
soil_sensor = DigitalInputDevice(12)

# Create a CSV file to log the soil moisture data
with open('soil_moisture_log.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Soil Moisture'])

def log_data(moisture):
    timestamp = datetime.datetime.now().isoformat()
    with open('soil_moisture_log.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, moisture])
    print(f'{timestamp} - Soil Moisture: {moisture}')

while True:
    moisture = 'Wet' if soil_sensor.value == 0 else 'Dry'
    log_data(moisture)
    time.sleep(60)  # Log data every 60 seconds
```
