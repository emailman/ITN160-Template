import physense_emu
from time import sleep

# Get reference to the emulator
sensor = physense_emu.Sensor()

print('Remember to start the simulator by running physense_emuX.py')

sleep(2)

# Turn on red led
sensor.output('rled', 'on')
sleep(2)

# Turn off red led
sensor.output('rled', 'off')
sleep(2)
