from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_UP)

digits = ''
count = 0 
timer = time.ticks_ms()
while True:
    if button.value() == 0: #changed the 0 to a 1
        while button.value():
            pass
        count += 1
        time.sleep(.05)
        timer = time.ticks_ms()
    if time.ticks_ms()-timer > 50 and count:
        if count == 10:
            count = 0
        digits += str(count)
        count = 0
    if time.ticks_ms()-timer > 200 and digits:
        print ('Calling:' + digits)
        digits = ''      
calcnum()

#14201

                   
#     timer = time.ticks_ms()
#     time.ticks_ms()-timer
    

#time.ticks_ms()

