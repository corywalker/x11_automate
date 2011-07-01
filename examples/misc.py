from x11_automate import *
from time import sleep

active = get_active_window()
print 'bla', active.get_geometry()
 
print get_pixel_color(0, 0)
print search(name="System Monitor")
print search(name="System Monitor", onlyvisible=True)[0].get_pid()
'''
mousemove(0, 0)
sleep(1)
click_at(100, 100, 3)
sleep(1)
click_at(500, 100, 1)
'''
