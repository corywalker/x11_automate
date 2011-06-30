from py_xdotool import *
from time import sleep

print getactivewindow()
print search(name="System Monitor")
print search(name="System Monitor", onlyvisible=True)[0].get_name()
'''
mousemove(0, 0)
sleep(1)
click_at(100, 100, 3)
sleep(1)
click_at(500, 100, 1)
'''
