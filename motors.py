from ev3dev.ev3 import * 
from time import sleep
L = LargeMotor('outA')
R = LargeMotor('outD')
sp = 0
for i in range(3):
    sp += 100   #motor speed 
    sleep(0.5)  #sleep worx ONLY with sp, BUT NOT with rut_to_rel's
    L.run_to_rel_pos(position_sp=1080, speed_sp=sp) #speed_sp=100)
    R.run_to_rel_pos(position_sp=1080, speed_sp=sp) #speed_sp=100)
sleep(2) #sleep needed for motor acceleration
