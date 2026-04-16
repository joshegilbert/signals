from machine import Pin
import time

clock = Pin(16, Pin.OUT)
signal = Pin (15, Pin.OUT) 

time_clock = 1


string = 'Fire Gator Thursday!'
listy = []
zero = '0'

for ch in string:
    bina = bin(ord(ch))[2:]
    while len(bina) < 8:
        bina = zero + bina
    listy.append(bina)  
print(listy)

# listy = ['10101010']

while True:
    clock.value(0)
    signal.value(0)
    time.sleep(3)
    for bi in listy:
#         print(bi)
        for c in bi:
            clock.value(1)
            time.sleep_ms(time_clock)
            signal.value(1 if c == '1' else 0)
            time.sleep_ms(time_clock)
            clock.value(0)
            time.sleep_ms(time_clock)
            signal.value(0)
            time.sleep_ms(time_clock)
           
#1100001 
#100 characters(bits per second) in a second   
#14201
#31 bites per second
            
# string = input("What is the code: ")
# for i in string:
#      aski = ord(string)
#      bina = bin(aski)
#      inputs = bina[2:]
#             while inputs not False:
#                     for dig in inputs:
#                         clock.value(1)
#                         time.sleep_ms(time_clock)
#                         signal.value(1 if dig == '1' else 0)
#                         time.sleep_ms(time_clock)
#                         clock.value(0)
#                         time.sleep_ms(time_clock)
#                         signal.value(0)
#                         time.sleep_ms(time_clock)
#                      inputs = []

# aski = ord(string)
# print(aski)

# bina = bin(aski)
# print(bina)

# inputs = bina[2:]
# print(inputs)
