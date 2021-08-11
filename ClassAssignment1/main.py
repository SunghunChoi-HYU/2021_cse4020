import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

gCamAng = -105
elevation = 180
gPress = 0
gFov = 1
gLastX = 480
gLastY = 480
gXoffset = 0
gYoffset = 0
gSetting = 0

def drawUnitCube():
    glBegin(GL_QUADS)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
 
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()
    
def key_callback(window,key,scancode, action, mods):
    global gXoffset, gYoffset, gFov, gSetting
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_V:
            if gSetting == 0:
                gSetting = 1
            else:
                gSetting = 0

def mouse_button_callback(window, button, action, mods):
    global gPress

    if action == glfw.PRESS:
        if button == glfw.MOUSE_BUTTON_LEFT:
            gPress = 1
        if button == glfw.MOUSE_BUTTON_RIGHT:
            gPress = 2

    elif action == glfw.RELEASE:
        gPress = 0

def scroll_callback(window, xoffset, yoffset):
    global gFov

    if yoffset < 0:
            gFov += .5
    else :
        if gFov -.5 <=0:
            gFov = gFov
        else:
            gFov -= .5

def cursor_position_callback(winodw, xpos, ypos):
    global gLastX, gLastY, gCamAng, elevation, gXoffset, gYoffset

    xoffset = xpos - gLastX
    yoffset = gLastY - ypos
    gLastX = xpos
    gLastY = ypos

    if gPress == 1:
        gCamAng += xoffset * 0.005
        elevation -= yoffset * 0.005

    elif gPress == 2:
        gXoffset += xoffset * 0.005
        gYoffset += yoffset * 0.005
        
def render():
    global gCamAng, elevation, gXoffset, gYoffset
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    glLoadIdentity()

    if gSetting == 0:
        glFrustum(-1,1,-1,1,1,50)
    else :
        glOrtho(-7, 7, -7, 7, -7, 7)
    glTranslatef(gXoffset, gYoffset, 0)
    if(np.cos(-elevation) < 0):
        gluLookAt(5*np.sin(-gCamAng)*np.cos(elevation), -5*np.sin(elevation), 5*np.cos(-gCamAng)*np.cos(elevation), 0,0,0, 0,1,0)
    else:
        gluLookAt(5*np.sin(-gCamAng)*np.cos(elevation), -5*np.sin(elevation), 5*np.cos(-gCamAng)*np.cos(elevation), 0,0,0, 0,-1,0)
    glOrtho(-gFov, gFov, -gFov, gFov, -gFov, gFov)
    
    drawFrame()
    glColor3ub(255, 255, 255)
    drawGrid()
    drawUnitCube()

def drawUnitGrid():
    glBegin(GL_LINES)
    glColor3ub(255,255,255)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glVertex3f(1,0,1)
    glVertex3f(0,0,1)
    glVertex3f(1,0,1)
    glVertex3f(1,0,0)
    glEnd()

def drawGrid():
    for i in range(6):
            for k in range(6):
                glPushMatrix()
                glTranslatef(-i+2,0,-k+2)
                drawUnitGrid()
                glPopMatrix()

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([20.,0.,0.]))
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0.,0.,0.]))
    glVertex3fv(np.array([0.,20.,0.]))
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0.,0.,0]))
    glVertex3fv(np.array([0.,0.,20.]))
    glEnd()

def main():
    
    if not glfw.init():
        return
    window = glfw.create_window(640,640,"", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()

