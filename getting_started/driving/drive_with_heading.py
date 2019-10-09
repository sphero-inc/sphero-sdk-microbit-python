from microbit import sleep
from sphero import RVRDrive, RVRPower


# wait for RVR to turn on
RVRPower.wake()
sleep(2000)

# drive forward
count = 0
while count < 15:
    RVRDrive.drive(60, 0)
    sleep(200)
    count += 1

# drive to the right
count = 0
while count < 15:
    RVRDrive.drive(60, 90)
    sleep(200)
    count += 1

# drive back
count = 0
while count < 15:
    RVRDrive.drive(60, 180)
    sleep(200)
    count += 1

# drive to the left
count = 0
while count < 15:
    RVRDrive.drive(60, 270)
    sleep(200)
    count += 1

# stop driving
RVRDrive.stop(270)
