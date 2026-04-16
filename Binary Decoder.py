from machine import Pin
import time

clock = Pin(16, Pin.IN)
signal = Pin(15, Pin.IN)

data = []
char = []
message = ""
timer = time.ticks_ms()
clock_last = 0

while True:
    if clock.value() == 0 and clock_last == 1:
        if signal.value() == 1:
            data.append('1')
        else:
            data.append('0')
        clock_last = 0
#         timer = time.ticks_ms()
    elif clock.value() == 1:
        clock_last = 1
    if len(data) == 8:
        bi = "".join(data)
#         print(bi)
        x = int(bi, 2)
        character = chr(x)
        char.append(character)
        data = []

    if time.ticks_ms() - timer >= 3000 and char:
        timer = time.ticks_ms()
        message = ''.join(char)
        print(message)
        message = ''
        char = []  

#The clock is at 2 ms per top

#1101000
#14101

# strn = '1101000'
# print(strn)
# x = int(strn, 2)
# print(x)
# character = chr(x)
# print(character)
