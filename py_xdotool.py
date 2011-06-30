from subprocess import Popen, PIPE

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
        
    def activate(self):
        c = "windowactivate %d" % self.wid
        return run_command(c)
        
    def focus(self):
        c = "windowfocus %d" % self.wid
        return run_command(c)

def getactivewindow():
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

def mousemove(x, y):
    c = "mousemove %d %d" % (x, y)
    return run_command(c)
    
def click(btn):
    c = "click %d" % btn
    return run_command(c)

def click_at(x, y, btn):
    mousemove(x, y)
    return click(btn)
    
def run_command(c):
    return Popen("xdotool " + c, stdout=PIPE, shell=True).stdout.read()
