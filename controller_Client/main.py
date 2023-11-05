#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox, NumericMailbox, LogicMailbox

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Button

# This is the name of the remote EV3 or PC we are connecting to.

velocityControl = Motor(Port.A)
angleControl = Motor(Port.B)

ev3client = EV3Brick()

SERVER = 'ev3server'

client = BluetoothMailboxClient()

testMBox = TextMailbox('testMBox', client)
angleMBox = TextMailbox('angleMBox', client)
velocityMBox = TextMailbox('velocityMBox', client)
rightArmMBox = LogicMailbox('rightArmMBox', client)
leftArmMbox = LogicMailbox('leftArmMBox', client)

rightBStay = [False, False]
leftBStay = [False, False]

rightArmActive = False
leftArmActive = False

print('connecting to server...')
client.connect(SERVER)
print('connected!')


angleControl.reset_angle(0)
velocityControl.reset_angle(0)
# In this program, the client sends the first message and then waits for the
# server to reply.

#testMBox.send("Client Is Greeting You")

while True:
    angleMBox.send(int(angleControl.angle()))
    velocityMBox.send(int(velocityControl.angle()))

    if (ev3client.buttons.pressed() == [Button.UP]):
        rightBStay[0] = True
    else:
        rightBStay[0] = False

    if (rightBStay[0] == True and rightBStay[1] == False):
        if (rightArmActive):
            rightArmActive = False
        elif (rightArmActive == False):
            rightArmActive = True

        rightArmMBox.send(rightArmActive)

    rightBStay[1] = rightBStay[0]


    #==


    if (ev3client.buttons.pressed() == [Button.DOWN]):
        leftBStay[0] = True
    else:
        leftBStay[0] = False

    if (leftBStay[0] == True and leftBStay[1] == False):
        if (leftArmActive):
            leftArmActive = False
        elif (leftArmActive == False):
            leftArmActive = True

        leftArmMBox.send(leftArmActive)

    leftBStay[1] = leftBStay[0]