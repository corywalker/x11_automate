from subprocess import Popen, PIPE
import PIL.Image # python-imaging
import PIL.ImageStat # python-imaging
import Xlib.display # python-xlib

class Window:
    def __init__(self, wid):
        assert type(wid) == int
        self.wid = wid
        
    def get_wid(self):
        return self.wid
    
    def get_pid(self):
        c = "getwindowpid %d" % self.wid
        return int(run_command(c))
    
    def get_name(self):
        c = "getwindowname %d" % self.wid
        return run_command(c)
    
    def get_geometry(self):
        # TODO: should be parsed into Python objects
        c = "getwindowgeometry %d" % self.wid
        return run_command(c)
    
    def set_size(self, width, height):
        c = "windowsize %d %d %d" % (self.wid, width, height)
        return run_command(c)
    
    def move(self, x, y):
        c = "windowmove %d %d %d" % (self.wid, x, y)
        return run_command(c)
        
    def activate(self):
        c = "windowactivate %d" % self.wid
        return run_command(c)
        
    def focus(self):
        c = "windowfocus %d" % self.wid
        return run_command(c)
        
    def screen_map(self):
        c = "windowmap %d" % self.wid
        return run_command(c)
        
    def minimize(self):
        c = "windowminimize %d" % self.wid
        return run_command(c)
        
    def kill(self):
        c = "windowkill %d" % self.wid
        return run_command(c)
        
# Lifted from http://rosettacode.org/wiki/Color_of_a_screen_pixel
def get_pixel_color(i_x, i_y):
	o_x_root = Xlib.display.Display().screen().root
	o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
	o_pil_image_rgb = PIL.Image.fromstring("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
	lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
	return tuple(map(int, lf_colour))

def get_focused_window():
    c = "getactivewindow"
    wid = int(run_command(c))
    return Window(wid)

def get_active_window():
    c = "getactivewindow"
    wid = int(run_command(c))
    return Window(wid)
    
def get_windows(wids):
    windows = []
    for wid in wids:
        windows.append(Window(wid))
    return windows

def search(**kwargs):
    c = "search"
    noargs = ["onlyvisible", "class", "classname", "all", "any", "sync"]
    for arg in noargs:
        if arg in kwargs:
            if kwargs[arg]:
                c += " --%s" % arg
    if "name" in kwargs:
        c += ' --name "%s"' % kwargs['name']
    if "pid" in kwargs:
        c += " --pid %s" % kwargs['pid']
    str_wids = run_command(c).split()
    wids = []
    for str_wid in str_wids:
        wids.append(int(str_wid))
    return get_windows(wids)

def mouse_move(x, y):
    c = "mousemove %d %d" % (x, y)
    return run_command(c)
    
def click(btn):
    c = "click %d" % btn
    return run_command(c)

def click_at(x, y, btn=1):
    mouse_move(x, y)
    return click(btn)
    
def run_command(c):
    return run_command_raw("xdotool " + c)
    
def run_command_raw(c):
    return Popen(c, stdout=PIPE, shell=True).stdout.read()
    
