from subprocess import Popen, PIPE

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
