import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out

IO.setup(22,IO.OUT) #GPIO 4 -> Motor 1 terminal A, change
IO.setup(24,IO.OUT) #GPIO 24 -> Motor 1 terminal B, change

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A, fixed
IO.setup(23,IO.OUT) #GPIO 23 -> Motor Left terminal B. change

while 1:

 

    if(IO.input(2)==True and IO.input(3)==True): #both while move forward     
        IO.output(22,True) #1A+
        IO.output(24,True) #1B-

        IO.output(17,True) #2A+
        IO.output(23,True) #2B-

    elif(IO.input(2)==False and IO.input(3)==True): #turn right  
        IO.output(22,True) #1A+
        IO.output(24,True) #1B-

        IO.output(17,True) #2A+
        IO.output(23,False) #2B-

    elif(IO.input(2)==True and IO.input(3)==False): #turn left
        IO.output(22,True) #1A+
        IO.output(24,False) #1B-

        IO.output(17,True) #2A+
        IO.output(23,True) #2B-

    else:  #stay still 
        IO.output(22,True) #1A+
        IO.output(24,False) #1B-

        IO.output(17,True) #2A+
        IO.output(23,False) #2B-
