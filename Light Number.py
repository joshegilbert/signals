from machine import Pin
import time

laser = Pin(17, Pin.OUT)

pules = .05
breaks = .2


x = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
while True:
    for i in x:
        for l in range(0,i):
            laser.value(1)
            time.sleep(pules) '''.05''' '''.025'''
            laser.value(0)
            time.sleep(pules) '''.05''' '''.025'''
        time.sleep(breaks) '''.2'''
    time.sleep(.08)
        
#         .0025
#[100, .05 - pulse] [200 .2- break] [.08- break] - arms length, 10 pulses
#[50, .025 - pulse] [200 .2- break] [.08- break] - next to you, 20 pulses


#14101
