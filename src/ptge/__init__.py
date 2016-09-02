#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import sys
import array

from time import sleep

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Ptge():
    ESCAPE = '\033'

    # Number of the glut window.
    window = 0
    def __init__(self):
        self.vertices = array.array('f', [-1,-1,1, #vlevo dole predemnou
                                          -1,1,1, #vlevo nahore predemnou
                                          1,1,1, #vpravo nahore predemnou
                                          1,-1,1, #vpravo dole predmnou
                                          -1,-1,-1,
                                          -1,1,-1,
                                          1,1,-1,
                                          1,-1,-1 ] )

        self.colors = array.array('f', [ 0, 0, 0,
                                         1, 0, 0,
                                         1, 1, 0,
                                         0, 1, 0,
                                         0, 0, 1,
                                         1, 0, 1,
                                         1, 1, 1,
                                         0, 1, 1] )

        self.cIndices = array.array('B', [0, 3, 2, 1,  2, 3, 7, 6,  0, 4, 7, \
                3, 1, 2, 6, 5,  4, 5, 6, 7,  0, 1, 5, 4 ] )

        self.animationAngle = 0.0
        self.frameRate = 30

        self._gl_init()

    def _gl_init(self):
        glutInit(())
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(100, 100)
        glutCreateWindow("Project Thunder")
        glClearColor (0, 0, 0, 0)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

    def draw(self):
        glutDisplayFunc(self._draw_scene)
        glutIdleFunc(self._idle_scene)
        glutMainLoop()

    def _draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #muzu zmensit vykreslovany obrazek v okne
        glViewport(0, 0, 640, 640)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #gluLookAt(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        gluPerspective(90.0, 1.0, 0.1, 100.0)
        #glOrtho - je vhodne pro 2D objekty (ukazatele zivotu atd...)
        glOrtho(-4, 4, -4, 4, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(self.animationAngle, 1, 1, 0)
        glEnableClientState(GL_COLOR_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, self.colors.tostring())
        glVertexPointer(3, GL_FLOAT, 0, self.vertices.tostring())
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE,
                       self.cIndices.tostring())
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
        glutSwapBuffers()

    def _idle_scene(self):
        self.animationAngle += 2
        while self.animationAngle > 360:
            self.animationAngle -= 360
        sleep(1 / float(self.frameRate))
        glutPostRedisplay()


