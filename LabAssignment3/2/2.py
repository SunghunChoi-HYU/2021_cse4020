import numpy as np
import glfw
from OpenGL.GL import *

gComposedM = np.array([[1,0,0],
                          [0,1,0],
                          [0,0,1]])

def key_callback(window, key, scancode, action, mods):
    global gComposedM
    
    if key==glfw.KEY_W:
        if action==glfw.PRESS or action ==glfw.REPEAT:
            newM = [[1,0,0],
                    [0,0.9,0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_E or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[1,0,0],
                    [0,1.1,0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_S or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[np.cos(10*np.pi/180),-np.sin(10*np.pi/180),0],
                    [np.sin(10*np.pi/180), np.cos(10*np.pi/180),0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_D or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[np.cos(-10*np.pi/180), -np.sin(-10*np.pi/180),0],
                    [np.sin(-10*np.pi/180), np.cos(-10*np.pi/180),0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_X or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[1,0,0.1],
                    [0,1,0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_C or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[1,0,-0.1],
                    [0,1,0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_R or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            newM = [[-1,0,0],
                    [0,-1,0],
                    [0,0,1]]
            gComposedM = newM @ gComposedM
    elif key==glfw.KEY_1 or action ==glfw.REPEAT:
        if action==glfw.PRESS:
            gComposedM = np.array([[1,0,0],
                          [0,1,0],
                          [0,0,1]])

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2fv((T @ np.array([.0,.5,1.]))[:-1])
    glVertex2fv((T @ np.array([.0,.0,1.]))[:-1])
    glVertex2fv((T @ np.array([.5,.0,1.]))[:-1])
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
        render(gComposedM)
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
