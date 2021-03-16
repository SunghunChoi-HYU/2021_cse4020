import numpy as np
import glfw
from OpenGL.GL import *
    
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
    glfw.make_context_current(window)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        t = glfw.get_time()
        T = np.array([[np.cos(t), -np.sin(t), 0],
                     [np.sin(t), np.cos(t), 0],
                     [0,0,1]])
        
        S = np.array([[np.cos(0.5), -np.sin(0.5),.4],
                     [np.sin(0.5),np.cos(0.5),.4],
                     [0., 0., 0.]])
        render(T@S)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
