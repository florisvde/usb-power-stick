# USB Power Stick
The USB Power Stick is a USB stick to control power to a USB powered device from a PC or SBC.

<img src="assets/usb-power-stick.jpg" align="center" height="200">

It is designed to turn an IKEA HÅRTE USB powered light on and off using a Python script running on a Raspberry Pi.
The light is used to illuminate a 3D FFF printer, controlled by Octoprint so a webcam can track the printer's progression during the night. 

The Stick makes use of a USB to serial converter, a flip flop and an output transistor to switch power on and off 
to the device connected to the Stick's output. The Stick does not provide USB connectivity to the Stick's output.

## How does it work
The RTS line of a serial port idles high at all times. RTS can only be manipulated when the port is opened. 
Closing the port sets RTS to high again.

By connecting the RTS line to the flip flop's (FF) data input (D) and the TX line to the FF's clock input (C), 
the RTS state is latched to the FF's output (Q) when a character is sent.

R2 limits capacitive charging spike from the gate.

R1 and C4 perform a Power on Reset (PoR) of the flip flop.

## Build your own
The board is designed with manual assembly in mind, all parts are easily soldered down using a standard soldering iron and some tweezers. 
You can send the Gerber files to any PCB manufacturer and have the boards made. For everything but the passives a shop link is provided in the Bill of Materials (BOM).
