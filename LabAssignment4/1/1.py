import numpy as np
import glfw
from OpenGL.GL import *

global gComposedM
gComposedM = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
def key_callback(window, key, scancode, action, mods):
    global gComposedM
    
    if key==glfw.KEY_Q:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            newM = [[1,0,0,0.1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            gComposedM = newM@gComposedM
    elif key==glfw.KEY_E:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            newM = [[1,0,0,-0.1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            gComposedM = newM@gComposedM
    elif key==glfw.KEY_A:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            th = np.radians(10)
            newM = [[np.cos(th),-np.sin(th),0,0],[np.sin(th),np.cos(th),0,0],[0,0,1,0],[0,0,0,1]]
            gComposedM = newM@gComposedM
    elif key==glfw.KEY_D:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            th = np.radians(10)
            newM = [[np.cos(-th),-np.sin(-th),0,0],[np.sin(-th),np.cos(-th),0,0],[0,0,1,0],[0,0,0,1]]
            gComposedM = newM@gComposedM
    elif key==glfw.KEY_1:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            gComposedM = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

def render():
    global gComposedM
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    glColor3ub(255, 255, 255)
    glMultMatrixf(gComposedM.T)
    drawTriangle()
    
def drawTriangle():
    glBegin(GL_TRIANGLES)
    glVertex2fv(np.array([0.,.5]))
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([.5,0.]))
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

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        newM = glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
