# All you need to know about GPIO's
![Screenshot 2024-06-12 at 4 15 26 PM](https://github.com/Manikanta25055/Rasberry_Pi_5-/assets/69751652/686a8471-4b7c-41ff-95fd-51f922f4869f)

When you want to turn on the LED, set the GPIO to *high*, and when you want to turn off the LED, set it to *low*

Code:

```
from gpiozero, import LED
from time import sleep

led = LED(17)

While True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)



