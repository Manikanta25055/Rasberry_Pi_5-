# Project Details

This is the code for your project on ultrasonic sensor with raspberry pi

```python

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
```
