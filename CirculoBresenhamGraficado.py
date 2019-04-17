from OpenGL.GL import * #GL, gl
from OpenGL.GLU import * #GLUT, glut
from OpenGL.GLUT import *

def display():
	print("aqui estoy display")
	glClear(GL_COLOR_BUFFER_BIT)

	glColor3f(0,0,0)

	glBegin(GL_POINTS)

	for i in range (-250,250+1):
		glVertex2i(0,i)
		glVertex2i(i,0)

	glColor3f(1,0,0)
	
	ArregloPuntos = circluloBresenham(50,110,110)

	i=0
	while i < len (ArregloPuntos):
		ArregloPuntos[i][0] *= 2
		ArregloPuntos[i][1] *= 2
		ArregloPuntos[i][0] += 100
		ArregloPuntos[i][1] += 100

		i+=1
	#######################################
	for p in ArregloPuntos:
		glVertex2iv(p)
		
	#######################################
	
	glEnd()

	glFlush()
	
def reshape(winW,winH):
	print("aqui hay un reshape",winW,winH)
	glViewport(0,0,winW,winH)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-250,250,-250,250)

	#################################
def circluloBresenham(r,h,k): #h,k son para "x" y "y"

	x,y=0,r
	DPK=3-2*r
	puntos=[]

	while x<=y:
		puntos.append([x,y])
		puntos.append([x,-y])
		puntos.append([-x,y])
		puntos.append([-x,-y])

		puntos.append([y,x])
		puntos.append([y,-x])
		puntos.append([-y,x])
		puntos.append([-y,-x])
		
		if DPK >=0:
			DPK=DPK+4*(x-y)+10
			y-=1
		else:
			DPK=DPK+4*x+6
		x+=1

	return puntos
	###############################
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutInitWindowSize(500,500)
glutCreateWindow(b'b0225')
glClearColor(1,1,1,0) #red, green, blue, alpha
glutDisplayFunc(display) #Evento display
glutReshapeFunc(reshape)
glutMainLoop()