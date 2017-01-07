# pocket-phone
Connect a Fona808 to PocketChip
Currently this software only support dialing out, no recieved calls or sms...
yet.  

Requirements
------------

-Python 2.7
-pySerial module
-time module
-And of course a pocketChip and Fona808 GSM module

Very Basic Hardware Setup
-------------------------

To start with wire up the Fona to the PocketChip wit the following configuration:
FONA TX -> PocketChip RX
FONA RX -> PocketChip Tx
FONA GND -> PocketChip GND
FONA Key -> PocketChip Gnd
FONA VIO -> PocketChip 3v

Software Setup
--------------

Next, you'll need to disable getty services for the UART
In terminal:
$ sudo systemctl stop serial-getty@ttyS0.service

Unfortunately Getty will restart after a reboot, so add:
sudo systemctl mask serial-getty@ttyS0.service

To run the applicaion, navigate to file's folder and run from command line:
$ python pocket-phone.py

