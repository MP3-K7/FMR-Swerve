#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server must be started before the client!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox, NumericMailbox

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This is the name of the remote EV3 or PC we are connecting to.

velocityControl = Motor(Port.A)
angleControl = Motor(Port.B)

SERVER = 'ev3server'

client = BluetoothMailboxClient()

testMBox = TextMailbox('testMBox', client)
angleMBox = TextMailbox('angleMBox', client)
velocityMBox = TextMailbox('velocityMBox', client)

print('connecting to server...')
client.connect(SERVER)
print('connected!')


angleControl.reset_angle(0)
velocityControl.reset_angle(0)
# In this program, the client sends the first message and then waits for the
# server to reply.

testMBox.send("Client Is Greeting You")

while True:
    angleMBox.send(int(angleControl.angle()))
    velocityMBox.send(int(velocityControl.angle()))