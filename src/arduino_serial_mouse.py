#!/usr/bin/python
import serial
import pyautogui
import time

MAXSPEED = 30
INC = 4

move_dict = {
    "0":( 0, 0),
    "1":(INC, 0),
    "2":( 0, INC),
    "3":( 0, 0),
    "4":( -INC, 0),
    "5":( 0, -INC),
    "6":( 0, 0),
    "7":( 0, 0),}

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

def map_num_to_mouse(number):
    """
    move_dict = {
        "0":( 0, 0),
        "1":(INC, 0),
        "2":( 0, INC),
        "3":( 0, 0),
        "4":( -INC, 0),
        "5":( 0, -INC),
        "6":( 0, 0),
        "7":( 0, 0),}
    """
    if number == 7:
        print("CLICK!")
        pyautogui.click()
        return 2
    else:
        #TODO: crashes if I give it a number not in the dictionary
        pyautogui.moveRel(move_dict[str(number)])
        return 1

def slow_speed(axis_speed):
    print("entering slow_speed...")
    if axis_speed == INC:
        return 0
    if axis_speed == -INC:
        return 0
    if axis_speed > 0:
        return (axis_speed - INC)
    if axis_speed < 0:
        return (axis_speed + INC)
    else:
        return 0

def inertia_mouse(x_speed, y_speed, button_state):
    print("STARTING x_speed is: " + str(x_speed) + ", y_speed is " + str(y_speed))
    #print("Hey! We got into intertia_mouse!")
    #RIGHT
    if button_state == 1 and x_speed < (MAXSPEED - INC):
        print("RIGHT")
    #if button_state == 1 and x_speed < (MAXSPEED - INC):
        x_speed += INC
        y_speed = slow_speed(y_speed)
    #LEFT
    elif button_state == 4 and x_speed > (-MAXSPEED + INC):
        print("LEFT")
    #else if button_state == 4 and x_speed > (-MAXSPEED + INC):
        x_speed -= INC
        y_speed = slow_speed(y_speed)
    #UP
    elif button_state == 2 and y_speed < (MAXSPEED - INC):
        print("UP")
        y_speed += INC
        x_speed = slow_speed(x_speed)
    #DOWN
    elif button_state == 5 and y_speed > (-MAXSPEED + INC):
        print("DOWN")
        y_speed -= INC
        x_speed = slow_speed(x_speed)
    #HOLD
    elif button_state == 7: 
        print("HOLD!")
    elif button_state == 3:
        print("CLICK")
        pyautogui.click()
        x_speed = slow_speed(x_speed)
        y_speed = slow_speed(y_speed)
        time.sleep(.25)
    else:
        x_speed = slow_speed(x_speed)
        y_speed = slow_speed(y_speed)
    print("ENDING x_speed is: " + str(x_speed) + ", y_speed is " + str(y_speed))
    if x_speed or y_speed:
        pyautogui.moveRel(x_speed, y_speed)
    return x_speed, y_speed

def main():
    print("entering main...")
    for i in xrange(10):
        try:
            #assuming your arduino appears in /dev as ttyACM<number>
            print("Trying /dev/ttyACM" + str(i) + "...")
            arduino = serial.Serial('/dev/ttyACM'+str(i), 9600, timeout=.1)
            print("Success! Connecting...")
            time.sleep(1)
            break
        except:
            print("/dev/ttyACM" + str(i) + " didn't work.")
    print("setting temp_x_speed and temp_y_speed to 0")
    x_speed = 0
    y_speed = 0
    time.sleep(1)
    while True:
        data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
        print("data is... " + str(data))
        if len(data) == 3:
            button_state = sum_digits(data)
            print("button state is " + str(button_state))
            #map_num_to_mouse(sum_digits(data))
            x_speed, y_speed = inertia_mouse(x_speed, y_speed, button_state)
        #time.sleep(.5)

def stop():
    print("\nGot keyboard interrupt, Stopping!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop()

