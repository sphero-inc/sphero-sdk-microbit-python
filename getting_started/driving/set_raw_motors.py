from microbit import sleep
from sphero import RVRDrive, RawMotorModes, RVRPower


# wait for RVR to turn on
RVRPower.wake()
sleep(2000)

# drive forward with speed 60
count = 0
while count < 15:
    RVRDrive.set_raw_motors(RawMotorModes.FORWARD, 60, RawMotorModes.FORWARD, 60)
    sleep(200)
    count += 1

# stop and wait 1 second
RVRDrive.set_raw_motors(RawMotorModes.OFF, 0, RawMotorModes.OFF, 0)
sleep(1000)

# drive backward with speed 60
count = 0
while count < 15:
    RVRDrive.set_raw_motors(RawMotorModes.BACKWARD, 60, RawMotorModes.BACKWARD, 60)
    sleep(200)
    count += 1

# stop and wait 1 second
RVRDrive.set_raw_motors(RawMotorModes.OFF, 0, RawMotorModes.OFF, 0)
sleep(1000)

# drive forward with speed 80 on the left motor and speed 40 on the right motor
count = 0
while count < 20:
    RVRDrive.set_raw_motors(RawMotorModes.FORWARD, 80, RawMotorModes.FORWARD, 40)
    sleep(200)
    count += 1

# stop and wait 1 second
RVRDrive.set_raw_motors(RawMotorModes.OFF, 0, RawMotorModes.OFF, 0)
sleep(1000)

# drive forward with speed 40 on the left motor and speed 80 on the right motor
count = 0
while count < 20:
    RVRDrive.set_raw_motors(RawMotorModes.FORWARD, 40, RawMotorModes.FORWARD, 80)
    sleep(200)
    count += 1

# stop
RVRDrive.set_raw_motors(RawMotorModes.OFF, 0, RawMotorModes.OFF, 0)
