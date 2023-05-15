from microbit import *
from Maqueen import *

while true:
    distancia = read_distance()
    if distancia < 10:
        self.motor_stop_all()
    else:
        self.set.motor(0,255)
        self.set.motor(1,255)
