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
global LsuPhoto
LsuPhoto = ADC(Pin(26))
## The second PhotoResistor is Pin 27
## Named Auburn due to lBue and Orange wires
## Auurn = Bottom Left PhotoResistor
global AuburnPhoto
AuburnPhoto = ADC(Pin(27))
## The third PhotoResistor is Pin 28
## Named Slytherin due to Green and White wires
## Slytheri = Top Center PhotoResistor
SlytherinPhoto = ADC(Pin(28))

## Making variables for the PhotoResistors' values
AubAnolog = AuburnPhoto.read_u16()
SlyAnolog = SlytherinPhoto.read_u16()
LsuAnolog = LsuPhoto.read_u16()

def photoReader(photo_pin):
    val = photo_pin.read_u16()
    perc = val/65535
    fval = perc * 1023
    fval = round(fval)
    return fval

## Assigning the Servos their pins
## Servo Alpha is Pin 7
## Servo Alpha tilts solar panels Up and Down
alphaServo = PWM(Pin(7))
## Servo Zeta is Pin 11
## Servo Zeta rotates solar panels CW & CCW
## CW = Clockwise
## CCW = Counter Clockwise
zetaServo = PWM(Pin(11))

## Variables
## Alpha:
alphaUp = 1000000         ## This is the limit that Servo Alpha can go Up
alphaDown = 1750000       ## This is the limit Servo Alpha can go Down; Also the Starting Position for Servo Alpha
alphaOrigin = 1600000
global alphaCurrent       ## This variable will be used to track the Servo's current 
alphaCurrent = alphaOrigin  ## Setting alphaCurrent 

## Zeta:
zetaMaxLeft = 2500000  ## This is the most Servo Zeta can rotate Left
zetaLeft = 2000000      ## A Position between the MaxLeft and the Original Position
zetaOrigin = 2000000     ## The Original Position for Servo Zeta
zetaRight = 1000000     ## A Position between the Original and the MaxRight Position
zetaMaxRight = 750000  ## This is the most Servo Zeta can rotate Right
global zetaCurrent
zetaCurrent = zetaOrigin ## This will be our variable used in our functions




alphaServo.freq(50) ## Set the frequency for Servo Alpha
zetaServo.freq(50)  ## Set the frequency for Servo Zeta

## Set the Servos into their Starting Position
alphaServo.duty_ns(alphaOrigin)

zetaServo.duty_ns(zetaOrigin)

## turns the LED on & off to confirm the code ran
led.toggle()


while True:
    
    ## printing the PhotoResistor Values
    print(" Auburn = {} | Sly = {} | LSU = {} ".format(photoReader(AuburnPhoto), photoReader(SlytherinPhoto), photoReader(LsuPhoto)))
    
    
    ## Moving Right
    ## If Photoresistor Auburn is getting less sunlight than the other photoresistors
    if(photoReader(AuburnPhoto) > photoReader(SlytherinPhoto) and photoReader(AuburnPhoto) > photoReader(LsuPhoto)):
        ## loop to continuously turn Servo Zeta
        while(photoReader(AuburnPhoto) > photoReader(SlytherinPhoto) and photoReader(AuburnPhoto) > photoReader(LsuPhoto)):
            ## Saftey net to stop Servo Zeta from breaking it's limits
            time.sleep(0.01)
            ## updating zetaCurrent's Position
            zetaCurrent = zetaCurrent + 1000
            ## Moving Servo Zeta to zetaCurrent's new Position
            zetaServo.duty_ns(zetaCurrent)
                
            if(zetaCurrent >= zetaMaxLeft):
                print("hit Right limit")
                break

    ## If Photoresistor Lsu is getting less sunlight than the other photoresistors
    if(photoReader(LsuPhoto) > photoReader(SlytherinPhoto) and photoReader(LsuPhoto) > photoReader(AuburnPhoto)):
        ## loop to continuously turn Servo Zeta
        while(photoReader(LsuPhoto) > photoReader(SlytherinPhoto) and photoReader(LsuPhoto) > photoReader(AuburnPhoto)):
            time
            ## updating zetaCurrent's Position
            zetaCurrent = zetaCurrent - 1000
            ## Moving Servo Zeta to zetaCurrent's new Position
            zetaServo.duty_ns(zetaCurrent)
            
                ## Saftey net to stop Servo Zeta from breaking it's limits
            if(zetaCurrent <= zetaMaxRight):
                print("Hit the Left Limit")
                break

    ## If Photoresistor Slytherin is getting more sunlight than the other photoresistors
    elif(photoReader(SlytherinPhoto) < photoReader(AuburnPhoto) and photoReader(SlytherinPhoto) < photoReader(LsuPhoto)):
        ## loop to continuously turn Servo Alpha
        while(photoReader(SlytherinPhoto) < photoReader(AuburnPhoto) and photoReader(SlytherinPhoto) < photoReader(LsuPhoto)):
            time.sleep(0.01)
            ## updating alphaCurrent's Position
            alphaCurrent = alphaCurrent + 1000
            ## Moving Servo Alpha to alphaCurrent's new Position
            alphaServo.duty_ns(alphaCurrent)
                
            ## Saftey net to stop Servo Alpha from breaking it's limits
            if(alphaCurrent >= alphaUp):
                print("hit bottom limit")
                break

    ## If Photoresistor Slytherin is getting more sunlight than the other photoresistors
    elif(photoReader(SlytherinPhoto) > photoReader(AuburnPhoto) and photoReader(SlytherinPhoto) > photoReader(LsuPhoto)):
        ## loop to continuously turn Servo Zeta
        while(photoReader(SlytherinPhoto) > photoReader(AuburnPhoto) and photoReader(SlytherinPhoto) > photoReader(LsuPhoto)):
            time.sleep(0.01)
            ## updating alphaCurrent's Position
            alphaCurrent = alphaCurrent - 1000
            ## Moving Servo Zeta to zetaCurrent's new Position
            alphaServo.duty_ns(alphaCurrent)
            
            ## Saftey net to stop Servo Zeta from breaking it's limits
            if(alphaCurrent <= alphaDown):
                print("hit the Up Limit")
                break













