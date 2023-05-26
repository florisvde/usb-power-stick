# Changes
Documents the changes between hardware versions. Commits are tagged with the version number.
## v1.1:
- Removed transistor inverter and solder jumper.
- Replaced output transistor with an easier to solder one (SOT-723 -> SOT-23).
- Added pull down resistor on the gate of the output transistor.
- Increased inline gate resistor to be the same value as the LED's current limiting resistor.
- Added a 74HC74D flip flop + Power on Reset circuit.
- Added a status LED and current limiting resistor.
- Reannotated the schematic, thus references may not match between v1.0 and v1.1.
## v1.0:
- First version, not on GitHub.
- Used RTS line of the CH340 to directly drive a MOSFET. During testing it was discovered that the RTS line idles high when the serial port is closed, and leaving the port open is problematic, script wise.
