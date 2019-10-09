# Rainbow Racer
Race against your friends! In this game, RVR's LEDs will randomly change colors. Your job is to press the button that matches the color of RVR's LEDs. The better you do, the faster he'll go! If you hit the wrong button or you wait too long to press a button, RVR will slow down, so try to keep up!

## Parts List
If you want to build your own Rainbow Racer, you will need the following parts (most of them are included in [this nifty kit from SparkFun]):
* RVR
* [BBC micro:bit]
* Micro B USB cable (preferably a long one!)
* [SparkFun micro:bit Breakout (with Headers)]
* Breadboard
* 12 Jumper Wires
* 4 Multi-Colored Momentary Push Buttons (we used red, green, blue, and yellow)
* 4 10K Ω Resistors

## Instructions
First you'll need to put together your circuit! Follow the below wiring diagram:

![wiring diagram]

After you've got your circuit set up, you're ready to flash the code to your micro:bit. Follow the below steps:
* Download the [rainbow\_racer.py] and [sphero.py] files. `rainbow_racer.py` is the file that will run on the micro:bit, and `sphero.py` contains the functions you'll need to be able to interact with RVR using your micro:bit. You'll notice that `RVRDrive` and `RVRLed` are imported from `sphero.py` at the top of the `rainbow_racer.py` file.
* We're going to use an editor called Mu to edit our MicroPython code and flash it to the micro:bit. You can follow [this link] if you don't already have Mu downloaded on your computer. [This link is useful] if you haven't used Mu with micro:bit before.
* Once you've opened Mu, you'll need to open the `rainbow_racer.py` file in Mu. Do this by clicking the **Load** button at the top of the screen and navigating to the `rainbow_racer.py` file (it's probably in your downloads folder).
* You'll also need to put the `sphero.py` file in a place where Mu can reach it. Find a folder called **mu\_code**; it should have been created automatically when Mu was downloaded. Move `sphero.py` into the **mu\_code** folder.
* Now we can flash the code onto your micro:bit! Plug your micro:bit into your computer using the Micro B USB cable. After a few seconds, you'll see a message along the bottom of Mu's interface that says "Detected new BBC micro:bit device."
* After that message has appeared, you can click the **Flash** button at the top of the screen. You'll see the orange light on the back of the micro:bit flash for a few seconds while the code is being flashed to the device.
* Once the flashing stops, you'll see an error message scroll across micro:bit's LED matrix: "Line 3 ImportError no module named 'sphero'". This is because your micro:bit doesn't have access to the `sphero.py` file. To fix that, we're going to copy the file onto the micro:bit. Click the **Files** button at the top of the screen. This will open a window at the bottom of the screen showing the files you have on your micro:bit on the left and the files in the **mu\_code** folder on the right. Drag the `sphero.py` file from the right side to the left side to copy it onto your micro:bit. This should just take a couple seconds.
* Now you're good to go! Just eject the micro:bit from your computer before you unplug the USB cable and you're ready to race!

## The Race
To start the race all you'll need to do is plug the micro:bit (which should be mounted in the breakout board) into the RVR using the USB cable, and then turn on the RVR. You'll need to walk with the RVR as it moves since it's plugged into your micro:bit - that's why we suggested finding a long cable! If you have a friend that built their own Rainbow Racer, you can race them! Consider putting tape lanes and a finish line on the ground to have an official race track (keep in mind that the RVR will only drive in a straight line). If you're flying solo, run multiple races and keep track of your times. See if you can beat your own high score!

## Now What?
Try to improve your Rainbow Racer! Here are some ideas to get you started:
* Speed things up by playing with some of the values in the `rainbow_racer.py` file.
* Need more of a challenge? Add more buttons and colors!
* Add a joystick to your circuit so you can steer your RVR.
* The breadboard circuit can be pretty clunky to race with - try designing a better controller!

If you're adding a lot to your code, you may run into some Memory Errors. That's okay - micro:bit is best for smaller projects. If you feel like you've outgrown your micro:bit, try upgrading to an [Arduino] or a [Raspberry Pi]!


[this nifty kit from SparkFun]: https://www.sparkfun.com/products/14542
[BBC micro:bit]: https://microbit.org
[SparkFun micro:bit Breakout (with Headers)]: https://www.sparkfun.com/products/13989
[wiring diagram]: Rainbow%20Racer_bb.png
[rainbow\_racer.py]: rainbow_racer.py
[sphero.py]: sphero.py
[this link]: https://codewith.mu
[This link is useful]: https://codewith.mu/en/tutorials/1.0/microbit
[Arduino]: https://www.arduino.cc
[Raspberry Pi]: https://www.raspberrypi.org
