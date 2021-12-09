def getSVGdimensions(svgContentsList):
    widthStr=[]
    heightStr=[]
    for _ in svgContentsList:
        if("width" in _ and widthStr!=None):
            widthStr.append(_)
        if("height" in _ and heightStr!=None):
            heightStr.append(_)
        if('id="svg5"' in _):
            if(len(heightStr)!=0 and len(widthStr)!=0):
                pass
            else:
                raise Exception("Not an inkscape SVG")
    width = float((widthStr[0])[widthStr[0].index("width=\"")+7:widthStr[0].index("mm")])
    height = float((heightStr[0])[heightStr[0].index("height=\"")+8:heightStr[0].index("mm")])

    return(width,height)

def svgRotate(filename,angle):
    with open(filename,"r") as f:
        originalSVGlist=f.readlines()
    w,h = getSVGdimensions(originalSVGlist)
    
    ind=None
    for i,x in enumerate(originalSVGlist):
        if('id="svg5"' in x):
            ind = i
            break
    
    if(ind==None):
        raise Exception("Not an Inkscape SVG")
    else:
        originalSVGlist[ind]+=f'transform = "translate({str(w)}, {str(h)}) rotate({str(angle)})"\n'
    tranformedSVG=''.join(originalSVGlist)
    with open("./new.svg",'w') as f:
        f.write(tranformedSVG)

svgRotate("./x.svg",90)