'''
Created on 13 de ene. de 2017

@author: daniel.cano
'''
import canlib
from time import sleep

'''    Constants definition    '''
LOW_TIMEOUT = 10    # seconds
HIGH_TIMEOUT = 10   # seconds

'''    Variable definition'''
loop_counter = 0
loop_period = 0.2   # seconds

if __name__ == '__main__':
    canLib = canlib.canlib()

    '''***    Config CAN    ***'''
    ch1 = canLib.openChannel(0, canlib.canOPEN_REQUIRE_EXTENDED + canlib.canOPEN_ACCEPT_VIRTUAL)
    ch1.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch1.setBusParams(canlib.canBITRATE_250K)
    EXTENDED_FLAG = canlib.canMSG_EXT
    ch1.busOn()

    '''***    Loop    ***'''
    while(1):
        if(loop_counter < (LOW_TIMEOUT/loop_period)):
            #  low speed
            ch1.write(0x18FDCD00, [0x10, 00, 00, 00, 00, 00, 00, 00],EXTENDED_FLAG)  # (msgId, msg, flg)

        elif (loop_counter > (LOW_TIMEOUT/loop_period)):
            #  high speed
            ch1.write(0x18FDCD00, [0x30, 00, 00, 00, 00, 00, 00, 00],EXTENDED_FLAG)  # (msgId, msg, flg)
        if (loop_counter >= (HIGH_TIMEOUT+LOW_TIMEOUT)/loop_period):
            loop_counter = 0

        loop_counter += 1
        sleep(loop_period)

    print 'END PROGRAM'
