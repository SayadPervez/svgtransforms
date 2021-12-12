import os
import cairo

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

svgResize2Drawing("./new.svg")