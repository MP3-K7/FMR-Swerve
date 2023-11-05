#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

#==

# Ev3 and Pybricks references
from pybricks.messaging import BluetoothMailboxServer, TextMailbox, NumericMailbox

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

leftWheelMotor = Motor(Port.A) # the red one but the wheel
rightWheelMotor = Motor(Port.C) # the yellow one but the wheel

leftPivotMotor = Motor(Port.B) # the red one
rightPivotMotor = Motor(Port.D) # the yellow one

#Referencing the current brick as a server
server = BluetoothMailboxServer()

#Creating the mailboxes
testMBox = TextMailbox('testMBox', server)
angleMBox = TextMailbox('angleMBox', server)
velocityMBox = TextMailbox('velocityMBox', server)
rigthArmMBox = LogicMailbox('rigthArmMBox', server)
leftArmMBox = LogicMailbox('leftArmMBox', server)

#==

#Functions:

def changeWheelAngle(targetAngle:int) -> int:
    speed = targetAngle - leftPivotMotor.angle()
    return speed

def ratio(input:int) -> int:
    top = 1
    bottom = 7
    return (input * bottom) / top

def moveWheels(left, right):
    leftWheelMotor.dc(left)
    rightWheelMotor.dc(right)

def rotateWheels(left, right):
    leftPivotMotor.dc(left)
    rightPivotMotor.dc(right)

#==

print('connecting to client...')
server.wait_for_connection()
print('connected!')

leftPivotMotor.reset_angle(0)
rightPivotMotor.reset_angle(0)

leftWheelMotor.reset_angle(0)
rightWheelMotor.reset_angle(0)

testMBox.wait()
print(testMBox.read())

angleMBox.wait()
velocityMBox.wait()

while True:
    #Pivot motors move
    angle = int(angleMBox.read())

    dif = (leftPivotMotor.angle() - rightPivotMotor.angle()) / 2

    pivotSpeed = int(changeWheelAngle(ratio(angle)))

    rotateWheels(pivotSpeed - dif, pivotSpeed + dif)

    #Wheel motors move
    velocity = -int(velocityMBox.read())

    # if (velocity <= 15 & velocity >= -15):
    #     velocity = 0

    # if (velocity > 80):
    #     velocity = 100

    # if (velocity < -80):
    #     velocity = -100

    moveWheels(velocity, velocity)