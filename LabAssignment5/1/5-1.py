import numpy as np
import glfw
from OpenGL.GL import *
    
def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3ub(255, 255, 255)
    drawTriangle()
    drawFrame()

def render1():
    glLoadIdentity()
    th = np.radians(30)
    TR = np.array([[np.cos(-th),np.sin(-th),0,0],[-np.sin(-th),np.cos(-th),0,0],[0,0,1,0],[0,0,0,1]])
    TT = np.array([[1,0,0,0.6],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    glMultMatrixf(TT.T)
    glMultMatrixf(TR.T)
    drawFrame()
    glColor3ub(0,0,255)
    drawTriangle()

def render2():
    glLoadIdentity()
    th = np.radians(30)
    TR = np.array([[np.cos(-th),np.sin(-th),0,0],[-np.sin(-th),np.cos(-th),0,0],[0,0,1,0],[0,0,0,1]])
    TT = np.array([[1,0,0,0.6],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    glMultMatrixf(TR.T)
    glMultMatrixf(TT.T)
    drawFrame()
    glColor3ub(255,0,0)
    drawTriangle()

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    
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
    glfw.make_context_current(window)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        render1()
        render2()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
