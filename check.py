import os

def svgRotate(path,angle,outputFileName = "new"):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="select-all:all;transform-rotate:{str(angle)};FitCanvasToDrawing;export-filename:{outputFileName}.svg;export-do;" {path}')
    #os.system(f'inkscape  --actions="FitCanvasToDrawing;export-filename:{outputFileName}.svg;export-do" {path}')
        

svgRotate("new.svg",25)
#inkscape --verb=EditSelectAll --verb=AlignHorizontalCenter --verb=AlignVerticalCenter --verb=FileSave --verb=FileQuit foo.svg
#
#inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose --verb=FileQuit new.svg