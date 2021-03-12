import numpy as np
import glfw
from OpenGL.GL import *

x = np.linspace(0, 2 *np.pi,13)
key_input = 3

def key_callback(window, key, scancode, action, mods):
    global x
    global key_input
    if key==glfw.KEY_1:
        if action==glfw.PRESS:
            key_input = 2
    elif key==glfw.KEY_2:
        if action==glfw.PRESS:
            key_input = 1
    elif key==glfw.KEY_3:
        if action==glfw.PRESS:
            key_input = 0
    elif key==glfw.KEY_4:
        if action==glfw.PRESS:
            key_input = -2
    elif key==glfw.KEY_5:
        if action==glfw.PRESS:
            key_input = -3
    elif key==glfw.KEY_6:
        if action==glfw.PRESS:
            key_input = -4
    elif key==glfw.KEY_7:
        if action==glfw.PRESS:
            key_input = -5
    elif key==glfw.KEY_8:
        if action==glfw.PRESS:
            key_input = -6
    elif key==glfw.KEY_9:
        if action==glfw.PRESS:
            key_input = -7
    elif key==glfw.KEY_0:
        if action==glfw.PRESS:
            key_input = -8
    elif key==glfw.KEY_Q:
        if action==glfw.PRESS:
            key_input = -9
    elif key==glfw.KEY_W:
        if action==glfw.PRESS:
            key_input = -10
    
def render():
    global x
    global key_input
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINE_LOOP)
    for i in range(len(x)):
        glVertex2f(np.cos(x[i]),np.sin(x[i]))
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(np.cos(x[key_input]),np.sin(x[key_input]))
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480,480,"2019061721", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, key_callback)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
