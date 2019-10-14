# Sphero SDK

Greetings adventurous students, developers, hackers, and makers!  RVR is one of the best starting points into the vast world of robotics, and we’re here to help you get started with using our approachable development tools.

## First things first

### Getting Started

Visit our [Getting Started](http://sdk.sphero.com/getting_started) to learn more about the ins-and-outs of working with RVR, including some important details on the getting started process.

### More information and documentation

Visit our [SDK website](sdk.sphero.com) to find more information about RVR, the SDK and the API!

### Where to get help

Visit our [community forum](https://community.sphero.com/c/advanced-programming) to get help, share your project, or help others!

### Staying up to date

Consider [signing up](http://sdk.sphero.com/sign-up) for our SDK email list to stay current on new features being released in our robot firmware as well as our SDKs, including new platform / language support.

# micro:bit Python SDK

This module contains the set of commands that allow the micro:bit to communicate with the [Sphero RVR](https://www.sphero.com/rvr) robot.

In order to use the SDK, `sphero.py` will need to be copied onto the micro:bit, along with the Python file to be run.

The drive commands can be accessed by typing `from sphero import RVRDrive, RawMotorModes` at the top of the Python file.
<br>The **RawMotorModes** class is only used to specify the _left\_mode_ and _right\_mode_ values of the **set\_raw\_motors** command, and may be excluded from the import statement if the user does not wish to use this command.

The LED commands can be accessed by typing `from sphero import RVRLed, LEDs` at the top of the Python file.
<br>The **LEDs** class is only used to specify the _index_ value of the **set\_rgb\_led\_by\_index** command, and may be excluded from the import statement if the user does not wish to use this command.

The power commands can be accessed by typing `from sphero import RVRPower` at the top of the Python file.

**Note:** Due to the micro:bit's memory constraints, `sphero.py` contains a lot of seemingly arbitrary hexadecimal values. This is not good programming practice, and was only used to allow as much space for the user as possible in the micro:bit's limited memory.


## RVRDrive

The class containing all RVR drive commands. All drive commands are static, and can be called by typing `RVRDrive.<command>`.
    
**Examples:**
    
    RVRDrive.drive(60, 90)
    RVRDrive.set_raw_motors(RawMotorModes.FORWARD, 80, RawMotorModes.FORWARD, 80)
    RVRDrive.reset_yaw()
   
**Note:** Unless stated otherwise, the commands will not work if the provided values are outside of the specified ranges.

* **drive**(*speed*, *heading*): drives the robot at the given speed with the given heading.
  * *speed* (int): an integer from 0-255
  * *heading* (int): an integer from 0-359 degrees (0 is forwards, 90 is to the right, 180 is backwards, and 270 is to the left)
* **stop**(*heading*): tells the robot to stop driving. The heading should be the robot's current heading.
  * *heading* (int): an integer from 0-359 (0 is forwards, 90 is to the right, 180 is backwards, and 270 is to the left)
* **set\_raw\_motors**(*left\_mode*, *left\_speed*, *right\_mode*, *right\_speed*): sets the motors' modes and speeds individually. If a mode value outside of the 0-2 range is given, the mode will default to 0 (off).
  * *left\_mode* (**RawMotorModes**): a member of the **RawMotorModes** class representing the drive mode for the left motor (OFF, FORWARD, BACKWARD)
  * *left\_speed* (int): an integer from 0-255
  * *right\_mode* (**RawMotorModes**): a member of the **RawMotorModes** class representing the drive mode for the right motor (OFF, FORWARD, BACKWARD)
  * *right\_speed* (int): an integer from 0-255
* **reset\_yaw**(): sets the robot's current yaw angle to zero.

## RVRLed

The class containing all RVR LED commands. All LED commands are static, and can be called by typing `RVRLed.<command>`.
    
**Examples:**

    RVRLed.set_all_leds(0, 0, 255)
    RVRLed.set_rgb_led_by_index(LEDs.RIGHT_STATUS, 140, 125, 240)
    
**Note:** The commands will not work if the provided values are outside of the specified ranges.

* **set\_all\_leds**(*red*, *green*, *blue*): sets all of RVR's LEDs to the color represented by the given red, green, and blue values.
  * *red* (int): an integer from 0-255 indicating the desired red value
  * *green* (int): an integer from 0-255 indicating the desired green value
  * *blue* (int): an integer from 0-255 indicating the desired blue value
* **set\_rgb\_led\_by\_index**(*index*, *red*, *green*, *blue*): sets the indicated LED to the color represented by the given red, green, and blue values.
  * *index* (**LEDs**): a member of the **LEDs** class used to specify which LED is to be set
  * *red* (int): an integer from 0-255 indicating the desired red value
  * *green* (int): an integer from 0-255 indicating the desired green value
  * *blue* (int): an integer from 0-255 indicating the desired blue value

## RVRPower

The class containing all RVR power commands. All power commands are static, and can be called by typing `RVRPower.<command>`.

**Examples:**

    RVRPower.sleep()
    RVRPower.wake()

* **sleep**(): puts the robot in a soft sleep state.
* **wake**(): wakes the robot from sleep.
