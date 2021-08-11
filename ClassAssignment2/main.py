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
gVertex = []
gNormal = []
iarr = []
varr = []
narr = []
normalArr = []
gIndexArray = np.array([])
gVertexArray = np.array([])
gNormalArray = np.array([])
gVertexS = []
gNormalS = []
iarrS = []
varrS = []
narrS = []
normalArrS = []
gIndexArrayS = np.array([])
gVertexArrayS = np.array([])
gNormalArrayS = np.array([])
gVertexE = []
gNormalE = []
iarrE = []
varrE = []
narrE = []
normalArrE = []
gIndexArrayE = np.array([])
gVertexArrayE = np.array([])
gNormalArrayE = np.array([])
gVertexM = []
gNormalM = []
iarrM = []
varrM = []
narrM = []
normalArrM = []
gIndexArrayM = np.array([])
gVertexArrayM = np.array([])
gNormalArrayM = np.array([])
face_3 = 0
face_4 = 0
face_5 = 0
face_3S = 0
face_4S = 0
face_5S = 0
face_3E = 0
face_4E = 0
face_5E = 0
face_3M = 0
face_4M = 0
face_5M = 0

def drawArray():
    global gVertex, iarr, gVertexArray, gIndexArray, varr, face_3, face_4, face_5

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    
    index1 = 0
    
    for i in range(len(iarr)) :
        
        if(len(iarr[i]) == 3):
            index = 3
            glVertexPointer(3, GL_FLOAT, 3*gVertexArray.itemsize, gVertexArray)
            glNormalPointer(GL_FLOAT, 3*gNormalArray.itemsize, gNormalArray)
            glDrawArrays(GL_TRIANGLES, index1, int(((gVertexArray.size)/3 - face_4 - face_5)/face_3))
            index1 += 3
        elif(len(iarr[i]) == 4):
            index = 4
            glVertexPointer(3, GL_FLOAT, 3*gVertexArray.itemsize, gVertexArray)
            glNormalPointer(GL_FLOAT, 3*gNormalArray.itemsize, gNormalArray)
            glDrawArrays(GL_QUADS, index1, int(((gVertexArray.size)/3 - face_3 - face_5)/face_4))
            index1 += 4
        else:
            index = len(iarr[i])
            glVertexPointer(3, GL_FLOAT, 3*gVertexArray.itemsize, gVertexArray)
            glNormalPointer(GL_FLOAT, 3*gNormalArray.itemsize, gNormalArray)
            glDrawArrays(GL_POLYGON, 0, int(((gVertexArray.size)/3 - face_3 - face_4)/face_5))
            index1 += len(varr[i])

def drawSun():
    global gVertexS, iarrS, gVertexArrayS, gIndexArrayS, varrS, face_3S, face_4S, face_5S

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    
    index1 = 0

    drop_callback_Sun("Sun.obj")
    
    for i in range(len(iarrS)) :
        
        if(len(iarrS[i]) == 3):
            index = 3
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayS.itemsize, gVertexArrayS)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayS.itemsize, gNormalArrayS)
            glDrawArrays(GL_TRIANGLES, index1, int(((gVertexArrayS.size)/3 - face_4S - face_5S)/face_3S))
            index1 += 3
        elif(len(iarrS[i]) == 4):
            index = 4
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayS.itemsize, gVertexArrayS)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayS.itemsize, gNormalArrayS)
            glDrawArrays(GL_QUADS, index1, int(((gVertexArrayS.size)/3 - face_3S - face_5S)/face_4S))
            index1 += 4
        else:
            index = len(iarrS[i])
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayS.itemsize, gVertexArrayS)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayS.itemsize, gNormalArrayS)
            glDrawArrays(GL_POLYGON, 0, int(((gVertexArrayS.size)/3 - face_3S - face_4S)/face_5S))
            index1 += len(varrS[i])

def drawEarth():
    global gVertexE, iarrE, gVertexArrayE, gIndexArrayE, varrE, face_3E, face_4E, face_5E

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    
    index1 = 0

    drop_callback_Earth("Earth.obj")
    
    for i in range(len(iarrE)) :
        
        if(len(iarrE[i]) == 3):
            index = 3
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayE.itemsize, gVertexArrayE)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayE.itemsize, gNormalArrayE)
            glDrawArrays(GL_TRIANGLES, index1, int(((gVertexArrayE.size)/3 - face_4E - face_5E)/face_3E))
            index1 += 3
        elif(len(iarrE[i]) == 4):
            index = 4
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayE.itemsize, gVertexArrayE)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayE.itemsize, gNormalArrayE)
            glDrawArrays(GL_QUADS, index1, int(((gVertexArrayE.size)/3 - face_3E - face_5E)/face_4E))
            index1 += 4
        else:
            index = len(iarrE[i])
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayE.itemsize, gVertexArrayE)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayE.itemsize, gNormalArrayE)
            glDrawArrays(GL_POLYGON, 0, int(((gVertexArrayE.size)/3 - face_3E - face_4E)/face_5E))
            index1 += len(varrE[i])

def drawMoon():
    global gVertexM, iarrM, gVertexArrayM, gIndexArrayM, varrM, face_3M, face_4M, face_5M

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    
    index1 = 0

    drop_callback_Moon("Moon.obj")
    
    for i in range(len(iarrM)) :
        
        if(len(iarrM[i]) == 3):
            index = 3
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayM.itemsize, gVertexArrayM)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayM.itemsize, gNormalArrayM)
            glDrawArrays(GL_TRIANGLES, index1, int(((gVertexArrayM.size)/3 - face_4M - face_5M)/face_3M))
            index1 += 3
        elif(len(iarrM[i]) == 4):
            index = 4
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayM.itemsize, gVertexArrayM)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayM.itemsize, gNormalArrayM)
            glDrawArrays(GL_QUADS, index1, int(((gVertexArrayM.size)/3 - face_3M - face_5M)/face_4M))
            index1 += 4
        else:
            index = len(iarrM[i])
            glVertexPointer(3, GL_FLOAT, 3*gVertexArrayM.itemsize, gVertexArrayM)
            glNormalPointer(GL_FLOAT, 3*gNormalArrayM.itemsize, gNormalArrayM)
            glDrawArrays(GL_POLYGON, 0, int(((gVertexArrayM.size)/3 - face_3M - face_4M)/face_5M))
            index1 += len(varrM[i])

def drop_callback(window, paths):
    global gVertex, gNormal, iarr, gIndexArray, gVertexArray, varr, narr, normalArr, gNormalArray, face_3, face_4, face_5
    temp = []
    tempNormal = []
    gVertex = []
    gNormal = []
    iarr = []
    varr = []
    narr = []
    normalArr = []
    gIndexArray = np.array([])
    gVertexArray = np.array([])
    gNormalArray = np.array([])

    face_3 = 0
    face_4 = 0
    face_5 = 0
    
    file_name = paths[0].split('\\')
    print("File name : " + file_name[-1])
    file = open(paths[0], "r")
    while(True):
        line = file.readline()
        if not line:
            break
        OBJ_check = line.split()
        if OBJ_check[0] == 'v' : # Vertex
            gVertex.append((float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])))
        elif OBJ_check[0] == 'vn' : # normal
            gNormal.append( (float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])) )
        elif OBJ_check[0] == 'f':
            if len(OBJ_check[1:]) == 3:
                face_3 += 1
            elif len(OBJ_check[1:]) == 4:
                face_4 += 1
            else :
                face_5 += 1
            for i in range(len(OBJ_check)):
                if i == 0 :
                    continue
                vertex = OBJ_check[i].split("/")
                temp.append(int(float(vertex[0])) -1 )
                tempNormal.append(int(vertex[2])-1)
            iarr.append(temp)
            narr.append(tempNormal)
            temp = []
            tempNormal = []

    gIndexArray = np.array([iarr])

    for i in range(len(iarr)):
        for j in range(len(iarr[i])):
            vertexNumber = iarr[i][j]
            normalNumber = narr[i][j]
            vertex = gVertex[vertexNumber]
            normal = gNormal[normalNumber]
            varr.append(vertex)
            normalArr.append(normal)
            #varr.append(gNormal[vertexNumber])
    gVertexArray = np.array([varr], 'float32')
    gNormalArray = np.array([normalArr], 'float32')

    print("Total number of faces : " + str(face_3 + face_4 + face_5))
    print("Number of faces with 3 vertices : " + str(face_3))
    print("Number of faces with 4 vertices : " + str(face_4))
    print("Number of faces with more than 4 vertices : " + str(face_5))

def drop_callback_Sun(paths):
    global gVertexS, gNormalS, iarrS, gIndexArrayS, gVertexArrayS, varrS, narrS, normalArrS, gNormalArrayS, face_3S, face_4S, face_5S
    temp = []
    tempNormal = []
    gVertexS = []
    gNormalS = []
    iarrS = []
    varrS = []
    narrS = []
    normalArrS = []
    gIndexArrayS = np.array([])
    gVertexArrayS = np.array([])
    gNormalArrayS = np.array([])

    face_3S = 0
    face_4S = 0
    face_5S = 0
    

    file = open(paths, "r")
    while(True):
        line = file.readline()
        if not line:
            break
        OBJ_check = line.split()
        if OBJ_check[0] == 'v' : # Vertex
            gVertexS.append((float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])))
        elif OBJ_check[0] == 'vn' : # normal
            gNormalS.append( (float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])) )
        elif OBJ_check[0] == 'f':
            if len(OBJ_check[1:]) == 3:
                face_3S += 1
            elif len(OBJ_check[1:]) == 4:
                face_4S += 1
            else :
                face_5S += 1
            for i in range(len(OBJ_check)):
                if i == 0 :
                    continue
                vertex = OBJ_check[i].split("/")
                temp.append(int(float(vertex[0])) -1 )
                tempNormal.append(int(vertex[2])-1)
            iarrS.append(temp)
            narrS.append(tempNormal)
            temp = []
            tempNormal = []

    gIndexArrayS = np.array([iarrS])

    for i in range(len(iarrS)):
        for j in range(len(iarrS[i])):
            vertexNumber = iarrS[i][j]
            normalNumber = narrS[i][j]
            vertex = gVertexS[vertexNumber]
            normal = gNormalS[normalNumber]
            varrS.append(vertex)
            normalArrS.append(normal)
            #varr.append(gNormal[vertexNumber])
    gVertexArrayS = np.array([varrS], 'float32')
    gNormalArrayS = np.array([normalArrS], 'float32')

def drop_callback_Earth(paths):
    global gVertexE, gNormalE, iarrE, gIndexArrayE, gVertexArrayE, varrE, narrE, normalArrE, gNormalArrayE, face_3E, face_4E, face_5E
    temp = []
    tempNormal = []
    gVertexE = []
    gNormalE = []
    iarrE = []
    varrE = []
    narrE = []
    normalArrE = []
    gIndexArrayE = np.array([])
    gVertexArrayE = np.array([])
    gNormalArrayE = np.array([])

    face_3E = 0
    face_4E = 0
    face_5E = 0
    

    file = open(paths, "r")
    while(True):
        line = file.readline()
        if not line:
            break
        OBJ_check = line.split()
        if OBJ_check[0] == 'v' : # Vertex
            gVertexE.append((float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])))
        elif OBJ_check[0] == 'vn' : # normal
            gNormalE.append( (float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])) )
        elif OBJ_check[0] == 'f':
            if len(OBJ_check[1:]) == 3:
                face_3E += 1
            elif len(OBJ_check[1:]) == 4:
                face_4E += 1
            else :
                face_5E += 1
            for i in range(len(OBJ_check)):
                if i == 0 :
                    continue
                vertex = OBJ_check[i].split("/")
                temp.append(int(float(vertex[0])) -1 )
                tempNormal.append(int(vertex[2])-1)
            iarrE.append(temp)
            narrE.append(tempNormal)
            temp = []
            tempNormal = []

    gIndexArrayE = np.array([iarrE])

    for i in range(len(iarrE)):
        for j in range(len(iarrE[i])):
            vertexNumber = iarrE[i][j]
            normalNumber = narrE[i][j]
            vertex = gVertexE[vertexNumber]
            normal = gNormalE[normalNumber]
            varrE.append(vertex)
            normalArrE.append(normal)
            #varr.append(gNormal[vertexNumber])
    gVertexArrayE = np.array([varrE], 'float32')
    gNormalArrayE = np.array([normalArrE], 'float32')

def drop_callback_Moon(paths):
    global gVertexM, gNormalM, iarrM, gIndexArrayM, gVertexArrayM, varrM, narrM, normalArrM, gNormalArrayM, face_3M, face_4M, face_5M
    temp = []
    tempNormal = []
    gVertexM = []
    gNormalM = []
    iarrM = []
    varrM = []
    narrM = []
    normalArrM = []
    gIndexArrayM = np.array([])
    gVertexArrayM = np.array([])
    gNormalArrayM = np.array([])

    face_3M = 0
    face_4M = 0
    face_5M = 0
    

    file = open(paths, "r")
    while(True):
        line = file.readline()
        if not line:
            break
        OBJ_check = line.split()
        if OBJ_check[0] == 'v' : # Vertex
            gVertexM.append((float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])))
        elif OBJ_check[0] == 'vn' : # normal
            gNormalM.append( (float(OBJ_check[1]), float(OBJ_check[2]), float(OBJ_check[3])) )
        elif OBJ_check[0] == 'f':
            if len(OBJ_check[1:]) == 3:
                face_3M += 1
            elif len(OBJ_check[1:]) == 4:
                face_4M += 1
            else :
                face_5M += 1
            for i in range(len(OBJ_check)):
                if i == 0 :
                    continue
                vertex = OBJ_check[i].split("/")
                temp.append(int(float(vertex[0])) -1 )
                tempNormal.append(int(vertex[2])-1)
            iarrM.append(temp)
            narrM.append(tempNormal)
            temp = []
            tempNormal = []

    gIndexArrayM = np.array([iarrM])

    for i in range(len(iarrM)):
        for j in range(len(iarrM[i])):
            vertexNumber = iarrM[i][j]
            normalNumber = narrM[i][j]
            vertex = gVertexM[vertexNumber]
            normal = gNormalM[normalNumber]
            varrM.append(vertex)
            normalArrM.append(normal)
            #varr.append(gNormal[vertexNumber])
    gVertexArrayM = np.array([varrM], 'float32')
    gNormalArrayM = np.array([normalArrM], 'float32')
    
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

def key_callback(window,key,scancode, action, mods):
    global gXoffset, gYoffset, gFov, gSetting, polygonMode, hierachyMode
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_V:
            if gSetting == 0:
                gSetting = 1
            else:
                gSetting = 0
        elif key == glfw.KEY_Z:
            if polygonMode:
                polygonMode = False
            else:
                polygonMode = True
        elif key == glfw.KEY_H:
            if hierachyMode :
                hierachyMode = False
            else:
                hierachyMode = True
        
def render():
    global gCamAng, elevation, gXoffset, gYoffset, polygonMode
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    if polygonMode:
        glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
    else:
        glPolygonMode( GL_FRONT_AND_BACK, GL_FILL)

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

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_RESCALE_NORMAL)

    glPushMatrix()
    lightPos = (3,4,5,1)
    glLightfv (GL_LIGHT0, GL_POSITION, lightPos)
    glPopMatrix()

    lightColor = (1,0,0,1)
    ambientLightColor = (.1,0,0,1)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightColor)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLightColor)

    glPushMatrix()
    lightPos2 = (3,4,-5,1)
    glLightfv (GL_LIGHT1, GL_POSITION, lightPos2)
    glPopMatrix()

    lightColor2 = (0,1,0,1)
    ambientLightColor2 = (0,.1,0,1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightColor2)
    glLightfv(GL_LIGHT1, GL_SPECULAR, lightColor2)
    glLightfv(GL_LIGHT1, GL_AMBIENT, ambientLightColor2)

    objectColor = (1,1,1,1)
    specularObjectColor = (1,1,1,1)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, objectColor)
    glMaterialfv(GL_FRONT, GL_SHININESS, 10)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specularObjectColor)

    if not hierachyMode:
        glPushMatrix()
        glColor3ub(255,255,255)
        drawArray()
        glPopMatrix()

    else:
        t = glfw.get_time()
        glPushMatrix()
        glTranslatef(np.sin(t), 0,0)
        glRotatef(t*180, 0,1,0)
    
        glPushMatrix()
        glColor3ub(255,0,0)
        drawSun()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(15,0,0)
        glRotatef(t*(180/np.pi), 0,1,0)

        glPushMatrix()
        glColor3ub(0,0,255)
        drawEarth()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(5,0,0)
        glRotatef(t*(180/np.pi)/28,0,1,0)
        glColor(255,255,0)
        drawMoon()
        glPopMatrix()

        glPopMatrix()
        glPopMatrix()
            
    glDisable(GL_LIGHTING)

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
    global gVertex, gNormal, iarr, polygonMode, hierachyMode, varr
    polygonMode = True
    hierachyMode = False
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
    glfw.set_drop_callback(window,drop_callback)

        
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
