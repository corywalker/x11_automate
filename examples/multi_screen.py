from x11_automate import *
from time import sleep
from subprocess import Popen, PIPE

delay = 0.7

# Start amdccle
c = 'gksudo amdcccle &'
Popen(c, stdout=PIPE, shell=True)

sleep(4)
ccc = search(name="Catalyst Control Center", onlyvisible=True)[0]
ccc.move(0, 0)
ccc.activate()

sleep(delay)
click_at(84, 184)
sleep(delay)
click_at(655, 412)
sleep(delay)
click_at(775, 505)
sleep(delay + 1)
click_at(580, 147)
sleep(delay)
mouse_move(600, 193)
sleep(delay)
mouse_move(693, 216)
sleep(delay)
click_at(835, 283)
sleep(delay)
click_at(177, 573)

sleep(4)
dn = search(name="Display Notification", onlyvisible=True)[0]
dn.move(0, 0)
dn.activate()

sleep(delay)
click_at(210, 147)
