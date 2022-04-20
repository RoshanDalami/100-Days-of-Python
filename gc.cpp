#include<GL/glut.h>
void init(void){
    glClearColor(1.0,1.0,1.0,0.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0.0,200.0,0.0,150.0);

}
void printSegment(void){
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0,0.4,0.2);
    glBegin(GL_LINES);
    glVertex2i(180,15);
    glVertex2i(10,145);
    glEnd();
    glFlush();
}
void main(int argc,char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutInitWindowSize(400,300);
    glutInitWindowPosition(50,100);
    glutCreateWindow("An example of openGL program");
    init();
    glutDisplayFunc(printSegment);
    glutMainLoop();
}