import serial  # Import pySerial module
import time  # Import time module

numToCall = '' # Setup container for number to dial

# ----- Menu and modem initialization, TODO split modem menu into 2 funcs
def init(): 
    print('\n\n**************************\nWelcome to PhoneChip v0.1\n**************************\n\n')
    mainMenu = raw_input('Please make a selection by typing the menu number below:\n1. Make a call\n')
    # Only one option for now, this is expandable for sms etc
    if mainMenu == '1':
        while True:
            global numToCall
            numToCall = raw_input('Enter Number\n') # Ask for user to select option with CLI prompt
            str = numToCall # store entered data to anoth var, it just seemed like a good idea
            if (len(str) >= 11):
                break # if legit number, break out of loop
            elif (len(str) < 11): # if not legit number, ask them to enter again
                print('The Number you entered is too short, try again')            
    
    print('Connecting to modem, please wait')
    global ser
    ser = serial.Serial('/dev/ttyS0',115200, timeout=2) # Open up the UART and set speed
    time.sleep(1)
    
    ser.write('AT+CHFA=0\r') # Set audio channel to onboard mic
    time.sleep(1)

    serRead = ser.read(64) # Reading the GSM buffer and emptying it for error free life
    print(serRead)
    
    

    ser.write('AT+ECHO=0,20000,20000,30000,30000,0\r') # This calibrates the echo of the mic and caller, Refer to the Sim800 datasheet for all param values
    time.sleep(1)

    serRead = ser.read(64)
    print(serRead +'Mic and echo calibration complete')

    ser.write('AT+CLVL=90\r') # Set audio levels
    serRead = ser.read(64)
    print(serRead + 'volume is set')

init() # Start Modem and Menu setup

if ser.isOpen():
    print('Connection to port ' +ser.name+ ' is complete')
    time.sleep(2)
    ser.write('AT+CNUM\r') # Get the Sim card's phone number, this checks if the sim is working
    serRead = ser.read(64)
    print(serRead)

    print('Checking network connection...')
    time.sleep(1)       
    print('Now dialing...')     
    ser.write('ATD+'+numToCall+';\r') # Dial out to user entered number
    time.sleep(2)
    serRead = ser.read(64)
    print(serRead)
    
    cmd = raw_input("Type 'x' to hangup or exit\n") # Start exit option
    serRead = ser.read(64)
    print(serRead)

    while True: # Infinate loop waits for user input to exit
        if cmd == 'x':
            ser.write('ATH\r') # Send hangup command
            time.sleep(1)
            ser.close() # close the serial connection to GSM device
            print('Asta la vista, baby')
            exit() # Exit application