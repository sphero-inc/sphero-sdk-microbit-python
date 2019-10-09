from microbit import sleep
from sphero import RVRLed, LEDs, RVRPower


# wait for RVR to turn on
RVRPower.wake()
sleep(2000)

# turn all LEDs off and wait 2 seconds
RVRLed.set_all_leds(0, 0, 0)
sleep(2000)

while True:
    # turn all LEDS off
    RVRLed.set_all_leds(0, 0, 0)

    # set headlights to red
    RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT, 255, 0, 0)
    RVRLed.set_rgb_led_by_index(LEDs.LEFT_HEADLIGHT, 255, 0, 0)

    # wait 1 second
    sleep(1000)

    # set headlights to yellow
    RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT, 255, 255, 0)
    RVRLed.set_rgb_led_by_index(LEDs.LEFT_HEADLIGHT, 255, 255, 0)

    # wait 1 second
    sleep(1000)

    # set headlights to green
    RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT, 0, 255, 0)
    RVRLed.set_rgb_led_by_index(LEDs.LEFT_HEADLIGHT, 0, 255, 0)

    # wait 1 second
    sleep(1000)

    # set headlights to blue
    RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT, 0, 0, 255)
    RVRLed.set_rgb_led_by_index(LEDs.LEFT_HEADLIGHT, 0, 0, 255)

    # wait one second
    sleep(1000)

    # set all LEDs to white and wait 2 seconds
    RVRLed.set_all_leds(255, 255, 255)
    sleep(2000)
