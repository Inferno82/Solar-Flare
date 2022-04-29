from machine import ADC, Pin, PWM
import time

## Assigning the LED its pin
## LED is Pin 15
## LED is an indicator for if the code is running or not
led = Pin(15, Pin.OUT)

## Assigning the PhotoResistors their analog pins
## The first PhotoResistor is Pin 26
## Named Lsu due to Purple and Gold wires
## LSU = Bottom Right PhotoResistor
LsuPhoto = ADC(Pin(26))
## The second PhotoResistor is Pin 27
## Named Auburn due to lBue and Orange wires
## Auurn = Bottom Left PhotoResistor
AuburnPhoto = ADC(Pin(27))
## The third PhotoResistor is Pin 28
## Named Slytherin due to Green and White wires
## Slytheri = Top Center PhotoResistor
SlytherinPhoto = ADC(Pin(28))



## Assigning the Servos their pins
## Servo Alpha is Pin 7
## Servo Alpha tilts solar panels Up and Down
alphaServo = PWM(Pin(7))
## Servo Zeta is Pin 11
## Servo Zeta rotates solar panels CW & CCW
## CW = Clockwise
## CCW = Counter Clockwise
zetaServo = PWM(Pin(11))

##while True:
##    print("LSU = {} ".for mat(LsuPhoto.read_u16()))
##    print("Auburn = {} ".format(AuburnPhoto.read_u16()))
##    print("Slytherin = {} ".format(SlytherinPhoto.read_u16()))
##    time.sleep(1)
##    print(" ")
##    time.sleep(1)

## Variables
## Alpha:
alphaUp = 1000000       ## This is the most Servo Alpha can go Up
alphaDown = 2000000     ## This is the most Servo Alpha can go Down / Also the Original Position for Servo Alpha
global alphaTest        ## This  will be our variable used in our functions
## Zeta:
zetaMaxLeft = 2600000   ## This is the most Servo Zeta can rotate Left
zetaLeft = 2000000      ## A Position between the MaxLeft and the Original Position
zetaOrgin = 1510000     ## The Original Position for Servo Zeta
zetaRight = 1000000     ## A Position between the Original and the MaxRight Position
zetaMaxRight = 500000   ## This is the most Servo Zeta can rotate Right
global zetaCurrent
zetaCurrent = zetaOrgin ## This will be our variable used in our functions


alphaServo.freq(50)
zetaServo.freq(50)

alphaServo.duty_ns(alphaDown)
zetaServo.duty_ns(zetaMaxLeft)
## turns the LED on & off to confirm the code ran
led.toggle()


