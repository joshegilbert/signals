from machine import Pin
import time

button = Pin(16, Pin.IN)

digits = ''
count = 0 
timer = time.ticks_ms()
while True:
    if button.value() == 1:
        while button.value():
            pass
        count += 1
        time.sleep(.05)
        timer = time.ticks_ms()
    if time.ticks_ms()-timer > 100 and count:
        if count == 10:
            count = 0
        digits += str(count)
        count = 0
    if time.ticks_ms()-timer > 200 and digits:
        print ('Calling:' + digits)
        digits = ''      
calcnum() 
            
            
#     timer = time.ticks_ms()
#     time.ticks_ms()-timer
    

#time.ticks_ms()

