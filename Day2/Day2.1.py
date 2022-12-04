from machine import Pin
import time

red = Pin(19, Pin.OUT)
amber = Pin(18, Pin.OUT)
green = Pin(20, Pin.OUT)

red.value(1)
amber.value(1)
green.value(1)

time.sleep(3)
red.value(0)

time.sleep(1)
amber.value(0)

time.sleep(1)
green.value(0)