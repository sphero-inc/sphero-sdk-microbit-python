import random
from microbit import display, Image, sleep, pin8, pin12, pin13, pin16
from sphero import RVRDrive, RVRLed, RVRPower


# read the GPIO pins to figure out which button (if any) was pressed
def check_input():
    input_btn = 0
    if pin8.read_digital():
        input_btn = 1  # yellow
    elif pin12.read_digital():
        input_btn = 2  # green
    elif pin13.read_digital():
        input_btn = 3  # red
    elif pin16.read_digital():
        input_btn = 4  # blue
        
    return input_btn


# set RVR's LEDs depending on the randomly generated current_color    
def set_leds():
    if current_color == 1:
        RVRLed.set_all_leds(255, 255, 0)  # yellow
    elif current_color == 2:
        RVRLed.set_all_leds(0, 255, 0)  # green
    elif current_color == 3:
        RVRLed.set_all_leds(255, 0, 0)  # red
    elif current_color == 4:
        RVRLed.set_all_leds(0, 0, 255)  # blue

    return


# show a checkmark if the input_btn matched the current_color
def show_correct_feedback():
    display.show(Image.YES)
    sleep(600)
    display.clear()

    
# show an X if the input_btn did not match the current_color
def show_incorrect_feedback():
    display.show(Image.NO)
    sleep(600)
    display.clear()
    

# wait for RVR to turn on
RVRPower.wake()
sleep(2000)

# initialize values
current_color = random.randint(1, 4)
current_speed = 0
penalty_counter = 0
input_btn = 0


while True:
    set_leds()
    input_btn = check_input()
    penalty_counter += 1
    
    # check if the user takes too long to press a button
    if penalty_counter > 250:
        show_incorrect_feedback()
        current_speed -= 6
        penalty_counter = 0
        current_color = random.randint(1, 4)
        input_btn = 0

    # keep current_speed within the range [0, 60]
    if current_speed > 60:
        current_speed = 60
    if current_speed < 0:
        current_speed = 0

    RVRDrive.drive(current_speed, 0)

    # check user input and give proper feedback
    if input_btn == 0:
        pass
    elif input_btn == current_color:
        show_correct_feedback()
        current_speed += 6
        penalty_counter = 0
        current_color = random.randint(1, 4)
        input_btn = 0
    elif input_btn != current_color:
        show_incorrect_feedback()
        current_speed -= 6
        input_btn = 0
