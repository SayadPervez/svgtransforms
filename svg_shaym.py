import os
import cairo
from numpy import pi, sqrt

def svgResize2Drawing(path):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def svgRotate(path,angle,outputFileName = "new"):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="select-all:all;transform-rotate:{str(angle)};FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def createCanvas(width,height):
    with cairo.SVGSurface("canvas.svg", width,height) as surface:
        context = cairo.Context(surface)
        context.scale(700, 700)
        #context.stroke()


def Square(side,angle=0,name="Square"):
    filename=name+".svg"
    with cairo.SVGSurface(filename,side*2 ,side*2) as surface:
        cr = cairo.Context(surface)
        cr.rectangle(0,0,side,side)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)

def Rectangle(l,b,angle=0,name="Rectangle"):
    filename=name+".svg"
    with cairo.SVGSurface(filename,sqrt(l**2 + b**2) , sqrt(l**2+b**2)) as surface:
        cr = cairo.Context(surface)
        cr.rectangle(0,0,l,b)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename) 

def Circle(radius,name="Circle"):
    filename=name+".svg"
    with cairo.SVGSurface(filename,2.5*radius , 2.5*radius) as surface:
        cr = cairo.Context(surface)
        theta1=0
        theta2=2*pi
        cr.arc(radius+2,radius+2,radius,theta1,theta2)
        cr.fill()
        svgResize2Drawing(filename) 

def Cone(radius,height,angle=0,name="Cone"):
    filename=name+".svg"
    l=sqrt(radius**2 + height**2)
    theta1=0
    theta2=(radius/l)*(2*pi)
    with cairo.SVGSurface(filename,2.5*l,2.5*l) as surface:
        cr = cairo.Context(surface)
        cr.move_to(l+2,l+2)
        cr.arc(l+2,l+2,l,theta1,theta2)
        cr.close_path()
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)

def svg_arrange(shape_list,canvas_size):
    #Assuming shape_list = [[svg.Square(20),x1,y1],[svg.Circle(30),x2,y2],.....]
    with cairo.SVGSurface("file.svg", canvas_size[0], canvas_size[1]) as surface:
        cr = cairo.Context(surface)
