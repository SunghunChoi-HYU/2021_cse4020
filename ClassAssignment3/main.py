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
joint_name = []
offset = []
push_pop = []
chan_cnt = 0
chan = []
motion = []
drag_drop = False
spbar = 0
frame_cnt = 0
frame = 2
chans = []

def key_callback(window,key,scancode, action, mods):
    global gXoffset, gYoffset, gFov, gSetting, spbar
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_V:
            if gSetting == 0:
                gSetting = 1
            else:
                gSetting = 0
        elif key == glfw.KEY_SPACE:
            if spbar == 0:
                spbar +=1
            else:
                spbar -=1

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

def drop_callback(window, paths):
    global joint_name, offset, push_pop, chan_cnt, chan, drag_drop, motion, frame_cnt, chans
    push = 0
    pop = 0
    drag_drop = True
    joint_name = []
    line_chan = []
    line_motion = []
    offset = []
    motion = []
    chan = []
    push_pop = []
    chans = []
    
    chan_cnt = 0
    file_name = paths[0].split("\\")
    print("File name : " + file_name[-1])
    file = open(paths[0], "r")

    while(True):
        line = file.readline()
        if not line:
            break
        BVH_check = line.split()
        if BVH_check[0] == "HIERARCHY" or BVH_check[0] == "MOTION":
            continue

        elif BVH_check[0] == "End":
            continue

        elif BVH_check[0] == "ROOT" or BVH_check[0] == "JOINT":
            joint_name.append(BVH_check[1])

        elif BVH_check[0] == "Frames:" or BVH_check[0] == "Frames" :
            frame_cnt = BVH_check[1]
            print("Number of frames : " + BVH_check[1])

        elif BVH_check[0] == "Frame" :
            print("FPS : " + str(1/float(BVH_check[2])))

        elif BVH_check[0] == "OFFSET" :
            line_offset = [float(BVH_check[1]), float(BVH_check[2]), float(BVH_check[3])]
            offset.append(line_offset)

        elif BVH_check[0] == "{" or BVH_check[0] == "}":
            push_pop.append(BVH_check[0])

        elif BVH_check[0] == "CHANNELS" :
            chan = []
            chan_cnt += int(BVH_check[1])
            for i in range(len(BVH_check) - 2):
                chan.append([BVH_check[i+2],"0"])
            chans.append(chan)

        else:
            k = 0
            for i in range(len(chans)):
                for j in range(len(chans[i])):
                    chans[i][j].append(BVH_check[k])
                    k+=1
                
            
    print("Number of joints : " , len(joint_name))
    print("List of all joint names ", " ".join(joint_name))
        
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

    if(drag_drop):
        drawSkeleton()

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

def drawSkeleton():
    global offset, push_pop, chan, motion, frame, chans
    j = -1
    chan_index = 0
    
    if not spbar:
        for i in range(len(push_pop)):
            if(push_pop[i] == "{") :
                glPushMatrix()
                j +=1
                n2 = np.array(offset[j])
                glBegin(GL_LINES)
                glColor3ub(255, 255, 255)
                glVertex3fv(np.array([0,0,0]))
                glVertex3fv(n2)
                glEnd()
                glTranslatef(offset[j][0], offset[j][1], offset[j][2])

            elif(push_pop[i] == "}") :
                 glPopMatrix()

    if spbar:
        k = -1
        chan_index = 0
        for i in range(len(push_pop)):
            if(push_pop[i] == "{"):
                xpos = 0
                ypos = 0
                zpos = 0
                glPushMatrix()
                k+=1
                n2 = np.array(offset[k])
                glBegin(GL_LINES)
                glColor3ub(255, 255, 255)
                glVertex3fv(np.array([0,0,0]))
                glVertex3fv(n2)
                glEnd()
                glTranslatef(offset[k][0], offset[k][1], offset[k][2])

                if(push_pop[i+1] == "}"):
                   continue
                
                for j in range(len(chans[chan_index])):
                    if(chans[chan_index][j][0] == "XPOSITION" or chans[chan_index][j][0] == "Xposition"):
                        xpos = chans[chan_index][j][frame]
                    elif(chans[chan_index][j][0] == "YPOSITION" or chans[chan_index][j][0] == "Yposition"):
                        ypos = chans[chan_index][j][frame]
                    elif(chans[chan_index][j][0] == "ZPOSITION" or chans[chan_index][j][0] == "Zposition"):
                        zpos = chans[chan_index][j][frame]

                if xpos != 0 and ypos != 0 and zpos != 0:
                    glTranslatef(float(xpos), float(ypos), float(zpos))

                for j in range(len(chans[chan_index])):
                    if(chans[chan_index][j][0] == "XROTATION" or chans[chan_index][j][0] == "Xrotation"):
                        glRotatef(float(chans[chan_index][j][frame]), 1, 0, 0)
                    elif(chans[chan_index][j][0] == "YROTATION" or chans[chan_index][j][0] == "Yrotation"):
                        glRotatef(float(chans[chan_index][j][frame]), 0, 1, 0)
                    elif(chans[chan_index][j][0] == "ZROTATION" or chans[chan_index][j][0] == "Zrotation"):
                        glRotatef(float(chans[chan_index][j][frame]), 0, 0, 1)

                

                chan_index += 1
                
            elif(push_pop[i]== "}"):
                glPopMatrix()
        frame = (int(frame) + 1) % (int(frame_cnt) + 1)
        if frame == 0:
            frame = 2
            
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
    glfw.set_drop_callback(window, drop_callback)

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()

