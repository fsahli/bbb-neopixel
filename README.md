bbb-neopixel
============

A web interface to control each of the LEDs of a Neopixel bar using a Beagle Bone Black rev C.

Dependencies:

- Flask
- LEDscape (enables a OPC (Open Pixel Control) server to control the LED using the BBB) https://github.com/osresearch/LEDscape
- Fadecandy, is a Python OPC client. The file opc.py is included in this repo. https://github.com/scanlime/fadecandy/

TODO:
- Add "Select all" check box
- Add color squares for each LED, showing the present color.


![Alt text](Neopixel.png?raw=true "Web Interface")

![Alt text](Neopixel_BBB.jpg?raw=true "Hardware")
