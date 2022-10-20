from art import *
from datetime import datetime
from tqdm import tqdm
import time
import os
import netifaces
import ascii_magic
import buzz

# Clear Terminal
clear = lambda: os.system('clear')

# Grab and format current time
now = datetime.now()
current_time = now.strftime("%H:%M")

# Simualte bios load screen
clear()
tprint("Bios Load V.02")

for i in tqdm(range(100)):
    time.sleep(.01)
   
time.sleep(.5)
tprint("Load Successful")
time.sleep(1)
clear()
time.sleep(1)

# Simulate terminal launch
term_art = ascii_magic.from_image_file('scripts/image_files/cyberdeck.bmp',columns=200,mode=ascii_magic.Modes.ASCII)
ascii_magic.to_terminal(term_art)
buzzer = buzz.Buzzer()
buzzer.play(2)
time.sleep(1)
print('\n'+ '-'*150)
print(f'Current Time: {current_time}')
print('Testing Uplink/Downlink Status')
print("Up-link Packet Data")
for i in range(10):
    print("*"*i)
    time.sleep(.1)
time.sleep(1)
print('\nDown-link Packet Data\n')
for i in reversed(range(10)):
    print("*"*i)
    time.sleep(.1)
try:
    print('Hardline Status: Online\n\t'+ netifaces.ifaddresses('eth0')[2][0]['addr'])
except:
    print("Hardline Status: Offline\n\tCheck Transmission Config!")

try:
    print('\nWireless Status: Online\n\t ' + netifaces.ifaddresses('wlan0')[2][0]['addr'])

except:
    print("\nWireless Status: Offline\n\tCheck Transmission Config!")

input("\n\nBoot complete, hit return to enter CLI...")

